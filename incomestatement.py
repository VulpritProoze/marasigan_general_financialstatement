import tkinter as tk 
from tkinter import ttk


class IncomeStatement:
    def __init__(self, root):
        self.root = root
        self.root.title("Dr. Nick Marasigan, Income Statement")

        self.heading_label = ttk.Label(root, justify="center", text="Dr. Nick Marasigan, M.D.\nIncome Statement\nFor the period ended October 31, 2015", font=("Helvetica 9 bold"))
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
            ("REVENUES", ""),
            ("Medical Revenues", "434,000"),
            ("Research Revenues", "30,000"),
            ("Total", "464,000.00 Php"),
            ("", ""),
            ("EXPENSES", ""),
            ("Salaries Expense", "124,000"),
            ("Insurance Expense", "1,667"),
            ("Repairs Expense", "23,000"),
            ("Supplies Expense", "35,000"),
            ("Association Dues Expense", "15,000"),
            ("Telephone Expense", "3,000"),
            ("Depreciation Expense - Building", "5,000"),
            ("Depreciation Expense - Equipment", "9,000"),
            ("Interest Expense", "28,000"),
            ("Total", "243,667.00 Php"),
            ("", ""),
            ("Profit", "220,333.00 Php")
        ]

        for entry in entries:
            table.insert("", tk.END, values=entry)
# fawk this
if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeStatement(root)
    root.mainloop()
