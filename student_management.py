from flask import Flask, render_template, request, redirect, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"


# -----------------------------
# DATABASE INITIALIZATION
# -----------------------------

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


init_db()


# -----------------------------
# HOME (Dashboard)
# -----------------------------

@app.route("/", methods=["GET"])
def home():
    if "user" not in session:
        return redirect("/login")

    search = request.args.get("search")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    if search:
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ?",
            ('%' + search + '%',)
        )
    else:
        cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    conn.close()

    return render_template("index.html", students=students)


# -----------------------------
# ADD STUDENT
# -----------------------------

@app.route("/add", methods=["POST"])
def add():
    if "user" not in session:
        return redirect("/login")

    name = request.form["name"]
    age = request.form["age"]
    course = request.form["course"]

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    conn.close()

    flash("Student added successfully!", "success")
    return redirect("/")


# -----------------------------
# DELETE STUDENT
# -----------------------------

@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    flash("Student deleted successfully!", "danger")
    return redirect("/")


# -----------------------------
# EDIT STUDENT
# -----------------------------

@app.route("/edit/<int:id>")
def edit(id):
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cursor.fetchone()
    conn.close()

    return render_template("edit.html", student=student)


# -----------------------------
# UPDATE STUDENT
# -----------------------------

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    if "user" not in session:
        return redirect("/login")

    name = request.form["name"]
    age = request.form["age"]
    course = request.form["course"]

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, id)
    )
    conn.commit()
    conn.close()

    flash("Student updated successfully!", "info")
    return redirect("/")


# -----------------------------
# REGISTER
# -----------------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            conn.commit()
            flash("Registration successful! Please login.", "success")
            return redirect("/login")
        except:
            flash("Username already exists!", "danger")

        conn.close()

    return render_template("register.html")


# -----------------------------
# LOGIN
# -----------------------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = username
            flash("Login successful!", "success")
            return redirect("/")
        else:
            flash("Invalid credentials!", "danger")

    return render_template("login.html")


# -----------------------------
# LOGOUT
# -----------------------------

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully!", "info")
    return redirect("/login")


# -----------------------------
# RUN APP
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)
