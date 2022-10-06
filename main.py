import subprocess
from tkinter import *
import time
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import os


def space():
    space = Label(text="", bg="black")
    space.grid()


def open_directory():
    global directory_text
    filename = askdirectory()
    if len(filename) < 1:
        messagebox.showwarning("Error", "Directory is Empty!")
    else:
        subprocess.call(f"cd {filename}", shell=True)
        os.chdir(filename)
        directory_text.config(text=filename, fg="green")
        print(filename)


def execute_code():
    cwd = os.getcwd()
    text_box = link_box.get()
    if "https://github.com" in text_box:
        print(cwd)
        github_link = link_box.get()
        splitted_link = github_link.split("/")[4].split(".")[0]
        subprocess.call(f"echo # {splitted_link} >> README.md", shell=True)
        time.sleep(0.5)
        subprocess.call("git init", shell=True)
        time.sleep(0.5)
        subprocess.call("git add README.md", shell=True)
        time.sleep(0.5)
        subprocess.call(f"git commit -m '{splitted_link}'", shell=True)
        time.sleep(0.5)
        subprocess.call("git branch -M main", shell=True)
        time.sleep(2)
        subprocess.call(f"git remote add origin {github_link}", shell=True)
        time.sleep(0.3)
        subprocess.call("git push -u origin main", shell=True)
        messagebox.showinfo("Success", "Your Github upload was successful")


    else:
        messagebox.showwarning("Error", "Wrong Link Entered!")


root = Tk()

root.geometry("400x400")
root.title("Code Executer")
root.columnconfigure(0, weight=1)
root.config(bg="black")

space()
space()
space()

text = Label(root, text="Paste Github Repo Link", fg="#3dcc8e", bg="black", font=("arial", 11, "bold"))
text.grid()

space()
space()

EntryVar = StringVar()
link_box = Entry(root, width=50, textvariable=EntryVar)
link_box.grid()

space()

open_directory_btn = Button(root, width=15, height=2, bg="#3dcc8e", fg="black", text="Choose Directory",
                            command=open_directory)
open_directory_btn.grid()
directory_text = Label(root, text="", fg="#3dcc8e", bg="black", font=("arial", 11, "bold"))
directory_text.grid()

space()

execute_btn = Button(root, width=15, height=2, bg="#3dcc8e", fg="black", text="Execute", command=execute_code)
execute_btn.grid()

root.mainloop()
