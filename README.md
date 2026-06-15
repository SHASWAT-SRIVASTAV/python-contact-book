<div align="center">

# Python Contact Book

### A menu-driven contact manager built to understand how software is structured.

<br>

![Python](https://img.shields.io/badge/Python-3.x-c9184a?style=for-the-badge&logo=python&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Modular-800f2f?style=for-the-badge)
![Storage](https://img.shields.io/badge/Storage-In--Memory-ff4d6d?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-CLI-590d22?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-v1.0%20Complete-c9184a?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-800f2f?style=for-the-badge)

</div>

---

## About

**Python Contact Book** is a command-line application for managing contacts — add, search, delete, and view entries through a clean menu-driven interface.

This is the second project in my Python portfolio, built after completing a basic calculator. The goal was not feature density. The goal was to understand how a real program is structured: how functions are separated by responsibility, how a central data store is passed between operations, and how a program loop drives interaction.

Every design decision here was made in service of that learning objective.

---

## Features

| Feature | Description |
|---|---|
| Add Contact | Store a name and phone number as a new entry |
| Delete Contact | Remove an existing contact by name |
| Search Contact | Look up a contact by name and display their details |
| View All Contacts | List every contact currently in the book |
| Clear Contact Book | Wipe all contacts in a single operation |
| Duplicate Detection | Prevents overwriting an existing contact silently |
| Menu Interface | Loop-driven numbered menu for all operations |

---

## Project Structure

```
python-contact-book/
│
├── contact_book.py       # Main application — all logic and entry point
├── README.md             # Project documentation
├── LICENSE               # MIT License
└── screenshots/          # CLI output screenshots
```

This project intentionally lives in a single file. At this stage, the priority was learning function separation within one module before introducing multi-file architecture.

---

## Software Architecture

The program follows a straightforward linear flow. Each menu selection maps to exactly one function, and every function returns control to the menu loop on completion.

```
Program Starts
      ↓
   main()
      ↓
Display Menu
      ↓
 User Input
      ↓
 ┌────┴────────────────────────────────────┐
 │                                         │
[1] add_contact()      [2] delete_contact()
[3] search_contact()   [4] view_all()
[5] clear_book()       [6] Exit
 │                                         │
 └────┬────────────────────────────────────┘
      ↓
 Operation Executes
      ↓
 Return to Menu
      ↓
  [6] Exit → Program Ends
```

**Key design principle:** no function handles more than one responsibility. `add_contact()` only adds. `search_contact()` only searches. The menu loop only routes.

---

## Dictionary Usage

The contact book is backed by a single Python dictionary:

```python
contact_book = {}
# Structure: { "Name": "Phone Number" }
```

This was a deliberate choice for learning. Dictionaries offer:

- **O(1) average-case lookup** — searching by name is direct, not iterative
- **Natural key-value semantics** — name maps to number without boilerplate
- **Built-in membership testing** — `if name in contact_book` handles duplicate detection cleanly

The limitation — contacts are lost when the program exits — is acknowledged and addressed in Version 2.

---

## Learning Outcomes

This project was built to develop a concrete understanding of the following:

- **Functions with single responsibility** — each operation is isolated and independently testable
- **Dictionary operations** — insertion, deletion, lookup, and iteration across a live data structure
- **Program flow control** — using a `while` loop to sustain a menu session until the user exits
- **Input handling** — collecting, stripping, and validating user input inside CLI workflows
- **Modular thinking** — structuring code so that each function could be extracted or replaced without breaking others
- **Duplicate detection** — checking for key existence before writing, rather than silently overwriting

---

## Future Scope

### Version 2 — Persistence
- JSON-based file storage so contacts survive between sessions
- File read/write operations on program start and exit
- Improved input validation (empty fields, numeric-only phone numbers)
- Cleaner error messages and edge case handling

### Version 3 — Extended Features
- Desktop GUI using Tkinter or Flet
- Search by phone number in addition to name
- Email and address fields per contact
- Contact categories (personal, work, family)
- Export contacts to CSV

---

## How to Run

**Requirements:** Python 3.x — no external libraries required.

```bash
# Clone the repository
git clone https://github.com/shashwat/python-contact-book.git

# Navigate into the project directory
cd python-contact-book

# Run the application
python contact_book.py
```

---

## Sample Menu Output

```
=============================
       CONTACT BOOK
=============================
 1. Add Contact
 2. Delete Contact
 3. Search Contact
 4. View All Contacts
 5. Clear Contact Book
 6. Exit
=============================
Enter your choice: _
```

```
Enter name: Shaswat
Enter phone number: 9876543210
✔ Contact added successfully.

Enter name: Shaswat
✖ Contact already exists.
```

---

## Technologies Used

| Technology | Role |
|---|---|
| Python 3.x | Core language |
| Dictionary | Primary data structure |
| Functions | Modular operation handlers |
| CLI (stdin/stdout) | User interface layer |
| Git | Version control |
| GitHub | Remote hosting and portfolio |

---

## Version

| Version | Status | Description |
|---|---|---|
| v1.0 | ✅ Complete | In-memory CLI contact manager |
| v2.0 | 🔲 Planned | JSON persistence and file handling |
| v3.0 | 🔲 Planned | GUI and extended contact fields |

---

## Author

**Shashwat**
B.Tech — AI & ML · Noida Institute of Engineering and Technology

[![GitHub](https://img.shields.io/badge/GitHub-@shashwat-590d22?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shashwat)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-c9184a?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

*Part of the [Python Portfolio](https://github.com/SHASWAT-SRIVASTAV/Python) — a record of real projects built while learning.*

</div>
