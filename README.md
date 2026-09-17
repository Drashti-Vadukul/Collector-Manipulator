

## 👩‍💻 Author

### Drashti Vadukul

**BCA Student | AI, ML & Data Science Learner | Web Development Enthusiast**

📌 **Skills & Interests**
- 🐍 Python
- 📊 Data Analytics
- 🤖 AI & Machine Learning
- 🌐 HTML & CSS
- 💻 Git & GitHub

📚 Currently learning **AI, ML & Data Science** and building practical projects to strengthen my programming and problem-solving skills.

# 🎓 Student Data Organizer

> A Python-based console application designed to manage student records using fundamental Python programming concepts and basic CRUD operations.

---

## 📌 Project Overview

**Student Data Organizer** is a menu-driven console application developed using Python.

The main purpose of this project is to create a simple system where student information can be added, displayed, updated, and deleted through an interactive command-line menu.

The project uses Python's built-in data structures and control-flow concepts such as:

- Lists
- Dictionaries
- `while` loops
- `for` loops
- `if-else` statements
- `match-case`
- User input
- List methods
- Dictionary operations

This project is created as part of my **Python Fundamentals Learning Journey** to understand how basic programming concepts can be combined to create a practical application.

---

# 🎯 Project Objective

The primary objective of this project is to build a simple and user-friendly student record management system using core Python concepts.

The application allows users to:

1. Add new student information
2. View all available student records
3. Search and update student information
4. Delete student records
5. View subjects offered
6. Exit the application

The project also demonstrates how **CRUD operations** can be implemented using Python Lists and Dictionaries.

---

# 💡 Problem Statement

Managing student information manually can become difficult when the number of records increases.

A simple computerized system can make it easier to:

- Store student information
- Find a particular student
- Modify existing information
- Remove unwanted records
- View multiple student records

This project provides a basic console-based solution for these operations without using a database.

---

# ✨ Key Features

## ➕ 1. Add Student

The application allows the user to add a new student.

The following information can be entered:

- Student ID
- Student Name
- Age
- Grade
- Date of Birth
- Subjects

The information is stored inside a Python Dictionary.

Example:

```python
student = {
    "Student ID": 101,
    "Name": "Alice",
    "Age": 20,
    "Grade": "B+",
    "Date of Birth": "2002-05-14",
    "Subjects": "Math, Science, English"
}
```

The dictionary is then added to the main student list.

```python
students.append(student)
```

---

# 👀 2. Display All Students

The application provides an option to display all stored student records.

The program first checks whether the student list contains any records.

```python
if len(students) == 0:
    print("No students found.")
```

If records are available, a `for` loop is used to display each student.

Example:

```text
--- Display All Students ---

Student ID: 101 | Name: Alice | Age: 20 | Grade: B+ | Subjects: Math, Science, English
```

---

# ✏️ 3. Update Student Information

The update feature allows the user to modify an existing student's information.

The student is searched using the **Student ID**.

```python
if student["Student ID"] == student_id:
```

Once the student is found, the user can update:

- Name
- Age
- Grade
- Date of Birth
- Subjects

Example:

```text
Enter Student ID to update: 101

Student found!

Enter new Name:
Enter new Age:
Enter new Grade:
Enter new Date of Birth:
Enter new Subjects:

Student information updated successfully!
```

---

# 🗑️ 4. Delete Student

The delete feature allows the user to remove a student record.

The program searches for the student using the Student ID.

If the ID is found, the record is removed using:

```python
students.remove(student)
```

Example:

```text
Enter Student ID to delete: 101

Student deleted successfully!
```

If the ID does not exist:

```text
Student not found.
```

---

# 📚 5. Display Subjects Offered

The application also provides a separate option to display the subjects offered.

Currently, the application includes:

```text
Subject Offered:
- Mathematics
- Science
- English
- History
```

---

# 🚪 6. Exit

The user can exit the application by selecting option `6`.

The program uses:

```python
break
```

to stop the main `while` loop.

Output:

```text
Thank You !!
```

---

# 🧠 Python Concepts Used

This project combines several important Python fundamentals.

| Python Concept | How It Is Used |
|---|---|
| `print()` | Display menu and messages |
| `input()` | Take information from the user |
| Variables | Store user-entered values |
| List | Store multiple student records |
| Dictionary | Store individual student information |
| `while` loop | Keep the application running |
| `for` loop | Search and display records |
| `if-else` | Perform condition checking |
| `match-case` | Handle menu options |
| `break` | Exit loop |
| `append()` | Add student record |
| `remove()` | Delete student record |
| `len()` | Check number of students |

---

# 🗂️ Data Structures

Two main Python data structures are used in this project.

## 📋 List

The main student collection is created as:

```python
students = []
```

This list can contain multiple student dictionaries.

For example:

```python
students = [
    {
        "Student ID": 101,
        "Name": "Alice",
        "Age": 20,
        "Grade": "B+",
        "Date of Birth": "2002-05-14",
        "Subjects": "Math, Science, English"
    },
    {
        "Student ID": 102,
        "Name": "Bob",
        "Age": 21,
        "Grade": "A",
        "Date of Birth": "2001-08-20",
        "Subjects": "Science, English"
    }
]
```

---

## 📖 Dictionary

Each student is represented using a dictionary.

```python
student = {
    "Student ID": student_id,
    "Name": name,
    "Age": age,
    "Grade": grade,
    "Date of Birth": dob,
    "Subjects": subjects
}
```

A dictionary is useful because every value is associated with a meaningful key.

For example:

```python
student["Name"]
student["Age"]
student["Grade"]
```

---

# 🔄 CRUD Operations

One of the main concepts demonstrated by this project is **CRUD**.

CRUD stands for:

- **C — Create**
- **R — Read**
- **U — Update**
- **D — Delete**

| CRUD Operation | Project Feature |
|---|---|
| Create | Add Student |
| Read | Display All Students |
| Update | Update Student Information |
| Delete | Delete Student |

These four operations form the foundation of many data management applications.

---

# 🔁 Program Flow

The application follows a continuous menu-driven flow.

```text
Start
  ↓
Welcome Message
  ↓
Display Menu
  ↓
Take User Choice
  ↓
Check Choice
  ↓
 ┌───────────────────────────────┐
 │                               │
 │  1 → Add Student              │
 │  2 → Display Students         │
 │  3 → Update Student           │
 │  4 → Delete Student           │
 │  5 → Display Subjects         │
 │  6 → Exit                     │
 │                               │
 └───────────────────────────────┘
  ↓
Perform Selected Operation
  ↓
Display Menu Again
  ↓
Continue Until User Selects 6
  ↓
Exit
```

---

# 🖥️ Application Menu

When the program starts, the following menu is displayed:

```text
Welcome to the Student Data Organizer

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice:
```

---

# 📸 Sample Execution

## ➕ Adding a Student

```text
Enter your choice: 1

Enter student details:
Student ID: 101
Name: Alice
Age: 20
Grade: B+
Date of Birth (YYYY-MM-DD): 2002-05-14
Subjects (comma-separated): Math, Science, English

Student added successfully!
```

---

## 👀 Displaying Student Records

```text
Enter your choice: 2

--- Display All Students ---

Student ID: 101 | Name: Alice | Age: 20 | Grade: B+ | Subjects: Math, Science, English
```

---

## ✏️ Updating a Student

```text
Enter your choice: 3

Enter Student ID to update: 101

Student found!

Enter new Name: Alice Patel
Enter new Age: 21
Enter new Grade: A
Enter new Date of Birth (YYYY-MM-DD): 2002-05-14
Enter new Subjects (comma-separated): Math, Science, English

Student information updated successfully!
```

---

## 🗑️ Deleting a Student

```text
Enter your choice: 4

Enter Student ID to delete: 101

Student deleted successfully!
```

---

## 📚 Displaying Subjects

```text
Enter your choice: 5

Subject Offered:
- Mathematics
- Science
- English
- History
```

---

# ⚠️ Invalid Choice Handling

If the user enters an option that is not available in the menu, the program handles it using the default `match-case` option.

```python
case _:
    print("Invalid choice!")
```

Example:

```text
Enter your choice: 9

Invalid choice!
```

---

# 🔍 How Searching Works

The application uses the Student ID to find a particular student.

For example:

```python
for student in students:
    if student["Student ID"] == student_id:
```

The program checks each student in the list until it finds a matching Student ID.

This logic is used in:

- Update operation
- Delete operation

---

# 💾 Data Storage

The current version of the project stores data temporarily in memory.

The main list is:

```python
students = []
```

When a student is added:

```python
students.append(student)
```

the information remains available while the program is running.

### Important:

The current version does **not** use:

- MySQL
- SQLite
- CSV files
- JSON files
- External databases

Therefore, student data will be lost when the program is closed.

---

# 🛠️ Technologies Used

## Programming Language

🐍 **Python**

## Code Editor

💻 **Visual Studio Code**

## Python Features

- Lists
- Dictionaries
- Loops
- Conditional Statements
- Match-Case
- User Input
- Basic CRUD Operations

---

# 📂 Project Structure

```text
Student-Data-Organizer/
│
├── student_data_organizer.py
│
├── README.md
│
└── screenshots/
    ├── add-student.png
    ├── display-students.png
    └── update-student.png
```

---

# ▶️ Installation & Setup

## Step 1 — Install Python

Download and install Python on your computer.

Check whether Python is installed:

```bash
python --version
```

---

## Step 2 — Clone the Repository

Clone the GitHub repository using:

```bash
git clone <your-repository-url>
```

---

## Step 3 — Open the Project

Open the project folder in **Visual Studio Code**.

---

## Step 4 — Run the Program

Run:

```bash
python student_data_organizer.py
```

The application will start in the terminal.

---

# 🧪 Testing Scenarios

The project can be tested using different scenarios.

| Test | Expected Result |
|---|---|
| Add valid student | Student added |
| Display students | Student records displayed |
| Update existing ID | Information updated |
| Update invalid ID | Student not found |
| Delete existing ID | Student deleted |
| Delete invalid ID | Student not found |
| Select option 5 | Subjects displayed |
| Select option 6 | Program exits |
| Enter invalid menu choice | Invalid choice displayed |

---

# 📊 Current Limitations

Although the project performs basic student management successfully, the current version has some limitations.

### 1. Temporary Data

Student data is stored only in memory.

### 2. No Database

The project does not currently use a database.

### 3. Basic Validation

The application currently uses basic input handling.

For example, entering text where an integer is expected may generate an error.

### 4. Console-Based Interface

The application currently runs through the terminal and does not have a graphical user interface.

### 5. No Authentication

There is currently no login or user authentication system.

---

# 🚀 Future Enhancements

The project can be improved in several ways.

## 💾 File Storage

Student records could be stored permanently using:

- CSV
- JSON
- Text files

---

## 🗄️ Database Integration

The application could be connected with:

- SQLite
- MySQL

This would allow student data to remain available even after closing the program.

---

## 🔍 Advanced Search

Future versions could allow searching by:

- Student ID
- Name
- Grade
- Course
- Subject

---

## 📊 Student Statistics

The application could calculate:

- Average age
- Number of students
- Grade distribution
- Subject-wise student count

---

## 🖥️ Graphical User Interface

A GUI could be created using Python libraries such as:

- Tkinter
- PyQt

This would make the application more interactive and visually user-friendly.

---

## 🔐 Authentication

A future version could include:

- Admin Login
- Username and Password
- User Roles
- Secure Access

---

# 🎓 Learning Outcomes

After completing this project, I practiced and strengthened my understanding of:

### Python Fundamentals

- Variables
- Data Types
- Input and Output
- Operators

### Data Structures

- Lists
- Dictionaries

### Control Flow

- `if-else`
- `for` loop
- `while` loop
- `match-case`

### Data Management

- Adding records
- Reading records
- Updating records
- Deleting records

### Problem Solving

The project helped me understand how multiple Python concepts can work together to solve a practical problem.

---

# 💭 What I Learned From This Project

This project helped me move from writing small individual Python programs to creating a complete **menu-driven application**.

I learned how to:

- Break a problem into smaller operations
- Design a simple menu system
- Store multiple records using Lists
- Organize individual records using Dictionaries
- Search records using loops and conditions
- Modify existing dictionary values
- Remove records from a list
- Handle different user choices
- Implement basic CRUD functionality
- Structure a Python project for GitHub

---

# 📈 Skills Practiced

```text
Python
  │
  ├── Variables
  ├── Input / Output
  ├── Lists
  ├── Dictionaries
  ├── Loops
  ├── Conditions
  ├── Match-Case
  ├── CRUD Operations
  └── Problem Solving
```

---

# 🌱 Project Development Journey

This project represents one step in my programming learning journey.

I started by learning individual Python concepts such as:

```text
Variables
   ↓
Input / Output
   ↓
Conditions
   ↓
Loops
   ↓
Lists
   ↓
Dictionaries
   ↓
Match-Case
   ↓
CRUD Operations
   ↓
Student Data Organizer
```

The goal is to gradually apply these fundamentals to larger and more practical projects.

---

# 🔮 Future Vision

The current console application can be considered a foundation for a more advanced Student Management System.

In future versions, the project can evolve from:

```text
Python Console Application
        ↓
File-Based Application
        ↓
Database Application
        ↓
GUI Application
        ↓
Complete Student Management System
```

---

# 📸 Screenshots

Add your project screenshots inside the `screenshots` folder.

Example:

```markdown
![Add Student](screenshots/add-student.png)

![Display Students](screenshots/display-students.png)

![Update Student](screenshots/update-student.png)
```

---

# 📁 Repository Information

**Project Name:** Student Data Organizer

**Project Type:** Python Fundamentals Project

**Application Type:** Console-Based Application

**Programming Language:** Python

**Difficulty Level:** Beginner

**Data Storage:** In-Memory List

**Database:** Not Used

**Interface:** Command Line / Terminal

---

# ⭐ Project Highlights

- ✔️ Menu-driven application
- ✔️ Student record management
- ✔️ List and Dictionary implementation
- ✔️ Basic CRUD operations
- ✔️ Student search functionality
- ✔️ Update and delete functionality
- ✔️ Subject management
- ✔️ Invalid choice handling
- ✔️ Beginner-friendly Python implementation
- ✔️ Practical application of Python fundamentals

---

# 👩‍💻 Author

## Drashti Vadukul

**BCA Student | AI, ML & Data Science Learner | Web Development Enthusiast**

### 💻 Technical Interests

- 🐍 Python
- 📊 Data Analytics
- 🤖 Artificial Intelligence
- 🧠 Machine Learning
- 🌐 HTML & CSS
- 🔧 Git & GitHub
- 📈 Data Science

### 📚 Current Learning

Currently building my foundation in:

- Python Programming
- Data Analytics
- AI & Machine Learning
- Data Science
- Web Development Fundamentals

I am focusing on learning concepts step-by-step and applying them through practical projects.

---

# 🌟 Learning Philosophy

> **Learn → Practice → Build → Improve**

I believe that building small practical projects is an important part of developing programming and problem-solving skills.

This project is one of the steps in my journey toward building stronger technical skills and creating more advanced applications in the future.

---

# 🏆 Project Status

**Status:** ✅ Completed

**Version:** `1.0`

**Project Category:** Python Fundamentals

**Purpose:** Learning & Practice

---

# 📌 Note

This project was developed for educational and practice purposes as part of my Python learning journey.

The application focuses on understanding Python fundamentals rather than advanced database or software architecture.

---

# ⭐ Acknowledgement

Thank you for taking the time to explore my project.

I am continuously learning, practicing, and improving my programming skills through hands-on projects.

---

## 🚀 Keep Learning. Keep Building. Keep Improving. 💻🐍



## Output
![Program Output](output (1).png)
