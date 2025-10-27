# OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

This is a Python program to manage seating arrangements in an open space with multiple tables. It allows assigning people to seats, checking availability, organizing randomly, displaying, and storing seating plans.
![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)
---

## 🧱 Project Structure
```
challenge-openspace-classifier/
│
├── README.md
├── main.py
├── dev_notebook.ipynb
│
└── utils/
    ├── file_utils.py
    ├── table.py
    └── openspace.py
```

---

## ⚙️ How It Works
1. The user provides a list of team members.
2. The program randomly assigns them to seats across several tables with four ocuupants in each table(default is 6).
3. The result is displayed and stored in a text file (`Seating_plan.txt`).

---

## ▶️ Run Instructions
Run from your terminal:

```bash
python main.py
```

Or open `dev_notebook.ipynb` in JupyterLab to test interactively.

---

## 🧠 Example Output
```
Table 1: Frédéric, Amine, Sandrine, Pierrick
Table 2: Kristin, Michiel, Intan K., Anna
Table 3: Aleksei, Imran, Welederufeal, Ena
...
✅ Seating arrangement saved to 'Seating_plan.txt'
```

---

## 🧑‍💻 Technologies Used
- Python 3
- Object-Oriented Programming
- Jupyter Notebook
- GitHub

---

## ✨ Author
Developed as part of the **BeCode Data & AI Bootcamp** challenge.

Connect with me on [LinkedIn]().

