import tkinter as tk 
from tkinter import ttk

class Worksheet:
    def __init__(self, root):
        self.root = root
        self.root.title("Dr. Marasigan, Worksheet")
        self.root.resizable(width=False, height=False)
        
        self.heading = ttk.Label(self.root, justify="center", font=("Helvetica 9 bold"), text="Dr. Nick Marasigan, M.D.\nWorksheet\nFor the month ended October 31, 2015")
        self.heading.grid(row=0, column=0, pady=10)
        
        self.table_heading = ttk.Treeview(self.root, height=0, show="headings")
        self.table_heading["columns"] = ("Account Code", "Account", "Trial Balance", "Adjusting Entries", "Adjusted Trial Balance", "Income Statement", "Balance Sheet")
        self.table_heading_widths = (75, 300, 200, 200, 200, 200, 200)
        for i, column in enumerate(self.table_heading["columns"]):
            self.table_heading.heading(column, text=column)
            self.table_heading.column(column, width=self.table_heading_widths[i], stretch=False)
        self.table_heading.grid(row=1, column=0, sticky="nw", pady=(10,0), padx=10)
        
        self.table = ttk.Treeview(self.root, show="headings")
        self.table["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
        self.table_widths = (75, 300, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
        for i, column in enumerate(self.table["columns"]):
            if i < 2:
                self.table.heading(column, text="")
            elif i%2==0:
                self.table.heading(column, text="Credit")
            else:
                self.table.heading(column, text="Debit")
            self.table.column(column, width=self.table_widths[i], stretch=False)
        self.table.grid(row=2, column=0, pady=(0,10), padx=10)
        
        # Display entries
        self.display_entries()

        # Scrollbar
        self.y_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.grid(row=2, column=1, sticky="ns", padx=(0,5), pady=10)
        

    
    def display_entries(self):
        entries = [
            ("110", "Cash", "114,000", "", "", "","114,000", "", "", "", "114,000", ""),
            ("120", "Accounts Receivable", "204,000", "", "", "","204,000", "", "", "", "204,000", ""),
            ("130", "Medical Supplies", "56,000", "", "", "35,000","21,000", "", "", "", "21,000", ""),
            ("140", "Prepaid Insurance", "20,000", "", "", "1,666.67","18,333.33", "", "", "", "18,333.33", ""),
            ("150", "Land", "250,000", "", "", "","250,000", "", "", "", "250,000", ""),
            ("160", "Medical Building", "1,000,000", "", "", "","1,000,000", "", "", "", "1,000,000", ""),
            ("165", "Accumulated Depreciation - Medical Building", "", "", "", "5,000","", "5,000", "", "", "", "5,000"),
            ("170", "Medical Equipment", "465,000", "", "", "","465,000", "", "", "", "465,000", ""),
            ("175", "Accumulated Depreciation - Medical Equipment", "", "", "", "9,000","", "9,000", "", "", "", "9,000"),
            ("210", "24% Notes Payable", "", "400,000", "", "","", "400,000", "", "", "", "400,000"),
            ("220", "20% Notes Payable", "", "1,200,000", "", "","", "1,200,000", "", "", "", "1,200,000"),
            ("230", "Accounts Payable", "", "49,000", "", "","", "49,000", "", "", "", "49,000"),
            ("240", "Salaries Payable", "", "", "", "51,000","", "51,000", "", "", "", "51,000"),
            ("250", "Interest Payable", "", "", "", "28,000","", "28,000", "", "", "", "28,000"),
            ("260", "Unearned Research Revenue", "", "90,000", "30,000", "","", "60,000", "", "", "", "60,000"),
            ("310", "Marasigan, Capital", "", "250,000", "", "","", "250,000", "", "", "", "250,000"),
            ("320", "Marasigan, Withdrawals", "200,000", "", "", "","250,000", "", "", "", "200,000", ""),
            ("330", "Income Summary", "", "", "", "","", "", "", "", "", ""),
            ("410", "Medical Revenues", "", "434,000", "", "","", "434,000", "", "434,000", "", ""),
            ("420", "Research Revenues", "", "", "", "30,000","", "30,000", "", "30,000", "", ""),
            ("510", "Salaries Expense", "73,000", "", "51,000", "","124,000", "", "124,000", "", "", ""),
            ("520", "Insurance Expense", "", "", "1,666.67", "","1,666.67", "", "1,666.67", "", "", ""),
            ("530", "Repairs Expense", "23,000", "", "", "","23,000", "", "23,000", "", "", ""),
            ("540", "Supplies Expense", "", "", "35,000", "","35,000", "", "35,000", "", "", ""),
            ("550", "Association Dues Expense", "15,000", "", "", "","15,000", "", "15,000", "", "", ""),
            ("560", "Telephone Expense", "3,000", "", "", "","3,000", "", "3,000", "", "", ""),
            ("570", "Depreciation Expense - Building", "", "", "5,000", "","5,000", "", "", "", "", ""),
            ("580", "Depreciation Expense - Equipment", "", "", "9,000", "","9,000", "", "", "", "", ""),
            ("590", "Interest Expense", "", "", "28,000", "","28,000", "", "28,000", "", "", ""),
            ("", "TOTAL", "2,423,000.00 Php", "2,423,000.00 Php", "159,666.67 Php", "159,666.67 Php","2,516,000.00 Php", "2,516,000.00 Php", "243,667.00 Php", "464,000.00 Php", "2,272,333.33 Php", "2,052,000.00 Php"),
            ("", "Net Income", "", "" ,"", "", "", "", "220,333.33 Php", "", "" ,"220,333.33 Php"),
            ("", "Totals", "", "", "", "", "", "", "464,000.00 Php", "464,000.00 Php", "2,272,333.33 Php", "2,272,333.33 Php")
        ]
        
        for entry in entries:
            self.table.insert("", tk.END, values=entry)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Worksheet(root)
    root.mainloop()