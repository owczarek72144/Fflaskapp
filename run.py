import os

from flask import Flask
from flask import request
from flask import render_template

from AzureDB import AzureDB
from forms import ContatcForm, AddComment
from flask import send_from_directory
from flask_mail import Mail, Message
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/guestbook')
def guestbook():
    with AzureDB() as a:
        data = a.azureGetAllData();
        return render_template("guestbook.html", data=data)


@app.route('/deleteentry', methods=['POST'])
def deleteentry():
    if request.method == 'POST':
        id = request.form.get('id')
        with AzureDB() as delete:
            delete.azureDeleteEntry(id)
            return guestbook()


@app.route('/editentry', methods=['POST', 'GET'])
def editentry():
    if request.method == 'POST':
        id = request.form.get('id')
        with AzureDB() as getrecord:
            result = getrecord.azureGetRecord(id)
            form = AddComment()
            form.message.data = result[0][2]
            return render_template('addcomment.html', form=form, editItem=True, result=result)

@app.route('/update', methods=['POST'])
def updateentry():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        message = request.form.get('message')
        with AzureDB() as update:
            update.auzreUpdateEntry(id,name,message)
            return guestbook()

@app.route('/addcomment', methods=['GET', 'POST'])
def addcomment():
    form = AddComment()
    if request.method == 'GET':
        return render_template('addcomment.html', form=form, editItem=False)

    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        with AzureDB() as send_data:
            send_data.azureAddData(name, message)
        return render_template('contact_form/success.html', message="Zapisano komentarz")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContatcForm()
    message = ''

    if request.method == 'POST':
        email = request.form.get('email')
        try:
            validate_email(email)
        except EmailNotValidError:
            message = ('email', 'Nieprawidłowy adres mailowy')
            return render_template('contact_form/contact.html', form=form, message=message)

        subject = request.form.get('subject')
        name = request.form.get("name")
        message = request.form.get('message')
        recipients = ['vassilli.zaitsev@gmail.com']
        mesage_to_admin = Message(subject=subject,
                                  sender=app.config.get("MAIL_USERNAME"),
                                  recipients=recipients,  # replace with your email for testing
                                  body="Message from: " + name + "\n" + "email: " + email + "\n" + "Message:" + message)
        message_to_sender = Message(subject="Dziękuje za wysłanie wiadomośći",
                                    sender=app.config.get("MAIL_USERNAME"),
                                    recipients=list(email.split(" ")),  # replace with your email for testing
                                    body="Dziękuję za wiadomość, wkrótce odpiszę")
        mail.send(mesage_to_admin)
        mail.send(message_to_sender)

        return render_template('contact_form/success.html', message="Wysłano wiadomość")
    elif request.method == 'GET':
        return render_template('contact_form/contact.html', form=form, message=message)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# errors
@app.errorhandler(404)
def not_found_error(e):
    return render_template('error_pages/404.html'), 404


@app.errorhandler(500)
def not_found_error(e):
    return render_template('error_pages/500.html'), 500


# email configuration
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='vassilli.zaitsev@gmail.com',
    MAIL_PASSWORD='qplzxmdxmzakrwei'
)
mail = Mail(app)

app.secret_key = '289304jkdhfasd08f87sdayfasd89ufjsadfus'
if __name__ == '__main__':
    app.run(debug=False)
