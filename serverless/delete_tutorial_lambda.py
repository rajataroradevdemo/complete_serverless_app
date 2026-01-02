import json
import boto3

def lambda_handler(event, context):

   client = boto3.resource('dynamodb')

   table = client.Table('tutorials')

   response = table.delete_item(

       Key={

           'id': event['id']

       }

   )

   return {
           'statusCode': '204',
           'body': 'Tutorial Deleted successfully'
       }