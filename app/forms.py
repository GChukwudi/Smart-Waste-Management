from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ScheduleForm(FlaskForm):
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Schedule')

class RecyclingForm(FlaskForm):
    # materials = StringField('Materials', validators=[DataRequired()])
    # submit = SubmitField('Log Recycling')
    materials = SelectField('Materials', choices=[
        ('plastic', 'Plastic'),
        ('glass', 'Glass'),
        ('paper', 'Paper'),
        ('metal', 'Metal'),
        ('organic', 'Organic'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    submit = SubmitField('Log Recycling')

class ImpactMetricForm(FlaskForm):
    carbon_saved = FloatField('Carbon Saved (kg)', validators=[DataRequired()])
    energy_saved = FloatField('Energy Saved (kWh)', validators=[DataRequired()])
    submit = SubmitField('Track Impact')
