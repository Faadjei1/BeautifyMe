import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

import datetime

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///final.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    # code for get requeset
    return render_template("index.html")



@app.route("/register", methods=["GET", "POST"])
def register():

    session.clear()
    # Reach user via POST
    if request.method == "POST":

        # Check for the submission of username
        if not request.form.get("name"):
            return apology("must provide name", 200)

        # check for an email
        if not request.form.get("email"):
            return apology("must provide an email", 200)

         # Check for the submission of password
        if not request.form.get("password"):
            return apology("must provide password", 200)

        # Check for the confirmation of password
        if not request.form.get("confirmation"):
            return apology("must confirm password", 200)

        # check if passwords match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 200)

        # Create variables and store information received
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if password != confirmation:
            return apology("Password mismatch")

        hash = generate_password_hash(password)
        users = db.execute("SELECT id FROM users where email = ?", email)

        if len(users) != 0:
            return apology("invalid email")

        # Check if username is taken
        # for user in users:
        #     if id == user['id']:
        #         return apology("username taken", 200)

        # Add the new user to the  database
        newuser = db.execute("INSERT INTO users (name, email, hash) VALUES (?, ?, ?)", name, email, hash)

        # Query the database for username
        rows = db.execute("SELECT * FROM users WHERE email = ?", email)

        # Remember which user just logged in
        session["user_id"] = rows[0]["id"]

        # Redirect the new user to home page
        return redirect("/")
        #Reach User  via GET
    else:
        return render_template("register.html")




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("email"):
            return apology("must provide a valid email", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid email and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        print('passed through here')

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# method for logging out
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/About")
@login_required
def About():
    # code for get requeset
    return render_template("About.html")


@app.route("/Items")
@login_required
def Items():


    return render_template("Items.html")

@app.route("/Contact")
@login_required
def Contact():


    return render_template("Contact.html")

