from flask import Flask, render_template, redirect, url_for,request,send_file, send_from_directory
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
	ROI_number=0
	ROI_number = ROI_number+1
	if request.method=="POST":
		delete()
		uploaded_files = flask.request.files.getlist("file")
		if request.files['file'].filename == '':
			return render_template('error.html')
		print (uploaded_files)
		for file in uploaded_files:
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		convert(ROI_number)
		return redirect(url_for('download'))

@app.route('/download', methods=['GET','POST'])
def download():
	workingdir = os.path.abspath(os.getcwd())
	print(workingdir)
	return render_template('download.html')



@app.route('/download_file')
def download_file():
	return send_file('result/converted_pdf.pdf', as_attachment=True, cache_timeout=0)

if __name__ == "__main__":

	app.run(debug=True)