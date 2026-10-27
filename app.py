import os
from dotenv import load_dotenv  
from flask import Flask, render_template, request, redirect, flash
import mysql.connector
from datetime import date
load_dotenv()



app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )
    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/students")
def view_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("students.html", students=students)


@app.route("/attendance")
def attendance_page():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("attendance.html", students=students)




@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():
    student_id = request.form["student_id"]
    status = request.form["status"]

    connection = get_db_connection()
    cursor = connection.cursor()
    today = date.today()

    cursor.execute(
        "SELECT id FROM attendance WHERE student_id = %s AND attendance_date = %s",
        (student_id, today)
    )

    existing_record = cursor.fetchone()

    if existing_record:
        cursor.close()
        connection.close()

        flash("Attendance has already been recorded for this student today!", "error")
        return redirect("/attendance")

    cursor.execute(
        "INSERT INTO attendance (student_id, attendance_date, status) VALUES (%s, %s, %s)",
        (student_id, today, status)
    )

    connection.commit()
    cursor.close()
    connection.close()

    flash("Attendance saved successfully!", "success")
    return redirect("/attendance")




@app.route("/attendance_records")
def attendance_records():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT students.name, students.roll_no,
        attendance.attendance_date, attendance.status
        FROM attendance
        JOIN students ON attendance.student_id = students.id
        ORDER BY attendance.attendance_date DESC
    """)
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("attendance_records.html", records=records)




@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        roll_no = request.form["roll_no"]
        department = request.form["department"]

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO students (name, roll_no, department) VALUES (%s, %s, %s)",
            (name, roll_no, department)
        )

        connection.commit()
        cursor.close()
        connection.close()

        return redirect("/students")

    return render_template("add_student.html")



if __name__ == "__main__":
    app.run(debug=True)
