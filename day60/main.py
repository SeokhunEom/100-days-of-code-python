from flask import Flask, render_template, request
import requests
import smtplib
from email.mime.text import MIMEText

MY_EMAIL = "my_email@naver.com"
PASSWORD = "my_password"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        msg = MIMEText(f"name: {name}\nemail: {email}\nphone: {phone}\nmessage: {message}")
        msg['Subject'] = "NEW MESSAGE"
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        with smtplib.SMTP("smtp.naver.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg.as_string())

        return "<h1>Successfully sent your message</h1>"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
