import argparse
import markdown
import os

def convert_md_to_html(input_file, output_file):
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist.")
        return

    # Read Markdown content
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert to HTML
    html_content = markdown.markdown(md_content)

    # Write to HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ Conversion complete! HTML saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Markdown file to HTML.")
    parser.add_argument("input_file", help="Path to the input Markdown (.md) file")
    parser.add_argument("output_file", help="Path to the output HTML file")

    args = parser.parse_args()

    convert_md_to_html(args.input_file, args.output_file)
