import json
import boto3
from datetime import datetime

def lambda_handler(event, context):

   print("Event json %s" % json.dumps(event))
   print("Context %s" % context)
   
   client = boto3.resource('dynamodb')

   table = client.Table('tutorials')

   eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
   published = False
   
   response = table.put_item(
       Item={
           'id':  context.aws_request_id,

           'title': event['title'],

           'description': event['description'],
           
           'published': published,
           'createdAt': eventDateTime,
           'updatedAt': eventDateTime
          
       }
   )

   return {

       'statusCode': response['ResponseMetadata']['HTTPStatusCode'],

       'body': 'Record ' +  context.aws_request_id + ' added'

   }