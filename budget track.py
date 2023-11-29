import tkinter as tk
from tkinter import messagebox
import datetime

class Expense:
    def __init__(self, amount, description, category):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

class BudgetBuddyGUI:
    def __init__(self, root):
        self.expenses = []

        # Set up the main window with a yellow pastel background
        self.root = root
        self.root.title("BudgetBuddy")
        self.root.geometry("400x300")
        self.root.configure(bg="#FFF3A3")  # Yellow pastel background

        # Create GUI elements with pastel colors
        pastel_blue = "#AED9E0"
        pastel_green = "#B4D3B2"
        pastel_pink = "#F1C3D1"

        self.amount_label = tk.Label(root, text="Amount:", bg=pastel_blue)
        self.amount_entry = tk.Entry(root)
        self.description_label = tk.Label(root, text="Description:", bg=pastel_green)
        self.description_entry = tk.Entry(root)
        self.category_label = tk.Label(root, text="Category:", bg=pastel_pink)
        self.category_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense, bg=pastel_blue)
        self.view_button = tk.Button(root, text="View Expenses", command=self.view_expenses, bg=pastel_green)
        self.analyze_button = tk.Button(root, text="Analyze Expenses", command=self.analyze_expenses, bg=pastel_pink)

        # Layout GUI elements
        self.amount_label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.amount_entry.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.description_label.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.description_entry.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.category_label.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        self.category_entry.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")
        self.view_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")
        self.analyze_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

        # Configure column and row weights for resizing
        for i in range(6):
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i, weight=1)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()
            category = self.category_entry.get()

            new_expense = Expense(amount, description, category)
            self.expenses.append(new_expense)
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")

    def view_expenses(self):
        if not self.expenses:
            messagebox.showinfo("Info", "No expenses to display.")
        else:
            expenses_text = ""
            for expense in self.expenses:
                expenses_text += f"Date: {expense.date} | Category: {expense.category} | Amount: ${expense.amount} | Description: {expense.description}\n"

            # Create a pop-up window with pastel_green background
            popup = tk.Toplevel(self.root)
            popup.title("View Expenses")
            popup.configure(bg="#B4D3B2")  # pastel_green background
            self.center_window(popup)

            # Add widgets to the pop-up window
            label = tk.Label(popup, text=expenses_text, bg="#B4D3B2", justify="left")  # pastel_green background
            label.pack(padx=20, pady=10)
            ok_button = tk.Button(popup, text="OK", command=popup.destroy, bg="#B4D3B2")  # pastel_green background
            ok_button.pack(pady=10)

    def analyze_expenses(self):
        if not self.expenses:
            messagebox.showinfo("Info", "No expenses to analyze.")
        else:
            total_expenses = sum([expense.amount for expense in self.expenses])

            # Create a pop-up window with pastel_pink background
            popup = tk.Toplevel(self.root)
            popup.title("Expense Analysis")
            popup.configure(bg="#F1C3D1")  # pastel_pink background
            self.center_window(popup)

            # Add widgets to the pop-up window
            label = tk.Label(popup, text=f"Total Expenses: ${total_expenses}", bg="#F1C3D1")  # pastel_pink background
            label.pack(padx=20, pady=10)
            ok_button = tk.Button(popup, text="OK", command=popup.destroy, bg="#F1C3D1")  # pastel_pink background
            ok_button.pack(pady=10)

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


# Create and run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#FFF3A3")  # Set the yellow pastel background color for the main window
    budget_buddy_gui = BudgetBuddyGUI(root)
    budget_buddy_gui.center_window(root)  # Center the main window
    root.mainloop()
