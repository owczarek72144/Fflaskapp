from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms.validators import DataRequired, Email
import email_validator
from wtforms import TextAreaField
from wtforms import TextField
from wtforms import SubmitField

class ContatcForm(FlaskForm):
    name = TextField("Imię", [validators.required()])
    email = TextField("Email", validators=[DataRequired()])
    subject = TextField("Temat", [validators.required()])
    message = TextAreaField("Tekst wiadomosci:", [validators.required()])
    submit = SubmitField("Wyślij")
