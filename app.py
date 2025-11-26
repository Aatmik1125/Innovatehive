from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")  # use env var in prod

# Home + main pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/projects")
def projects():
    # You can supply projects array for dynamic rendering later
    return render_template("projects.html")

@app.route("/blogs")
def blogs():
    return render_template("blogs.html")

@app.route("/testimonials")
def testimonials():
    return render_template("testimonials.html")

# Contact: simple POST handling (saves submissions to a local file for demo)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in required fields (name, email, message).", "danger")
            return redirect(url_for("contact"))

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }

        # Append to local file (demo-only). In real app, send email / DB entry.
        submissions_file = os.path.join(os.path.dirname(__file__), "submissions.txt")
        with open(submissions_file, "a", encoding="utf-8") as f:
            f.write(str(entry) + "\n")

        flash("Thanks! Your message has been received.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
