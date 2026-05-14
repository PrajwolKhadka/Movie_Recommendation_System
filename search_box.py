import tkinter as tk
from tkinter import ttk
from search_function import search

def main():
    root = tk.Tk()
    root.title("Movie Recommender")
    root.geometry("600x400")

    # Search box
    tk.Label(root, text="Search Movie:", font=("Arial", 12)).pack(pady=10)
    search_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=search_var, font=("Arial", 12), width=40)
    entry.pack()

    # Results table
    columns = ("title", "clean_title")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
    tree.heading("title", text="Title")
    tree.heading("clean_title", text="Clean Title")
    tree.column("title", width=300)
    tree.column("clean_title", width=260)
    tree.pack(pady=20, padx=10, fill="both", expand=True)

    def on_type(*args):
        query = search_var.get().strip()
        for row in tree.get_children():
            tree.delete(row)
        if len(query)<2:
            return
        results = search(query)
        for _, row in results.iterrows():
            tree.insert("", "end", values=(row["title"], row["clean_title"]))
    search_var.trace("w", on_type)

    entry.focus()
    root.mainloop()

if __name__ == "__main__":
    main()

