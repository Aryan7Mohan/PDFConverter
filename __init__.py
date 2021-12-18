from flask import Flask, render_template, redirect, url_for,request,send_file
import flask
import os
from convert import *
from delete import *

app = Flask(__name__)

UPLOAD_FOLDER = 'temp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():


	return render_template('index.html')


@app.route("/", methods=['GET','POST'])
def upload():
	if request.method=="POST":
		delete()
		uploaded_files = flask.request.files.getlist("file")
		if request.files['file'].filename == '':
			return render_template('error.html')
		print (uploaded_files)
		for file in uploaded_files:
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		convert()
		return redirect(url_for('download'))

@app.route('/download', methods=['GET','POST'])
def download():
	if request.method=="POST":
		path = "result/converted_pdf.pdf"
		return send_file(path, as_attachment=True)
	return render_template('download.html')


if __name__ == "__main__":

	app.run(debug=True)