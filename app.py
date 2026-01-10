import os
import requests
from flask import Flask, render_template, request, redirect, flash
from dotenv import load_dotenv

# Load .env
load_dotenv()

app = Flask(__name__)

# Secret key from .env
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_secret_key")

# Telegram credentials
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


@app.route("/")
def homepage():
    return render_template("home_page.html")
@app.route("/profile")
def profile():
    return render_template("index.html")
@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        telegram_message = (
            f"📩 New Contact Form Submission:\n\n"
            f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        )

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params = {"chat_id": CHAT_ID, "text": telegram_message}

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if response.status_code == 200 and data.get("ok"):
                flash("Message sent successfully!", "success")
            else:
                error_desc = data.get("description", "Unknown error")
                flash(f"Failed to send message. Telegram error: {error_desc}", "danger")
        except Exception as e:
            flash(f"Error sending message: {e}", "danger")

        return redirect("/contact")

    return render_template("contact.html")


@app.route("/cv")
def cv():
    return render_template("CV.html")

if __name__ == "__main__":
    app.run(debug=True)