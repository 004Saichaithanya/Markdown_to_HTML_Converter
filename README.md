# 📄 Markdown to HTML Converter 🖥️

A simple Python command-line tool that reads a `.md` (Markdown) file and converts it into a clean, well-formatted `.html` file. It supports standard Markdown syntax like headers, bold, italics, lists, links, and inline code.

---

## 📌 Approach

The tool uses Python's `markdown` library to parse and convert Markdown content into HTML format. Command-line arguments are handled with `argparse`, allowing users to specify the input and output file paths. It reads the content of the Markdown file, converts it to HTML, and saves the result to a new file.

Basic error handling ensures that invalid or missing input files are reported to the user.

---

## 📦 Dependencies

| Library    | Purpose                                   |
| :--------- | :---------------------------------------- |
| `markdown` | Converts Markdown text to HTML format     |
| `argparse` | Handles command-line arguments (built-in) |
| `os`       | Checks file existence (built-in)          |

---

## 📥 Installation

Install the required `markdown` package if you haven't already:

```bash
pip install markdown
```

---

## 🎮 How to Use

1. **Save the script as `md_to_html.py`.**
2. **Run the script from your terminal:**

```bash
python md_to_html.py input_file.md output_file.html
```

**Example:**

```bash
python md_to_html.py sample.md result.html
```

✔️ This will convert `sample.md` to `result.html`.

---

## 📑 Supported Markdown Syntax

* Headers (`#`, `##`, etc.)
* Bold (`**text**`)
* Italics (`*text*`)
* Lists (`- item`)
* Links (`[title](URL)`)
* Inline code (`` `code` ``)

---

## 📸 Example

**sample.md**

```markdown
# Hello World

This is a **bold** text and *italic* text.

- Item 1
- Item 2

[OpenAI](https://openai.com)

Inline: `print("Hello")`
```

✔️ Converts to clean HTML code with proper tags.

---

## 💡 Future Improvements

* Add HTML boilerplate (`<html>`, `<head>`, `<body>`)
* Option to apply custom CSS styling
* Live preview in browser

---

## 📜 License

Open source for educational/demo purposes under the MIT License.
#
