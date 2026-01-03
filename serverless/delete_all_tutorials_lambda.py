
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tutorials')

def lambda_handler(event, context):
    scan = None

    with table.batch_writer() as batch:
        # Iterate through table until fully scanned
        while scan is None or 'LastEvaluatedKey' in scan:
            if scan and 'LastEvaluatedKey' in scan:
                scan = table.scan(
                    ProjectionExpression='id',  # Primary key
                    ExclusiveStartKey=scan['LastEvaluatedKey']
                )
            else:
                scan = table.scan(
                    ProjectionExpression='id'
                )

            for item in scan.get('Items', []):
                batch.delete_item(
                    Key={'id': item['id']}
                )

    return {
        'statusCode': 204,
        'body': 'All Tutorials Deleted successfully'
    }
