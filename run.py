import os

from flask import Flask
from flask import request
from flask import render_template
from forms import ContatcForm
from flask import send_from_directory
from flask_mail import Mail, Message
from flask import abort,redirect,url_for,make_response
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContatcForm()

    if request.method == 'POST':
        subject = request.form.get('subject')
        name = request.form.get("name")
        message = request.form.get('message')
        email = request.form.get('email')
        recipients = ['vassilli.zaitsev@gmail.com']
        mesageToMe = Message(subject=subject,
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=recipients, # replace with your email for testing
                      body="Message from: " + name + "\n" + "email: " + email + "\n" + "Message:"+ message)
        messageToSender = Message(subject="Dziękuje za wysłanie wiadomośći",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=list(email.split(" ")), # replace with your email for testing
                      body="Dziękuję za wiadomość, wkrótce odpiszę")
        mail.send(mesageToMe)
        mail.send(messageToSender)

        return render_template('contact_form/contactsuccess.html')
    elif request.method == 'GET':
        return render_template('contact_form/contact.html', form=form)
#    return render_template("contact.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#errors
@app.errorhandler(404)
def not_found_error(e):
    return render_template('error_pages/404.html'), 404

@app.errorhandler(500)
def not_found_error(e):
    return render_template('error_pages/500.html'), 500

#email configuration
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'vassilli.zaitsev@gmail.com',
    MAIL_PASSWORD = 'tgxphhhryjroxoas'
    )
mail = Mail(app)


app.secret_key = '289304jkdhfasd08f87sdayfasd89ufjsadfus'
if __name__ == '__main__':
    app.run(debug=False)

