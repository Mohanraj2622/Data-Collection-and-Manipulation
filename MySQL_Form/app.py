from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=" list_of_data "
)

# Route to display the list of users
@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT name, email FROM user")
    users = cursor.fetchall()
    cursor.close()
    return render_template("index.html", users=users)

# Route to display the list of users
@app.route("/list-users/")
def list_users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    cursor.close()

    if users:
        return render_template("list_users.html", users=users)
    else:
        return render_template("list_users.html", error="No users found.")

# Route to add a new user
@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        cursor = db.cursor()
        sql = "INSERT INTO user (name, email, phone) VALUES (%s, %s, %s)"
        values = (name, email, phone)
        cursor.execute(sql, values)
        db.commit()
        cursor.close()

        return redirect(url_for("list_users"))

    return render_template("add_user.html")

# Route to edit an existing user
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE id=%s", (id,))
    user = cursor.fetchone()
    cursor.close()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        cursor = db.cursor()
        sql = "UPDATE user SET name=%s, email=%s, phone=%s WHERE id=%s"
        values = (name, email, phone, id)
        cursor.execute(sql, values)
        db.commit()
        cursor.close()

        return redirect(url_for("list_users"))

    return render_template("edit_user.html", user=user)

# Route to delete a user
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete_user(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM user WHERE id=%s", (id,))
    db.commit()
    cursor.close()

    return redirect(url_for("list_users"))

if __name__ == "__main__":
    app.run(debug=True)