import tkinter as tk 
from tkinter import ttk 

class TrialBalance:
    def __init__(self, root):
        self.root = root
        self.root.title("Dr. Marasigan, Trial Balance")
        
        self.heading = ttk.Label(self.root, justify="center", text="Dr. Marasigan, M.D.\nTrial Balance\nOctober 31, 2021", font=("Helvetica 9 bold"))
        self.heading.grid(row=0, column=0, pady=10)
        
        self.table = ttk.Treeview(self.root, show="headings")
        self.table["columns"] = ("Account Titles", "F", "Debit", "Credit")
        
        self.table.heading("Account Titles", text="Account Titles")
        self.table.heading("F", text="F")
        self.table.heading("Debit", text="Debit")
        self.table.heading("Credit", text="Credit")
        
        self.table.column("Account Titles", width=300)
        self.table.column("F", width=75)
        self.table.column("Debit", width=75)
        self.table.column("Credit", width=75)
    
        self.table.grid(row=1, column=0, pady=10, padx=10)
        
        self.display_entries()
        
        # Scrollbar
        self.y_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.grid(row=1, column=1, sticky="ns", padx=(0,5), pady=10)
        self.root.resizable(width=False, height=False)
 
        
    def display_entries(self):
        table_entries = [
            ("Cash", "110", "114,000", ""),
            ("Accounts Receivable", "120", "204,000", ""),
            ("Medical Supplies", "130", "56,000", ""),
            ("Land", "150", "250,000", ""),
            ("Medical Building", "160", "1,000,000", ""),
            ("24% Notes Payable", "170", "465,000", ""),
            ("20% Notes Payable", "210", "", "400,000"),
            ("Accounts Payable", "220", "", "1,200,000"),
            ("Unearned Research Revenue", "230", "", "49,000"),
            ("Marasigan, Capital", "260", "", "90,000"),
            ("Marasigan, Withdrawals", "310", "", "250,000"),
            ("Medical Revenues", "320", "200,000", ""),
            ("Salaries Expense", "410", "", "434,000"),
            ("Insurance Expense", "510", "73,000", ""),
            ("Repairs Expense", "520", "20,000", ""),
            ("Association Dues Expense", "550", "15,000", ""),
            ("Telephone Expense", "560", "3,000", ""),
            ("TOTAL", "", "2,423,000 Php", "2,423,000 Php")
        ]

        for entry in table_entries:
            self.table.insert("", tk.END, values=entry) 
            
    
if __name__ == "__main__":
    root = tk.Tk()
    app = TrialBalance(root)
    root.mainloop()