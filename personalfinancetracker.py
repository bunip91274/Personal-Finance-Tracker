'''
Personal finance tracker that uses .csv files

Maksym Pronin, June 30 - July 4, 2025
'''

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv

# Function to write a new transaction to the CSV file
def writetofile():
    amount = amountentry.get()
    category = categoryentry.get()

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
    file = open("budget.csv", "a", newline='')
    writer = csv.writer(file)
    writer.writerow([amount, category, type])

    # Clear input fields after submission
    amountentry.delete(0, tk.END)
    categoryentry.delete(0, tk.END)

# Function to generate a pie chart of expenses
def piechart():
    amount = []  # List of expense amounts
    name = []    # Corresponding category names

    # Open and read data from CSV file
    file = open("budget.csv", "r")
    csvreader = csv.reader(file)
    for line in csvreader:
        amount.append(float(line[0]))  # Convert amount to float for plotting
        name.append(line[1])           # Use category as label

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
    file = open("budget.csv", "w")  # Opens file in write mode, erasing contents
    pass  # No content written = file is now empty

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

# Buttons for submitting data, viewing chart, and clearing CSV
tk.Button(window, text="Add Transaction", command=writetofile).pack(pady=10)
tk.Button(window, text="View Graph", command=piechart).pack()
tk.Button(window, text="Clear Data", command=clearcsv).pack(pady=10)

# Run the application
window.mainloop()
