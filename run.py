import os

from flask import Flask
from flask import request
from flask import render_template
from forms import ContatcForm
from flask import send_from_directory
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
        return render_template('contactsuccess.html')
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
#    return render_template("contact.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#errors
@app.errorhandler(404)
def not_found_error(e):
    return render_template('404.html'), 404

app.secret_key = '289304jkdhfasd08f87sdayfasd89ufjsadfus'
if __name__ == '__main__':
    app.run(debug=False)

