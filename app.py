from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from gan import generateMonet
from werkzeug.utils import secure_filename

#from flask import render_template, request, redirect

from flask import Flask

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "not-so-secret-key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route("/", methods=["GET", "POST"])
# def index():
#     return render_template("index.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    return render_template("results.html")

@app.route('/', methods=['POST'])
def upload_image():

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No image selected for uploading.')
        return redirect(request.url)

    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        generateMonet(filename)
        return render_template('results.html', filename=filename)

    else:
        flash('Only the following files are allowed: .png, .jpg, .jpeg')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):

    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)