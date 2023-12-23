import tkinter as tk
from tkinter import ttk

# prolem: heading_label must be smaller!
class PostingToLedger:
    def __init__(self, root):
        self.root = root
        self.root.title("Dr. Nick Marasigan, Posting to the Ledger")

        self.heading_label = tk.Label(self.root, text="Dr. Nick Marasigan, M.D.\nPosting to the Ledger", font=("Helvetica 9 bold"))
        self.heading_label.grid(row=0, column=0, pady=(5,0), padx=5)
    
        self.main_frame = tk.Frame(self.root, borderwidth=1, relief="sunken")
        self.main_frame.grid(row=1, column=0, padx=5, pady=(5, 10), sticky="nsew")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
    
        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.grid(row=1, column=0)
       
        self.y_scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.y_scrollbar.grid(row=1, column=1, sticky="ns")   
        
        self.canvas.configure(yscrollcommand=self.y_scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.config( scrollregion=self.canvas.bbox(tk.ALL)))    
        
        self.second_frame = tk.Frame(self.canvas)
        self.canvas.create_window( (0,0), window=self.second_frame, anchor="nw")

        # Column heading for all
        heading = ("Debit", "Credit")
        
        # Cash
        cash_data = [
            ("250,000", "50,000"),
            ("117,000", "59,000"),
            ("90,000", "20,000"),
            ("113,000", "73,000"),
            ("","23,000"),
            ("","3,000"),
            ("","13,000"),
            ("","200,000"),
            ("","15,000"),
            ("",""),
            ("570,000","456,000"),
            ("+114,000 php","")
        ]
        
        # accounts receivable
        accrec_data = [
            ("317,000", "113,000"),
            ("204,000", ""),
        ]
        
        # medical supples
        medsupp_data = [
            ("39,000", ""),
            ("17,000", ""),
            ("56,000", "")
        ]
        
        # land
        land_data = [
            ("250,000", ""),
            ("250,000", ""),
        ]
        
        # medical building
        medbuild_data = [
            ("1,000,000", ""),
            ("1,000,000", "")
        ]
        
        # medical equipment
        medequip_data = [
            ("420,000", ""),
            ("45,000", ""),
            ("465,000", ""),
        ]
        
        # 24% notes payable
        notepay24_data = [
            ("", "400,000"),
            ("", "400,000")
        ]
        
        # 20% notes payable
        notepay20_data = [
            ("", "1,200,000"),
            ("", "1,200,000")
        ]
        
        # accounts payable
        accpay_data = [
            ("13,000", "17,000"),
            ("", "45,000"),
            ("", ""),
            ("13,000", "62,000"),
            ("", "-49,000 Php")
        ]
        
        # unearned research revenues
        ueresrev_data = [
            ("", "90,000"),
            ("", "90,000")
        ]
        
        # marasigan, capital
        capital_data = [
            ("", "250,000"),
            ("", "250,000")
        ]
        
        # marasigan, withrawal
        withdraw_data = [
            ("200,000", ""),
            ("200,000", "")
        ]
        
        # medical revenues
        medicrev_data = [
            ("", "117,000"),
            ("", "317,000"),
            ("", "434,000")
        ]
        
        # salaries expense
        salexp_data = [
            ("73,000", ""),
            ("73,000", "")
        ]
        
        # insurance expense
        insuexp_data = [
            ("20,000", ""),
            ("20,000", "")    
        ]
        
        # repairs expense
        repexp_data = [
            ("23,000", ""),
            ("23,000", "")
        ]
        
        # association dues expense
        assduesexp_data = [
            ("15,000", ""),
            ("15,000", "")
        ]
        
        # telephone expense
        telexp_data = [
            ("3,000", ""),
            ("3,000", "")
        ]
        
        acctg_titles = [
            cash_data, accrec_data, medsupp_data, land_data, medbuild_data, medequip_data, notepay24_data, notepay20_data,
            accpay_data, ueresrev_data, capital_data, withdraw_data, medicrev_data,
            salexp_data, insuexp_data, repexp_data, assduesexp_data, telexp_data
        ]
        
        acctg_titles_title = [
            "Cash", "Accounts Receivable", "Medical Supply", "Land", "Medical Building", "Medical Equipment", "24% Notes Payable", "20% Notes Payable", "Accounts Payable",
            "Unearned Research Revenues", "Marasigan, Capital", "Marasigan, Withdrawals", "Medical Revenues",
            "Salaries Expense", "Insurance Expense", "Repairs Expense", "Association Dues Expense",
            "Telephone Expense"
        ]
        
        for i in range( len(acctg_titles)):
            self.create_table(self.second_frame, 2, 125, acctg_titles[i], heading, acctg_titles_title[i])
        
        # Make the window not resizable
        self.root.resizable(width=False, height=False)

    
    def create_table(self, parent, columns, column_width, rowcolumn_data, header_data, title):
        if columns < len(header_data):
            raise ValueError("Invalid parameters for rows or columns. Rows or columns must match the length of rowcolumn_data or header_data")

        # Create a frame to hold the table and title label with a border
        frame = ttk.Frame(parent)
        frame.grid(pady=10, padx=10)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Create a title label
        title_label = ttk.Label(frame, text=title, font=("Helvetica", 10, "bold"))
        title_label.grid(row=0, column=0, padx=7, pady=(5, 0))

        # Create a treeview for the table
        self.table = ttk.Treeview(frame, show="headings")
        self.table["columns"] = header_data
        self.table.grid(row=1, column=0, sticky="nsew")

        for i in range(columns):
            self.table.heading(i, text=header_data[i]) 
            self.table.column(i, width=column_width)

        for row_data in rowcolumn_data:
            self.table.insert("", tk.END, values=row_data)

        # Create a vertical scrollbar
        y_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.table.yview)
        y_scrollbar.grid(row=1, column=1, sticky="ns")

        # Configure the treeview to use the scrollbar
        self.table.configure(yscrollcommand=y_scrollbar.set)

        
        
# fawk this
if __name__ == "__main__":
    root = tk.Tk()
    app = PostingToLedger(root)
    root.mainloop()
