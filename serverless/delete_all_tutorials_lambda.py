import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-table')

scan = None

with table.batch_writer() as batch:
     # Iterate through table until it's fully scanned
    while scan is None or 'LastEvaluatedKey' in scan:
        if scan is not None and 'LastEvaluatedKey' in scan:
            scan = table.scan(
                ProjectionExpression='id', # Replace with your actual Primary Key
                ExclusiveStartKey=scan['LastEvaluatedKey'],
            )
        else:
            scan = table.scan(ProjectionExpression='id')

        for item in scan['Items']:
            batch.delete_item(Key={'id': item['id']})
