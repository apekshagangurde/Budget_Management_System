import tkinter as tk

from tkinter import messagebox

import csv

class Expense:

    def __init__(self, date, description, amount):

        self.date = date

        self.description = description

        self.amount = amount

def add_salary():

    try:

        global balance

        salary = float(salary_entry.get())

        balance += salary

        balance_label.configure(text="Balance: $" + str(balance))

        messagebox.showinfo("Information", "Salary added successfully.")

        display_remaining_balance()  # Call the function to show the remaining balance

    except ValueError:

        messagebox.showerror("Error", "Invalid input. Please enter a valid salary.")

def add_expense():

    expense_window = tk.Toplevel(window)

    expense_window.title("Add Expense")

    date_label = tk.Label(expense_window, text="Date (DD/MM/YYYY):", fg="blue")

    date_label.grid(row=0, column=0, padx=10, pady=10)

    date_entry = tk.Entry(expense_window)

    date_entry.grid(row=0, column=1, padx=10, pady=10)

    description_label = tk.Label(expense_window, text="Description:", fg="blue")

    description_label.grid(row=1, column=0, padx=10, pady=10)

    description_entry = tk.Entry(expense_window)

    description_entry.grid(row=1, column=1, padx=10, pady=10)

    amount_label = tk.Label(expense_window, text="Amount:", fg="blue")

    amount_label.grid(row=2, column=0, padx=10, pady=10)

    amount_entry = tk.Entry(expense_window)

    amount_entry.grid(row=2, column=1, padx=10, pady=10)

    confirm_button = tk.Button(expense_window, text="Confirm", bg="green", fg="white", command=lambda: confirm_expense(expense_window, date_entry.get(), description_entry.get(), amount_entry.get()))

    confirm_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def confirm_expense(expense_window, date, description, amount):

    try:

        expense_amount = float(amount)

        global balance

        balance -= expense_amount

        expense = Expense(date, description, expense_amount)

        expenses.append(expense)

        messagebox.showinfo("Information", "Expense added successfully.")

        expense_window.destroy()

        display_expenses()

        display_remaining_balance()  # Call the function to show the remaining balance

    except ValueError:

        messagebox.showerror("Error", "Invalid input. Please enter a valid expense amount.")

def show_expense_list():

    expense_list_window = tk.Toplevel(window)

    expense_list_window.title("Expense List")

    expenses_text = tk.Text(expense_list_window, height=10, width=50)

    expenses_text.pack(padx=10, pady=10)

    expenses_text.insert(tk.END, "Expense List:\n")

    expenses_text.insert(tk.END, "-----------------------------------------------------\n")

    expenses_text.insert(tk.END, "Date         | Description       | Amount ($)\n")

    expenses_text.insert(tk.END, "-----------------------------------------------------\n")

    for expense in expenses:

        expenses_text.insert(tk.END, f"{expense.date} | {expense.description} | {expense.amount}\n")

        expenses_text.insert(tk.END, "-----------------------------------------------------\n")

def save_to_file():

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Date", "Description", "Amount"])

        for expense in expenses:

            writer.writerow([expense.date, expense.description, expense.amount])

    messagebox.showinfo("Information", "Expenses saved to file.")

def show_file():

    try:

        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            content = "\n".join([" | ".join(row) for row in reader])

        messagebox.showinfo("Expense File", content)

    except FileNotFoundError:

        messagebox.showerror("Error", "Expense file not found.")

def update_expense():

    update_window = tk.Toplevel(window)

    update_window.title("Update Expense")

    index_label = tk.Label(update_window, text="Expense Index:", fg="blue")

    index_label.grid(row=0, column=0, padx=10, pady=10)

    index_entry = tk.Entry(update_window)

    index_entry.grid(row=0, column=1, padx=10, pady=10)

    date_label = tk.Label(update_window, text="New Date (DD/MM/YYYY):", fg="blue")

    date_label.grid(row=1, column=0, padx=10, pady=10)

    date_entry = tk.Entry(update_window)

    date_entry.grid(row=1, column=1, padx=10, pady=10)

    description_label = tk.Label(update_window, text="New Description:", fg="blue")

    description_label.grid(row=2, column=0, padx=10, pady=10)

    description_entry = tk.Entry(update_window)

    description_entry.grid(row=2, column=1, padx=10, pady=10)

    amount_label = tk.Label(update_window, text="New Amount:", fg="blue")

    amount_label.grid(row=3, column=0, padx=10, pady=10)

    amount_entry = tk.Entry(update_window)

    amount_entry.grid(row=3, column=1, padx=10, pady=10)

    confirm_button = tk.Button(update_window, text="Confirm", bg="green", fg="white", command=lambda: confirm_update(update_window, index_entry.get(), date_entry.get(), description_entry.get(), amount_entry.get()))

    confirm_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def confirm_update(update_window, index, date, description, amount):

    try:

        expense_index = int(index)

        expense_amount = float(amount)

        if expense_index >= 0 and expense_index < len(expenses):

            expenses[expense_index].date = date

            expenses[expense_index].description = description

            expenses[expense_index].amount = expense_amount

            messagebox.showinfo("Information", "Expense updated successfully.")

            update_window.destroy()

            show_expense_list()

            save_to_file()

            display_remaining_balance()  # Call the function to show the remaining balance

        else:

            messagebox.showerror("Error", "Invalid expense index.")

    except ValueError:

        messagebox.showerror("Error", "Invalid input. Please enter a valid expense index and amount.")

def exit_program():

    window.destroy()

def display_remaining_balance():

    messagebox.showinfo("Remaining Balance", "Your remaining balance is: $" + str(balance))

# Create the main window

window = tk.Tk()

window.title("Budget Management System")

# Add the heading

heading_label = tk.Label(window, text="Budget Management System", fg="purple", font=("Arial", 16, "bold"))

heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Add the tagline

tagline_label = tk.Label(window, text="Track, Manage, and Optimize Your Finances", fg="blue", font=("Arial", 12, "italic"))

tagline_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Add the balance label

balance = 0

balance_label = tk.Label(window, text="Balance: $" + str(balance), fg="green", font=("Arial", 14, "bold"))

balance_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Add the salary entry and button

salary_label = tk.Label(window, text="Enter Salary Amount:", fg="blue")

salary_label.grid(row=3, column=0, padx=10, pady=10)

salary_entry = tk.Entry(window)

salary_entry.grid(row=3, column=1, padx=10, pady=10)

add_salary_button = tk.Button(window, text="Add Salary", bg="green", fg="white", command=add_salary)

add_salary_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Add the expense buttons

add_expense_button = tk.Button(window, text="Add Expense", bg="orange", fg="white", command=add_expense)

add_expense_button.grid(row=5, column=0, padx=10, pady=10)

show_expense_list_button = tk.Button(window, text="Show Expense List", bg="orange", fg="white", command=show_expense_list)

show_expense_list_button.grid(row=5, column=1, padx=10, pady=10)

# Add the file-related buttons

save_to_file_button = tk.Button(window, text="Save to File", bg="purple", fg="white", command=save_to_file)

save_to_file_button.grid(row=6, column=0, padx=10, pady=10)

show_file_button = tk.Button(window, text="Show File", bg="purple", fg="white", command=show_file)

show_file_button.grid(row=6, column=1, padx=10, pady=10)

# Add the update and exit buttons

update_expense_button = tk.Button(window, text="Update Expense", bg="red", fg="white", command=update_expense)

update_expense_button.grid(row=7, column=0, padx=10, pady=10)

exit_button = tk.Button(window, text="Exit", bg="red", fg="white", command=exit_program)

exit_button.grid(row=7, column=1, padx=10, pady=10)

# Initialize the list to store expenses

expenses = []

# Start the GUI event loop

window.mainloop()
