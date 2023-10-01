import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from metaphor_python import Metaphor
import sys

selected_language = str(sys.argv[1])

# Method to show the search result
def show_text_popup(text_within_tags,title, url):
    text_popup = tk.Toplevel(root)
    text_popup.title(text_within_tags)
    
    title_label = tk.Label(text_popup, text=title, font=('Arial', 12, 'bold'))
    title_label.pack(padx=20, pady=(20,5), anchor="w")

    url_label = tk.Label(text_popup, text=url, fg="blue", cursor="hand2")
    url_label.pack(padx=20, pady=5, anchor="w")
    url_label.bind("<Button-1>", lambda e: open_url(url))

# Browser Integration for Hyperlinks
def open_url(url):
    import webbrowser
    webbrowser.open_new(url)

# Actual search function using Metaphor AI API
def search_metaphor_api(text):
    try:
        metaphor = Metaphor("42058552-9c37-4627-938c-e2c88309affd")
        start = 0
        while True:
            start = text.find('/::/', start)
            if start == -1:
                break
            end = text.find('/::/', start + 4)
            if end != -1:
                text_within_tags = text[start+4:end]
                start = end + 4
                search_response = metaphor.search(selected_language + text_within_tags, num_results=1, use_autoprompt=True,)
                contents_response = search_response.get_contents()

                for content in contents_response.contents:
                    title = content.title
                    url = content.url

                    show_text_popup(text_within_tags,title, url)
            else:
                break
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Actual IDE feel function to auto indent. (This needs adjustment to support multiple languages)
def auto_indent(event):
    index = text_widget.index(tk.INSERT)
    line = text_widget.get(index.split('.')[0] + '.0', index)

    if event.keysym in ["Return", "KP_Enter"]:
        leading_spaces = len(line) - len(line.lstrip())

        if "{" in line:
            text_widget.insert(tk.INSERT, '\t\n}')
            text_widget.mark_set(tk.INSERT,index)

# Save file fucntion
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension="."+str(selected_language), filetypes=[("Text files", "*.txt"), ("Java Program", "*.java"), ("C++ Program", "*.cpp"), ("Python Program", "*.py")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(text_widget.get("1.0", 'end-1c'))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {str(e)}")

# Defining the Code editor UI
root = tk.Tk()
root.title("Code Editor")

# Inserting the basic text editor
text_widget = tk.Text(root)
text_widget.pack(expand=True, fill='both')

# Integrating the IDE functions
text_widget.bind('<Return>', auto_indent)
text_widget.bind('<KP_Enter>', auto_indent)

# Buttons
replace_button = tk.Button(root, text="Search Metaphor API", command=lambda: search_metaphor_api(text_widget.get("1.0",'end-1c')))
replace_button.pack()
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

root.mainloop()

