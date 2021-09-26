import json
import boto3
import uuid
import bcrypt
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    
    # (POST) Create User Route
    if event['rawPath'] == '/createUser':
        decodedEvent = json.loads(event['body'])
        email = decodedEvent['email']
        password = decodedEvent['password']
        userName = decodedEvent['userName']
        userType = decodedEvent['userType']
        
        
        # hashing password
        b_password = password.encode('utf-8') # string to bytes
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(b_password, salt)
        hashed_password = hashed_password.decode('utf-8') # bytes to string
        # checking user type
        if userType == 'Learner':
            userId = 'L-' + str(uuid.uuid4())
        elif userType == 'Trainer':
            userId = 'T-' + str(uuid.uuid4())
        elif userType == 'HR':
            userId = 'H-' + str(uuid.uuid4())
            
        try:
            response = table.query(
                KeyConditionExpression=Key('email').eq(email)
                )
            count = response['Count']
            if count == 0:
                response = table.put_item(
                    Item={
                        'email': email,
                        'userName': userName,
                        'password': hashed_password,
                        'userType': userType,
                        'userId': userId
                    })
                return response, userId
            else:
                return "user is already registered!"
                
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response
    
    # (GET) User Login Route
    elif event['rawPath'] == '/userLogin':
        email = event['queryStringParameters']['email']
        password = event['queryStringParameters']['password']
        
        b_password = password.encode('utf-8')

        try:
            response = table.query(
                KeyConditionExpression=Key('email').eq(email)
                )
            items = response['Items']
            hashed = items[0]['password'] # string
            hashed = hashed.encode('utf-8') # string to bytes

            if bcrypt.checkpw(b_password, hashed):
                return response
            else:
                return "Error user is not authenticated"
                
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response