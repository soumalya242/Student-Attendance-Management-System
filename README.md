# Student Attendance Management System

A web-based Student Attendance Management System built as a college mini-project using Python, Flask, MySQL, HTML, and CSS.

## Features

- Dashboard for easy navigation
- Add new student details
- View the list of students
- Mark daily student attendance
- Prevent duplicate attendance for the same student on the same day
- View attendance records
- Store student and attendance data in MySQL
- Display success and error messages

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- MySQL Connector/Python
- python-dotenv

## Project Structure

```text
Student_attendance/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   ├── students.html
│   ├── attendance.html
│   ├── attendance_records.html
│   └── add_student.html
└── static/
    └── style.css
```


## Requirements

- Python installed on your computer
- MySQL Server
- MySQL Workbench (recommended)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-attendance-system.git
cd student-attendance-system
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bat
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```


### 4. Run the Application

```bash
python app.py
```

Open the application in your browser:

http://127.0.0.1:5000

## How to Use

1. Open the dashboard.
2. Add student information.
3. View the registered students.
4. Mark attendance for a student.
5. View attendance records.

## Future Improvements

- Edit and delete student details
- Search and filter attendance records
- Generate attendance reports
- Calculate attendance percentages
- Add user authentication
