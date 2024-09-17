from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/ff599056d3e97ac4abb7')
    posts = response.json()
    return render_template("index.html", posts=posts)

@app.route('/post/<int:id>')
def post(id):
    response = requests.get('https://api.npoint.io/ff599056d3e97ac4abb7')
    posts = response.json()
    target_post = None
    for post in posts:
        if post['id'] == id:
            target_post = post
            break
    return render_template("post.html", post=target_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
