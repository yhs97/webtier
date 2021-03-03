import boto3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# def uploadToS3()

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_files = request.files.getlist('file[]')
    print(uploaded_files)
    s3 = boto3.client('s3')
    sqs = boto3.resource('sqs', region_name='us-east-1')
    queue = sqs.get_queue_by_name(QueueName='requestq')


    for uploaded_file in uploaded_files:
	    if uploaded_file.filename != '':
	    	uploaded_file.save(uploaded_file.filename)
	    	s3Response = s3.upload_file(uploaded_file.filename, 'inputimgs', uploaded_file.filename)
    		sqsResponse = queue.send_message(MessageBody=uploaded_file.filename)
    		print(sqsResponse.get('MessageId'))
    		print(sqsResponse.get('MD5OfMessageBody'))

    return redirect(url_for('index'))