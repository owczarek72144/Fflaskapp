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
    email = TextField("Email", validators=[validators.required(), Email()])
    subject = TextField("Temat", [validators.required()])
    message = TextAreaField("Tekst wiadomosci:", [validators.required()])
    submit = SubmitField("Wyślij")

class AddComment(FlaskForm):
    name = TextField("Imię",[validators.required()])
    message = TextAreaField("Wiadomość",[validators.required()])
    submit = SubmitField("Wyślij komentarz")
    update = SubmitField("Aktualizuj komentarz")
