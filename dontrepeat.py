import boto3
from boto3.dynamodb.conditions import Key, Attr
import os
import random
tableName = 'Ryan'

newWords = input("Enter new words: ")
words = newWords.split(' ')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(tableName)
print("So far you have entered ",table.item_count,"unique words")

while( newWords != ''):
    for word in words:
        if word is not None and word != '':
            response = table.query(
                KeyConditionExpression=Key('name').eq(word)
            )
            count = response['Count']
            if count == 0:
                response = table.put_item(
                    Item={
                    'name': word,
                }
                )
                if word[-2:]=='er' or word[-2:]=='or':
                    os.system('say '+word+', I hardly know her')
            
            else:
                print(word, 'already used')
                os.system('say you idiot, you already said the word'+word)
    newWords = input("Enter new words: ")
    words = newWords.split(' ')


    