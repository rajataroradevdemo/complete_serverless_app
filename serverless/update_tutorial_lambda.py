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
   
   print("Updating record.")

   response = table.put_item(
       Item={
           'id':  event['id'],
           'title': event['title'],
           'description': event['description'],
           'published': event['published'],
           'updatedAt': eventDateTime,
           'createdAt': eventDateTime
       }
   )

   print("Record updated successfully.")

   return {
       'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
       'body': 'Record ' +  context.aws_request_id + ' updated'
   }