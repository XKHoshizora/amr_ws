import os
from pathlib import Path

def should_skip_file(filename, script_name, output_file):
    """Check if the file should be skipped for content merging"""
    skip_extensions = {
        '.git', '.md', '.png', '.dae', '.rviz', '.sh', 
        '.pyc', '.jpg', '.jpeg', '.bmp', 
        '.pdf', '.doc', '.docx', '.exe', '.bin'
    }
    
    # Skip files without extension (like 'LICENSE'), files with unwanted extensions,
    # and the script itself or its output file
    return (
        not os.path.splitext(filename)[1] or 
        os.path.splitext(filename)[1].lower() in skip_extensions or
        filename == script_name or filename == output_file
    )

def generate_tree(path, prefix="", is_last=True, script_name=None, output_file=None):
    """Generate a tree structure string for a directory"""
    output = []
    base_name = os.path.basename(path)

    # Skip .git directory or the script/output files in tree view
    if base_name in {'.git', script_name, output_file}:
        return []

    connector = "└─" if is_last else "├─"
    output.append(f"{prefix}{connector}{base_name}")

    child_prefix = prefix + ("   " if is_last else "│  ")

    if os.path.isdir(path):
        items = sorted(os.listdir(path))
        for i, item in enumerate(items):
            item_path = os.path.join(path, item)
            is_last_item = (i == len(items) - 1)
            output.extend(generate_tree(item_path, child_prefix, is_last_item, script_name, output_file))

    return output

def get_language_from_extension(ext):
    """Return language identifier for markdown code blocks based on file extension"""
    ext_map = {
        '.py': 'python',
        '.cpp': 'cpp',
        '.c': 'c',
        '.h': 'cpp',
        '.xml': 'xml',
        '.txt': '',
        '.msg': '',
        '.srv': '',
        'CMakeLists.txt': 'cmake'
    }
    return ext_map.get(ext, '')

def combine_files(project_path, output_file, script_name):
    """Combine all files in the project into a single markdown file"""
    with open(output_file, 'w', encoding='utf-8') as out_file:
        # Write project structure first
        out_file.write("# Project Structure\n\n````\n")
        tree = generate_tree(project_path, script_name=script_name, output_file=output_file)
        out_file.write('\n'.join(tree))
        out_file.write("\n````\n\n# Files Content\n")

        # Then write all files content
        for root, _, files in os.walk(project_path):
            # Skip .git directory
            if '.git' in root:
                continue

            for file in sorted(files):  # Sort files for consistent output
                if should_skip_file(file, script_name, output_file):
                    continue

                file_path = Path(root) / file
                rel_path = file_path.relative_to(project_path)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    out_file.write(f"\n## File: {rel_path}\n\n")
                    lang = get_language_from_extension(file_path.suffix)
                    if file == "CMakeLists.txt":
                        lang = get_language_from_extension(file)

                    out_file.write(f"```{lang}\n")
                    out_file.write(content)
                    if not content.endswith('\n'):
                        out_file.write('\n')
                    out_file.write("```\n")
                except UnicodeDecodeError:
                    out_file.write(f"*Binary file: {rel_path}*\n")
                except Exception as e:
                    print(f"Error processing file {file_path}: {str(e)}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    output_file = "combined_files.md"
    script_name = os.path.basename(__file__)
    combine_files(current_dir, output_file, script_name)
    print(f"Files combined successfully into {output_file}")
