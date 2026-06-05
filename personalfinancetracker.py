'''
Personal finance tracker that uses .csv files

Maksym Pronin, June 30 - July 4, 2025
'''

import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
import csv
import os
import shutil

# Name of the file all transactions are stored in
BUDGET_FILE = "budget.csv"

# Function to write a new transaction to the CSV file
def writetofile():
    amount = amountentry.get().strip()
    category = categoryentry.get().strip()

    # Shows error if not all input fields are filled
    if not amount or not category:
        messagebox.showerror("Input Error", "All fields must be filled.")
        return

    # Verify if amount field is a number
    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return

    # Open the file in append mode and write the entry
    with open(BUDGET_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])

    # Clear input fields after submission
    amountentry.delete(0, tk.END)
    categoryentry.delete(0, tk.END)

# Function to generate a pie chart of expenses
def piechart():
    amount = []  # List of expense amounts
    name = []    # Corresponding category names

    # Open and read data from CSV file. utf-8-sig strips any BOM that
    # Excel adds when saving as "UTF-8 CSV", which would otherwise break
    # float conversion (e.g. 'ï»¿1000').
    if not os.path.exists(BUDGET_FILE):
        messagebox.showinfo("No Data", "No expenses to display.")
        return

    with open(BUDGET_FILE, "r", encoding="utf-8-sig", newline='') as file:
        csvreader = csv.reader(file)
        for line in csvreader:
            # Skip blank lines and malformed rows instead of crashing
            if len(line) < 2:
                continue
            try:
                amount.append(float(line[0]))  # Convert amount to float for plotting
            except ValueError:
                continue
            name.append(line[1])               # Use category as label

    # If the csv file is empty and there's no data to display
    if not amount:
        messagebox.showinfo("No Data", "No expenses to display.")
        return

    # Format pie chart slices as dollar values
    def dollars(pct):
        total = sum(amount)
        value = total * pct / 100
        return "$" + str(round(value, 2))

    # Create and display the pie chart
    plt.pie(amount, labels=name, autopct=dollars)
    plt.title("Expenses Breakdown")
    plt.show()

# Function to clear all data in the CSV file
def clearcsv():
    # Ask for confirmation before erasing everything
    if not messagebox.askyesno("Clear Data", "Are you sure you want to delete all data?"):
        return

    # Opening in write mode and closing immediately erases the contents
    with open(BUDGET_FILE, "w", newline=''):
        pass

# Function to import an existing CSV file, replacing the current data
def importcsv():
    path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
    )

    # User cancelled the dialog
    if not path:
        return

    # Validate the file can be read as "amount,category" rows before
    # replacing the current budget, and normalize away any BOM.
    rows = []
    try:
        with open(path, "r", encoding="utf-8-sig", newline='') as file:
            for line in csv.reader(file):
                if len(line) < 2:
                    continue
                float(line[0])  # Raises ValueError on bad data
                rows.append([line[0].strip(), line[1].strip()])
    except (ValueError, IndexError):
        messagebox.showerror(
            "Import Error",
            "File must contain rows formatted as: amount,category",
        )
        return
    except OSError:
        messagebox.showerror("Import Error", "Could not read the selected file.")
        return

    # Write the cleaned rows out as the new budget file
    with open(BUDGET_FILE, "w", newline='') as file:
        csv.writer(file).writerows(rows)

    messagebox.showinfo("Import Complete", f"Imported {len(rows)} transaction(s).")

# Initialize main application window
window = tk.Tk()
window.geometry("600x400")
window.title("Personal Finance Tracker")

# Labels and entry fields for transaction input
tk.Label(window, text="Amount:").pack()
amountentry = tk.Entry(window)
amountentry.pack()

tk.Label(window, text="Category:").pack()
categoryentry = tk.Entry(window)
categoryentry.pack()

# Buttons for submitting data, viewing chart, clearing and importing CSV
tk.Button(window, text="Add Transaction", command=writetofile).pack(pady=10)
tk.Button(window, text="View Graph", command=piechart).pack()
tk.Button(window, text="Clear Data", command=clearcsv).pack(pady=10)
tk.Button(window, text="Import CSV", command=importcsv).pack()

# Run the application
window.mainloop()
