import tkinter as tk  
from tkinter import ttk
import subprocess
import os

# Get the current directory of main.py
current_directory = os.path.dirname(os.path.abspath(__file__))

class Main:
    def __init__ (self, root):
        self.root = root
        self.root.title("Dr. Nick Marasigan, General Financial Reports")
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
  
        self.heading = tk.Label(self.root,justify="left", wraplength=600, font=("Helvetica 9 bold"), text="Dr. Nick Marasigan, upon completing a residency program at Harvard Medical established a medical practice in San Pablo, Laguna. During October 2022, the first month of operations, the following transactions occurred:")
        self.heading.grid(row=0, columnspan=3)
        
        self.tree = ttk.Treeview(root, show="headings")  # Exclude tree structure column

        self.tree["columns"] = ("Rows", "Account Titles", "Debit", "Credit")

        self.tree.heading("Rows", text="Rows")
        self.tree.heading("Account Titles", text="Account Titles")
        self.tree.heading("Debit", text="Debit")
        self.tree.heading("Credit", text="Credit")

        self.tree.column("Rows", width=50)
        self.tree.column("Account Titles", width=300)
        self.tree.column("Debit", width=75)
        self.tree.column("Credit", width=75)

        self.tree.grid(row=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.display_entries()

        button_names = [
            {"text": "Open General Ledger", "command": self.open_general_ledger},
            {"text": "Open Posting to the Ledger", "command": self.open_posting_to_ledger},
            {"text": "Open Trial Balance", "command": self.open_trial_balance},
            {"text": "Open Adjusting Entries", "command": self.open_adjusting_entries},
            {"text": "Open Worksheet", "command": self.open_worksheet},
            {"text": "Open Income Statement", "command": self.open_income_statement},
            {"text": "Open Balance Sheet", "command": self.open_balance_sheet},
            {"text": "Open Statement of Changes in Owner's Equity", "command": self.open_statement_changes}
        ]

        self.buttons = []
        
        rows = 2
        columns = 0
        index = 0
        while index < len(button_names):
            data = button_names[index]
            button = tk.Button(self.root, text=data["text"], command=data["command"])
            button.grid(row=rows, column=columns, pady=5)
            self.buttons.append(button)

            if (columns+1)%3 == 0:
                rows+=1
                columns=0
            else:
                columns+=1
            index+=1
          
        # Scrollbar y  
        self.y_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.grid(row=1, column=3, sticky="ns")
        
        
    def display_entries(self):
        self.root.resizable(width=False, height=False)
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
        ]

        for entry in entries:
            self.tree.insert("", tk.END, values=entry)    
            
            
    def open_general_ledger(self):
        # Open generalledger.py using subprocess
        subprocess.run(["python", os.path.join(current_directory, "generalledger.py")])
    
    def open_posting_to_ledger(self):
        subprocess.run(["python", os.path.join(current_directory, "postingtoledger.py")])
        
    def open_trial_balance(self):
        subprocess.run(["python", os.path.join(current_directory, "trialbalance.py")])

    def open_adjusting_entries(self):
        subprocess.run(["python", os.path.join(current_directory, "adjustingentries.py")])

    def open_worksheet(self):
        subprocess.run(["python", os.path.join(current_directory, "worksheet.py")])

    def open_income_statement(self):
        subprocess.run(["python", os.path.join(current_directory, "incomestatement.py")])

    def open_statement_changes(self):
        subprocess.run(["python", os.path.join(current_directory, "statementofchanges.py")])

    def open_balance_sheet(self):
        subprocess.run(["python", os.path.join(current_directory, "balancesheet.py")])


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
    