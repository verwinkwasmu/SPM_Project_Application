from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import boto3
from botocore.exceptions import ClientError
import logging
import os

app = Flask(__name__)
BUCKET = os.getenv('BUCKET')
S3_DOMAIN = os.getenv('S3_DOMAIN')

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
    content_type = request.mimetype

    try:
        response = s3.put_object(ACL='public-read',
                                 Body=file,
                                 Bucket=BUCKET,
                                 Key=f'{courseId}/{className}/{sectionName}/' + filename,
                                 ContentType=content_type)
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

            result.append({"filename": filename,
                           "url": url,
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
