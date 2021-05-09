from flask import Flask
from flask import request
from flask import render_template
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

@app.route('/contact')
def contact():
    return render_template("contact.html")

#errors
@app.errorhandler(404)
def not_found_error(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=False)

