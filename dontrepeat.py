import boto3
from boto3.dynamodb.conditions import Key, Attr
import os
import random

newWords = input("Enter new words: ")
words = newWords.split(' ')
while( newWords != ''):
    for word in words:
        if word is not None and word != '':
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('Ryan')
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


    