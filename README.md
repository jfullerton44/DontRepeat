# DontRepeat
Python Program to track unique words said by user

## Setup
* In order for this to work you must have local AWS credientials and a DynamoDB table with the name set to tableName on line 5.
  * The table must have the primary key: 'name'

## Execution
* Run with command *python dontrepeat.py*
* Will run until empty string is entered as a word

## Notes
* Word count displayed in program will only update every 6 hours. 
  * To create a continusly updating word count the table.item_count must be replaced with a scan query (very inefficient)
