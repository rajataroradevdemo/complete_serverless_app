import json
import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr

def lambda_handler(event, context):
   print("Event json %s" % json.dumps(event))
   print("Context %s" % context)
   
   client = boto3.resource('dynamodb')
   table = client.Table('tutorials')
   
   title = event['title']
   
   print("Getting Title Filter %s" % title)
   
   if not title:
      print("Title is empty")
      response = table.scan()
   else:
      print("Title is NOT empty")
      response = table.scan(
                     FilterExpression = Attr('title').begins_with(title)
                     )

   return response['Items']
  
