from ensurepip import bootstrap

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_bootstrap import Bootstrap

VALID_EMAIL = "admin@email.com"
VALID_PASSWORD = "12345678"

def length(min=-1):
    message = f'Field must be at least {min} characters long'

    def _length(form, field):
        if len(field.data) < min:
            raise ValidationError(message)

    return _length

class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email('Invalid email')])
    password = PasswordField(label='password', validators=[DataRequired(), length(8)])
    submit = SubmitField(label='Login')

app = Flask(__name__)
app.secret_key = "mysecretkey"
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html', bootstrap=bootstrap)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == VALID_EMAIL and form.password.data == VALID_PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)