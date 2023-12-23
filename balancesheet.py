import tkinter as tk 
from tkinter import ttk


class BalanceSheet:
    def __init__(self, root):
        self.root = root
        self.root.title("Dr. Nick Marasigan, Balance Sheet")

        self.heading_label = ttk.Label(root, justify="center", text="Dr. Nick Marasigan, M.D.\nBalance Sheet\nFor the period ended October 2015", font=("Helvetica 9 bold"))
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
            ("ASSETS", ""),
            ("", ""),
            ("Current Assets", ""),
            ("Cash", "114,000"),
            ("Accounts Receivable", "204,000"),
            ("Medical Supplies", "21,000"),
            ("Prepaid Insurance", "18,333.33"),
            ("Total Current Assets", "357,333.33 Php"),
            ("", ""),
            ("Non-current Assets", ""),
            ("Land", "250,000"),
            ("Medical Building", "1,000,000"),
            ("Less: Accumulated Depreciation - Medical Building", "(5,000)"),
            ("Medical Equipment", "465,000"),
            ("Less: Accumulated Depreciation - Medical Equipment", "(9,000)"),
            ("Total Non-current Assets", "1,701,000.00 Php"),
            ("", ""),
            ("TOTAL ASSETS", "2,058,333.33 Php"),
            ("", ""),
            ("LIABILITY AND OWNER'S EQUITY", ""),
            ("", ""),
            ("Liability", ""),
            ("24% Notes Payable", "400,000"),
            ("20% Notes Payable", "1,200,000"),
            ("Accounts Payable", "49,000"),
            ("Salaries Payable", "51,000"),
            ("Interest Payable", "28,000"),
            ("Unearned Research Revenues", "60,000"),
            ("Total Liability", "1,788,000.00 Php"),
            ("", ""),
            ("Owner's Equity", ""),
            ("Marasigan, Capital, Ending", "270,333.00 Php"),
            ("", ""),
            ("TOTAL LIABILITY AND OWNER'S EQUITY", "2,058,333.33 Php"),
        ]
        for entry in entries:
            table.insert("", tk.END, values=entry)
            
            
# fawk this
if __name__ == "__main__":
    root = tk.Tk()
    app = BalanceSheet(root)
    root.mainloop()
