python
Copy code
import boto3
from datetime import datetime

# Подключение к DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Имя_таблицы')

# User_ID пользователя и значения активности
user_id = 'Уникальный_ID_пользователя'
activities = ['активность1', 'активность2', 'активность3']

# Создание записи в таблице
timestamp = datetime.now().strftime('%Y-%m-%d')
table.put_item(
    Item={
        'User_ID': user_id,
        'Activities': activities,
        'Date': timestamp
    }
)