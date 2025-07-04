# Personal Finance Tracker

A simple Python desktop app that tracks income and expenses, stores them in a CSV file, and visualizes spending as a pie chart using matplotlib.

---

## Features

- Add transactions with amount, category, and type (income/expense)
- Stores data in `budget.csv`
- View expenses with a pie chart labeled by category
- Pie chart shows actual dollar amounts
- Clear all data with a one-click button (includes confirmation)
- Input validation to prevent blank fields or invalid values

---

## Visuals

![Screenshot](Screenshot%202025-07-04%20183914.png)

*The interface is built with Tkinter.*

![Screenshot](Screenshot%202025-07-04%20174812.png)

*Data is visualized using matplotlib*

---

## How It Works

1. Enter a numeric amount (e.g. `25.99`) and a category (e.g. `Food`)
2. Click **Add Transaction** to log the entry
3. Click **View Graph** to see a pie chart of your expense breakdown
4. Click **Clear Data** to reset all entries (with confirmation)

---

## Requirements

- Python 3.x
- `matplotlib`

To install matplotlib:

```bash
pip install matplotlib
