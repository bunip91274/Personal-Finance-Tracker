# Personal Finance Tracker

A simple Python desktop app that tracks expenses, stores them in a CSV file, and visualizes spending as a pie chart using matplotlib.

---

## Features

- Add transactions with amount, category, and type (income/expense)
- Stores data in `budget.csv`
- View expenses with a pie chart labeled by category
- Pie chart shows actual dollar amounts
- Clear all data with a one-click button (includes confirmation)
- Input validation to prevent blank fields or invalid values
- Supports file import of standard CSV files (not UTF-8), due to BOM's messing up the program

---

## Visuals

![Screenshot](Screenshot%202025-07-15%20223652.png)

*The interface is built with Tkinter.*

![Screenshot](Screenshot%202025-07-04%20174812.png)

*Data is visualized using matplotlib*

---

## How It Works

1. Enter a numeric amount (e.g. `25.99`) and a category (e.g. `Food`)
2. Click **Add Transaction** to log the entry
3. Click **View Graph** to see a pie chart of your expense breakdown
4. Click **Clear Data** to reset all entries (with confirmation)
5. Click **Import CSV** to import your own CSV file. You can then add to it with the UI or view the graph if data is already present.
   **Data should be formatted in the following format for each row: amount,name of expense**

---

## Requirements

- Python 3.x
- `matplotlib`

To install matplotlib:

```bash
pip install matplotlib
