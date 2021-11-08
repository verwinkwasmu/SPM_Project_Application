from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import boto3
from botocore.exceptions import ClientError
import logging
import os
import mimetypes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


BUCKET = "spm-grp2-storage"
S3_DOMAIN = "http://spm-grp2-storage.s3.amazonaws.com/"

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


@app.route("/upload", methods=['PUT'])
def upload():
    courseId = request.args.get('courseId')
    className = request.args.get('className')
    sectionName = request.args.get('sectionName')
    file = request.files['file']

    filename = secure_filename(file.filename)

    file_type = mimetypes.guess_type(filename)
    
    try:
        response = s3.put_object(ACL='public-read',
                                 Body=file,
                                 Bucket=BUCKET,
                                 Key=f'{courseId}/{className}/{sectionName}/' + filename,
                                 ContentType=file_type[0]
                                 )
        return response

    except ClientError as e:
        logging.error(e)
        return jsonify({
            "message": "Unable to commit to s3.",
            "data": str(request.get_data())
        }), 500


@app.route("/getFiles")
def list_files():
    """
    Function to list files in a given S3 bucket
    """
    courseId = request.args.get('courseId')
    className = request.args.get('className')
    sectionName = request.args.get('sectionName')
    result = []
    try:
        response = s3.list_objects(
            Bucket=BUCKET, Prefix=f'{courseId}/{className}/{sectionName}/')['Contents']
            
        for item in response:
            url = S3_DOMAIN + item['Key']
            filename = (item['Key']).split('/')[-1]
            betterFileId = ((item['Key']).replace('/', '')).replace('.', "")
            
            result.append({"filename": filename,
                           "url": url,
                           "completed": False,
                           "fileId": item['Key'],
                           "betterFileId": betterFileId
                           })
        return jsonify(result)

    except ClientError as e:
        logging.error(e)
        return jsonify({
            "message": "Unable to get files from s3."
        }), 500


@app.route("/removeFile", methods=['DELETE'])
def removeFile():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('courseId', 'className', 'sectionName', 'fileName')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    courseId = data['courseId']
    className = data['className']
    sectionName = data['sectionName']
    fileName = data['fileName']

    try:
        response = s3.delete_object(
            Bucket=BUCKET,
            Key=f'{courseId}/{className}/{sectionName}/' + fileName
        )
        return response
    except ClientError as e:
        logging.error(e)
        return jsonify({
            "message": "Unable to delete file from s3."
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)