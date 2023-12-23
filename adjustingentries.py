import tkinter as tk 
from tkinter import ttk


class AdjustingEntries:
    def __init__(self, root):
        self.root = root
        self.root.title("Dr. Nick Marasigan, Adjusting Entries")

        self.heading_label = ttk.Label(root, justify="center", text="Dr. Nick Marasigan, M.D.\nAdjusting Entries", font=("Helvetica 9 bold"))
        self.heading_label.grid(row=0, column=0, columnspan=6)

        self.table = ttk.Treeview(self.root, show="headings")
        self.table["columns"] = ("", "Account Titles", "Debit", "Credit")
        self.table_widths = (75, 300, 100, 100)
        for i, column in enumerate(self.table["columns"]):
            self.table.heading(column, text=column)
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
            ("A", "Insurance Expense", "1,666.67", ""),
            ("", "\tPrepaid Insurance", "", "1,666.67"),
            ("B", "Supplies Expense", "35,000", ""),
            ("", "\tMedical Supplies", "", "35,000"),
            ("C", "Depreciation Expense - Medical Building", "5,000", ""),
            ("", "\tAccumulated Depreciation - Medical Building", "", "5,000"),
            ("", "Depreciation Expense - Medical Equipment", "9,000", ""),
            ("", "\tAccumulated Depreciation - Medical Equipment", "", "9,000"),
            ("D", "Unearned Research Revenues", "30,000", ""),
            ("", "\tResearch Revenues", "", "30,000"),
            ("E", "Salaries Expense", "51,000", ""),
            ("", "\tSalaries Payable", "", "51,000"),
            ("F", "Interest Expense", "28,000", ""),
            ("", "\tInterest Payable", "", "28,000"),
            ("TOTAL", "", "159,666.67 Php", "159.666.67 Php")
        ]
        for entry in entries:
            table.insert("", tk.END, values=entry)
            
            
# fawk this
if __name__ == "__main__":
    root = tk.Tk()
    app = AdjustingEntries(root)
    root.mainloop()
