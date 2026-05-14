import tkinter as tk
from tkinter import ttk
from search_function import search
from similar_users import find_similar_movies

def main():
    root = tk.Tk()
    root.title("Movie Recommender")
    root.geometry("800x600")

    #Search Box
    tk.Label(root, text="Search Movie:", font=("Arial", 12)).pack(pady=10)
    search_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=search_var, font=("Arial", 12), width=40)
    entry.pack()

    #Search Results Table
    tk.Label(root, text="Search Results (click a movie):", font=("Arial", 10)).pack()
    # search_columns = ("title",)
    # search_tree = ttk.Treeview(root, columns=search_columns, show="headings", height=5)
    # search_tree.heading("title", text="Title")
    # search_tree.column("title", width=400)
    # search_tree.pack(pady=5, padx=10, fill="x")
    search_frame = tk.Frame(root)
    search_frame.pack(pady=5, padx=10, fill="x")

    search_tree = ttk.Treeview(search_frame, columns=("title",), show="headings", height=5)
    search_tree.heading("title", text="Title")
    search_tree.column("title", width=400)

    search_scroll = ttk.Scrollbar(search_frame, orient="vertical", command=search_tree.yview)
    search_tree.configure(yscrollcommand=search_scroll.set)

    search_tree.pack(side="left", fill="x", expand=True)
    search_scroll.pack(side="right", fill="y")

    #Recommendations Table
    tk.Label(root, text="Recommended Movies:", font=("Arial", 10)).pack()
    rec_columns = ("score", "title", "genres")
    rec_tree = ttk.Treeview(root, columns=rec_columns, show="headings", height=10)
    rec_tree.heading("score", text="Score")
    rec_tree.heading("title", text="Title")
    rec_tree.heading("genres", text="Genres")
    rec_tree.column("score", width=80)
    rec_tree.column("title", width=300)
    rec_tree.column("genres", width=300)
    rec_tree.pack(pady=5, padx=10, fill="both", expand=True)

    # stores movieId mapped to title for clicked row lookup
    movie_map = {}

    def on_type(*args):
        query = search_var.get().strip()
        for row in search_tree.get_children():
            search_tree.delete(row)
        movie_map.clear()
        if len(query) < 2:
            return
        results = search(query)
        for _, row in results.iterrows():
            iid = search_tree.insert("", "end", values=(row["title"],))
            movie_map[iid] = row["movieId"]

    def on_select(event):
        selected = search_tree.focus()
        if not selected:
            return
        movie_id = movie_map.get(selected)
        if movie_id is None:
            return
        for row in rec_tree.get_children():
            rec_tree.delete(row)
        recs = find_similar_movies(movie_id)
        if recs.empty:
            rec_tree.insert("", "end", values=("***", "No recommendations found", "***"))
            return
        for _, row in recs.iterrows():
            rec_tree.insert("", "end", values=(f"{row['score']:.2f}", row["title"], row["genres"]))

    search_var.trace("w", on_type)
    search_tree.bind("<<TreeviewSelect>>", on_select)
    entry.focus()
    root.mainloop()

if __name__ == "__main__":
    main()