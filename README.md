# PLP Python Week 7 — Lists

This repository contains my Week 7 Python lists assignment.

- `list_warmup.py` demonstrates list indexes, `.append()`, `.remove()`, and `len()`.
- `shopping_list.py` provides a safe interactive shopping-list menu with add, remove, show, and done commands.
- `list_report.py` numbers a list, counts names longer than four letters, and finds the longest item by loop comparison.
- `screenshots/` contains screenshots of each program running.

Checking whether an item is in a list before calling `.remove()` is safer because `.remove()` raises a `ValueError` when the item is missing. Using `if item in shopping_list` prevents the program from crashing and lets it show a helpful message instead.
