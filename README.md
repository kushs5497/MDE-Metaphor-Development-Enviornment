Simple Code Editor with Metaphor AI Integration
===================================================

This is a simple code editor implemented in Python using the tkinter library and Metaphor AI. It allows you to write code in various programming languages and provides the following functionalities:

1. Integration with Metaphor AI API for searching relevant content.
2. Auto-indentation to give an IDE-like feel.
3. Save functionality with support for multiple programming languages.


Usage
===================================================

Make sure you have Python installed on your system.

Install the required dependencies:

> pip install metaphor_python

Run the code editor with the desired programming language as an argument:

> python code_editor.py [programming_language]

Replace [programming_language] with the desired language (e.g., java, cpp, py).


Functionality Details
===================================================

Metaphor API Integration

Click the "Search Metaphor API" button to search for content related to the text enclosed in /::/ tags.

Auto Indentation

Press Enter after typing an open brace { to auto-indent and place a closing brace } on the next line.

Saving Files

Click the "Save" button to save the code. The file extension will be determined by the selected programming language.


Example Usage
===================================================

Run the code editor with a specific programming language:

> python code_editor.py java

Type code and use /::/ tags to indicate content for search.

Click the "Search Metaphor API" button to search for relevant content.

Use auto-indentation by typing an open brace and pressing Enter.

Click the "Save" button to save the file.
