from flask import Flask

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWdrdWZ3ZWE4dDE2ZDM3cWkyank2dG1vcWNraWk4NzRmbmJuNXZxaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g7YDlrD5YLqfe/giphy.webp" alt="A gif of a cat waving">'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Goodbye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)