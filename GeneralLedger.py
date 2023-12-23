import tkinter as tk
from tkinter import ttk


class GeneralLedger:
    def __init__(self, root):
        self.root = root
        self.root.title("Dr. Nick Marasigan, General Ledger")

        self.heading_label = ttk.Label(root, justify="center", text="Dr. Nick Marasigan, M.D.\nGeneral Ledger\nFor the month ended October 31, 2021", font=("Helvetica 9 bold"))
        self.heading_label.grid(row=0, column=0, columnspan=6)

        self.tree = ttk.Treeview(root, show="headings")
        self.tree["columns"] = ("Month", "Day", "Particulars", "PR", "Debit", "Credit")

        self.tree.heading("Month", text="Month")
        self.tree.heading("Day", text="Day")
        self.tree.heading("Particulars", text="Particulars")
        self.tree.heading("PR", text="PR")
        self.tree.heading("Debit", text="Debit")
        self.tree.heading("Credit", text="Credit")

        self.tree.column("Month", width=50)
        self.tree.column("Day", width=50)
        self.tree.column("Particulars", width=300)
        self.tree.column("PR", width=50)
        self.tree.column("Debit", width=75)
        self.tree.column("Credit", width=75)

        self.tree.grid(row=1, column=0, padx=10, pady=10)

        # Create a vertical scrollbar and link it to the treeview
        self.tree_scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scrollbar.set)

        # Place the scrollbar to the right of the treeview
        self.tree_scrollbar.grid(row=1, column=1, sticky="ns")
        
        self.display_entries()
        
        # Make the window not resizable
        self.root.resizable(width=False, height=False)
 

    def display_entries(self):
        entries = [
            ("Oct", "1", "Cash", "110", "250,000", ""),
            ("", "", "\tMarasigan, Capital", "310", "", "250,000"),
            ("", "", "", "", "", ""),
            ("", "", "Medical Building", "160", "1,000,000", ""),
            ("", "", "Land", "150", "250,000", ""),
            ("", "", "\tCash", "110", "", "50,000"),
            ("", "", "\t20% Notes Payable", "220", "", "1,200,000"),
            ("", "", "", "", "", ""),
            ("", "2", "Insurance Expense", "520", "20,000", ""),
            ("", "", "\tCash", "110", "", "20,000"),
            ("", "", "", "", "", ""),
            ("", "4", "Cash", "110", "117,000", ""),
            ("", "", "\tMedical Revenues", "410", "", "117,000"),
            ("", "", "", "", "", ""),
            ("", "7", "Medical Supplies", "130", "17,000", ""),
            ("", "", "\tAccounts Payable", "230", "", "17,000"),
            ("", "", "", "", "", ""),
            ("", "10", "Salaries Expense", "510", "73,000", ""),
            ("", "", "\tCash", "110", "", "73,000"),
            ("", "", "", "", "", ""),
            ("", "12", "Cash", "110", "90,000", ""),
            ("", "", "\tUnearned Research Revenue", "260", "", "90,000"),
            ("", "", "", "", "", ""),
            ("", "18", "Accounts Receivable", "120", "317,000", ""),
            ("", "", "\tMedical Revenues", "410", "", "317,000"),
            ("", "", "", "", "", ""),
            ("", "21", "Repairs Expense", "530", "23,000", ""),
            ("", "", "\tCash", "110", "", "23,000"),
            ("", "", "", "", "", ""),
            ("", "23", "Telephone Expense", "560", "3,000", ""),
            ("", "", "\tCash", "110", "", "3,000"),
            ("", "", "", "", "", ""),
            ("", "24", "Medical Equipment", "170", "45,000", ""),
            ("", "", "\tAccounts Payable", "230", "", "45,000"),
            ("", "", "", "", "", ""),
            ("", "25", "Cash", "110", "113,000", ""),
            ("", "", "\tAccounts Receivable", "120", "", "113,000"),
            ("", "", "", "", "", ""),
            ("", "27", "Accounts Payable", "230", "13,000", ""),
            ("", "", "\tCash", "110", "", "13,000"),
            ("", "", "", "", "", ""),
            ("", "30", "Marasigan, Withdrawals", "320", "200,000", ""),
            ("", "", "\tCash", "110", "", "200,000"),
            ("", "", "", "", "", ""),
            ("", "", "Association Dues Expense", "550", "15,000", ""),
            ("", "", "\tCash", "110", "", "15,000")
        ]

        for entry in entries:
            self.tree.insert("", tk.END, values=entry)
# fawk this
if __name__ == "__main__":
    root = tk.Tk()
    app = GeneralLedger(root)
    root.mainloop()
