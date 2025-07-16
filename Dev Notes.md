# Dev Notes
## July 15th
Feature added: CSV file import

While finalizing the first version of the app, I added a feature that lets the user import a .csv file and replace the current data (budget.csv). This was part of a full Tkinter guide I was watching, and I wanted the app to feel more flexible and usable beyond manual input.

Before publishing, I decided to remove the type field entirely. Originally, I had users specify whether a transaction was an income or an expense, but I realized the app only focused on visualizing expenses anyway, so the field added complexity without value. Removing it simplified both the UI and file format.

The import feature itself took a bit of time to figure out. Some of the errors I hit:

Encoding issues from Excel, especially when files were saved as UTF-8 with BOM. This caused float conversion to fail (ValueError: could not convert string to float: 'ï»¿1000'). Solved this by either stripping the BOM in code or saving as standard CSV (Comma-delimited).

Blank lines and incomplete rows — I added validation to skip these safely when reading the file.

Overall, importing now works cleanly, and the app handles real-world CSV quirks a lot better than when I first started.
