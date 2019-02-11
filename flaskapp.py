import os
import time
from flask import Flask, render_template, request, Response, redirect, url_for, send_from_directory
from PIL import Image
from scipy import misc

app = Flask(__name__)

UPLOAD_FOLDER = '/var/www/html/flaskapp/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload' , methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.isfile(path):
        return render_template("upload.html", path=path, filename=filename)
    else:
        file.save(path)
        return render_template("upload.html", path=path, filename=filename)

@app.route("/uploads/<filename>")
def retrieve(filename):
    try:
        return send_from_directory(UPLOAD_FOLDER,filename)
    except Exception as e:
        return str(e)

@app.route('/properties' , methods=['GET'])
def properties():
    filename = request.args['filename']
    app.config['UPLOAD_FOLDER'] = os.path.realpath('.')+'/var/www/html/flaskapp/uploads'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    im = Image.open(filepath)
    msg1 = "Creation date : "+ str(time.ctime(os.path.getctime(filepath)))
    msg2 = " modification time : "+ str(time.ctime(os.path.getmtime(filepath)))
    msg3 = "Size : "+str(os.path.getsize(filepath))
    msg4 = " Image Resolution : "+str(im.size)
    msg5 = " Average RGB Mean : "+str(misc.imread(filepath).mean(axis=(0,1)))
    return render_template('upload.html',msg1=msg1,msg2=msg2,msg3=msg3,msg4=msg4,msg5=msg5,filepath=filepath,filename=filename)

@app.route('/delete' , methods=['GET'])
def delete():
    filename = request.args['filename']
    app.config['UPLOAD_FOLDER'] = os.path.realpath('.')+'/var/www/html/flaskapp/uploads'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.isfile(filepath):
        os.unlink(filepath)
        msg = "Image has been deleted"
    return render_template('upload.html', msg = msg, filename=filename)
if __name__ == "__main__":
    app.run(debug=True)