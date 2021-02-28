from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_files = request.files.getlist('file[]')
    print(uploaded_files)
    
    for uploaded_file in uploaded_files:
	    if uploaded_file.filename != '':
	    	uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))