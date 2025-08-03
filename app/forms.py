from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange, Length
from app.models import User

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already registered. Please use a different email address.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

# logout
class LogoutForm(FlaskForm):
    submit = SubmitField('Log Out')

class AccessWealthPaymentForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Pay Now')

class PaymentForm(FlaskForm):
    name_first = StringField("First Name", validators=[DataRequired(), Length(max=50)])
    name_last = StringField("Last Name", validators=[DataRequired(), Length(max=50)])
    email_address = StringField("Email", validators=[DataRequired(), Email()])
    amount = DecimalField("Amount (R)", validators=[DataRequired(), NumberRange(min=1)], places=2)
    submit = SubmitField("Pay Now")

