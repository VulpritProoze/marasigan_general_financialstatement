import tkinter as tk 
from tkinter import ttk


class StatementOfChanges:
    def __init__(self, root):
        self.root = root
        self.root.title("Dr. Nick Marasigan, Statement of Changes")

        self.heading_label = ttk.Label(root, justify="center", text="Dr. Nick Marasigan, M.D.\nStatement of Changes in Owner's Equity\nFor the period ended October 2015", font=("Helvetica 9 bold"))
        self.heading_label.grid(row=0, column=0, columnspan=6)

        self.table = ttk.Treeview(self.root, show="headings")
        self.table["columns"] = ("1", "2")
        self.table_widths = (300, 100)
        for i, column in enumerate(self.table["columns"]):
            self.table.heading(column, text="")
            self.table.column(column, width=self.table_widths[i], stretch=False)
        self.table.grid(row=1, column=0, sticky="nw", pady=10, padx=10)

        # Create a vertical scrollbar and link it to the treeview
        self.y_scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.grid(row=1, column=1, sticky="ns")
        
        self.display_entries(self.table)
        
        # Make the window not resizable
        self.root.resizable(width=False, height=False)
 

    def display_entries(self, table):
        entries = [
            ("Marasigan, Capital, Starting", "250,000"),
            ("ADD: Profit", "220,333.33 Php"),
            ("", ""),
            ("Balance", "470,333"),
            ("Less: Marasigan, Withdrawal", "200,000.00 Php"),
            ("", ""),
            ("Marasigan, Capital, Ending", "270,333.00 Php"),
            
        ]
        for entry in entries:
            table.insert("", tk.END, values=entry)
            
            
# fawk this
if __name__ == "__main__":
    root = tk.Tk()
    app = StatementOfChanges(root)
    root.mainloop()
