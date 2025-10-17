# 🗂️ To-Do List Manager

A simple and structured command-line (CLI) project and task management tool.  
This program helps you organize projects and tasks efficiently — with full control over creation, editing, deletion, and viewing.

---

## ✨ Features

- ✅ Create and delete projects  
- ✅ Add, edit, and remove tasks within each project  
- ✅ Validate titles, descriptions, and deadlines  
- ✅ Beautiful and user-friendly CLI interface  
- ✅ Modular and extensible design (future-ready for GUI or API)  
- ✅ Manage multiple projects simultaneously  

---


---

## 🚀 Installation & Usage

### 1️⃣ Requirements
Make sure Python 3.9 or higher is installed:

```bash
python --version
```
گ
### 2️⃣ Clone the repository

```bash
git clone https://github.com/saleh-sabagh/to-do-list-2-
cd to-do-list-2-/src/to_do_list
```

### 3️⃣ Install dependencies

```bash
pip install poetry
poetry install
```


### 4️⃣ Run the program

```bash
poetry env activate
poetry run python -m main
```
## 💡 How to Use

After running the program, you’ll see the main CLI menu:

===== TO DO LIST MANAGER =====
1. Create new project
2. Add task to project
3. Edit project
4. Edit task
5. Delete task from project
6. List all projects
7. List tasks in project
8. Delete project
0. Exit
==============================


### Available actions:

1 → Create a new project

2 → Add a task to a project

3 / 4 → Edit project or task

5 / 8 → Delete task or project

6 / 7 → View all projects or all tasks

## 🧠 Object-Oriented Design
### 🧩 Task Class

Represents a single task with:

id: unique identifier

title: short name of the task

description: detailed information

deadline: due date in YYYY-MM-DD format

status: "todo", "doing", or "done"

### 🗂️ Project Class

Represents a project containing multiple tasks:

Add or remove tasks

Edit project name or description

Retrieve and list project tasks

