from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SubmitField, RadioField, SelectField, StringField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    # Name field with required validation
    name = StringField("Candidate Name", [DataRequired("Please enter your name.")])

    # Gender radio buttons with choices
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])

    # Address field (no required validation)
    address = TextAreaField("Address")

    # Email field with required validation and email format check
    email = StringField("Email", [
        DataRequired("Please enter your email address."),
        Email("Please enter a valid email address.")
    ])

    # Age field
    age = IntegerField("Age", validators=[DataRequired()])

    # Programming language selection
    language = SelectField('Programming Languages', choices=[('java', 'Java'), ('py', 'Python')])

    # Submit button
    submit = SubmitField("Submit")
