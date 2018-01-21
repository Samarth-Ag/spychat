from termcolor import colored
import csv

with open('friends2.csv','rb') as friend_data:
    csvreader = csv.reader(friend_data)

    for row in csvreader:
        print row