import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    return render_template("index.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        stock1 = lookup(request.form.get("symbol"))

        if not stock1:
            return apology("Invalid Stock.")

        if not request.form.get("shares"):
            return apology("Missing shares!")

        if request.form.get("shares") <= 0:
            return apology("Invalid shares!")

        shares = int(request.form.get("shares"))
        cash = db.execute("SELECT cash FROM users WHERE id = :x", x=session["user_id"])
        buying = stock1["price"] * shares

        if not cash or float(cash[0]["cash"]) < buying:
            return apology("Not enough money")

        db.execute("INSERT INTO stocks (symbol, shares, price_per_share, total_price, user_id, process) VALUES(:symbol, :shares, :price, :price1, :id, :pro)",
                   symbol=stock1["symbol"], shares=shares, price=stock1["price"], price1=usd(buying), id=session["user_id"], pro='Bought')

        db.execute("UPDATE users SET cash = cash - :buying WHERE id = :x",
                   buying=buying, x=session["user_id"])

        return render_template("index.html", stock=stock1)

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    hist = db.execute("SELECT * from stocks WHERE user_id=:x", x=session["user_id"])

    return render_template("history.html", hist=hist)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("Invalid Stock.")
        else:
            return render_template("quote1.html", stock=quote)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("Missing Username!")

        elif not request.form.get("password"):
            return apology("Missing Password!")

        elif not request.form.get("confirmation"):
            return apology("Missing Confirmation Password!")

        elif not (request.form.get("password") == request.form.get("confirmation")):
            return apology("Passwords do not match!")

        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                            username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))

        if not result:
            return apology("Username already exist")

        session["user_id"] = result
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":

        stock2 = lookup(request.form.get("symbol2"))

        if not stock2:
            return apology("Invalid Stock.")

        if not request.form.get("shares2"):
            return apology("Missing shares!")

        shares = int(request.form.get("shares2"))
        cash = db.execute("SELECT cash FROM users WHERE id = :x", x=session["user_id"])
        selling = stock2["price"] * shares

        db.execute("INSERT INTO stocks (symbol, shares, price_per_share, total_price, user_id, process) VALUES(:symbol, :shares, :price, :price1, :id, :pro)",
                   symbol=stock2["symbol"], shares=shares, price=stock2["price"], price1=usd(selling), id=session["user_id"], pro='Sold')

        db.execute("UPDATE users SET cash = cash + :selling WHERE id = :x",
                   selling=selling, x=session["user_id"])

        return redirect("index.html")

    else:
        return render_template("sell.html")


def errorhandler(e):
    """Handle error"""
    return apology("HI")
    # e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
