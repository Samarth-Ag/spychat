
                                            #IMPORTING USEFUL CLASSES,OBJECTS,DETAILS,FILES

from spy_details import Spy,spy,ChatMessage,friend
from steganography.steganography import Steganography
import csv
from termcolor import colored
from datetime import datetime

                                            #FUNCTION TO PRINT CHAT HISTORY

def chat_history():
    choice=select_a_friend()
    print colored(friend[choice].name,'red')
    for chat in friend[choice].chats:
        print "\nMessage is %s" %(chat.message)
        if chat.sent_by_me=="True":
            print "send at time "+ colored(chat.time,'blue')
        else:
            print "read at time " +colored(chat.time,'blue')

                                            #FUNCTION TO LOAD AND SAVE FRIENDS

def load_friends():
    with open('friends2.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data,delimiter=',')

        for row in reader:
            spy = Spy(name=row[0], salutation=row[1], rating=float(row[2]), age=int(row[3]))
            friend.append(spy)
                                            #FUNCTION TO LOAD AND SAVE CHATS

def load_chat():
    with open('chats.csv', 'rb') as chats_data:
        reader = csv.reader(chats_data,delimiter=',')
        for row in reader:
            chat = ChatMessage(message=row[1], time=row[2], sent_by_me=row[3])
            friend[int(row[0])].chats.append(chat)

                                            #FUNCTION TO READ MESSAGE WITH THE HELP OF STEGANOGRAPHY TECHNIQUE
def read_message():
  sender = select_a_friend()
  output_path = raw_input("What is the name of the file?")
  str,str2=output_path.split('.')
  while str2!='jpg':
      print colored("error: please enter correct file name", 'red')
      output_path = raw_input("What is the name of the file?")
      str, str2 = output_path.split('.')
  secret_text = Steganography.decode(output_path)
  new_chat =ChatMessage(secret_text,datetime.now(),False)
  friend[sender].chats.append(new_chat)
  with open('chats.csv', 'a') as chat_data:
      writerchat = csv.writer(chat_data)
      writerchat.writerow([sender,new_chat.message, new_chat.time, new_chat.sent_by_me])
  print "Your secret message has been saved! "

                                            #FUNCTION TO SEND MESSAGE WITH THE HELP OF STEGANOGRAPHY TECHNIQUE

def send_message():
    friend_choice = select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    str, str2 = original_image.split('.')
    while str2 != 'jpg':
        print colored("error: please enter correct file name",'red')
        original_image = raw_input("What is the name of the file?")
        str, str2 = original_image.split('.')
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image,output_path,text)
    new_chat2 = ChatMessage(text,datetime.now(), True)
    friend[friend_choice].chats.append(new_chat2)
    with open('chats.csv', 'a') as chat_data:
        writerchat = csv.writer(chat_data)
        writerchat.writerow([friend_choice,new_chat2.message,new_chat2.time,new_chat2.sent_by_me])
    print "Your secret message is ready!"

                                            #FUNCTION TO SELECT A FRIEND

def select_a_friend():
    x=1
    for friends in friend:
        print '%d %s %s' %(x,friends.salutation,friends.name)
        x=x+1
    choice=input("Select your friend")
    return choice-1

                                            #FUNCTION TO ADD FRIEND

def add_friend():
    new_friend=Spy('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name:")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.age = input("Age?")
    new_friend.rating = input("Spy rating?")
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friend.append(new_friend)
        with open('friends2.csv', 'a') as friends_data:
            writer=csv.writer(friends_data)
            writer.writerow([new_friend.name,new_friend.salutation,new_friend.age,new_friend.rating,new_friend.is_online])

        print "FRIEND ADDED"
    else:
        print colored('error:Sorry! Invalid entry. We can\'t add spy with the details you provided','red')
    return len(friend)

                                            #FUNCTION TO DISPLAY AND SELECT THE OPTION FROM MENU

def start_chat(spy):
    show_menu = True
    current_status_message = None
    while show_menu :
        menu_choices = colored("What do you want to do? \n\n 1.Add a status update\n 2.Add a friend\n 3.Send a secret message \n 4.Read a secret message  \n 5.Read chats from user \n 6.Close Applicattion",'blue')
        menu_choice = input(menu_choices)

        if menu_choice == 1:
            current_status_message=add_status(current_status_message)
        elif menu_choice == 2:
            number_of_friends = add_friend()
            print 'You have %d friends\n' % (number_of_friends)
        elif menu_choice== 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            chat_history()
        elif menu_choice==6:
            print  'Exiting'
            show_menu = False
        else:
            print colored("\nerror:Enter valid choice\n",'red')

                                                #FUNCTION TO ADD A STATUS

def add_status(current_status_message):
    STATUS_MESSAGES = ['My name is Bond', 'James Bond', '007', 'NIGHTFIRE']
    if current_status_message != None:
        print "your current status message is %s \n" %(current_status_message)
    else:
        print '\nYou don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
            print "\nYour status is updated\n"
    elif default.upper()=='Y':
        item_position=1
        for temprorary_status in STATUS_MESSAGES:
            print ("%d %s") %(item_position,temprorary_status)
            item_position=item_position+1
        message_selection=input("ENTER YOUR CHOICE")
        print "\nYour status is updated\n"
        if message_selection <= len(STATUS_MESSAGES):
            updated_status_message = STATUS_MESSAGES[message_selection-1]
    return updated_status_message

                                                #MAIN

print colored('Let\'s get started','green')
choice=True
while(choice):
    question = "Continue as " + spy.salutation + " " + spy.name + "(Y/N)? "
    existing = raw_input(question)
    if (existing.upper() == "Y"):
        choice=False
        print "\nWelcome %s %s with rating %.2f\n" %(spy.salutation,spy.name,spy.rating)
        load_friends()
        load_chat()
        start_chat(spy)
    elif(existing.upper() == "N"):
        choice = False
        spy = Spy('', '',0,0.0)
        name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
        if len(name) >0 :
            print 'Welcome ' + name + '. Glad to have you back with us.'
            spy.salutation = raw_input("choose your salutation Mr./Mrs")
            spy.name = spy.salutation + " " + name
            print "Alright " + spy.name + '. I\'d ;ike to know a little bit more about ...'
            spy.age = 0
            spy.rating = 0.0
            spy.isonline = False

            spy.age = input("What is your age?")
            if spy.age> 12 and spy.age < 50:
                spy.rating = input("What is your spy rating?")
                if spy.rating> 4.5:
                    print colored('Great ace!','green')
                elif spy.rating > 3.5 and spy.rating <= 4.5:
                    print colored('You are one of the good ones.','green')
                elif spy.rating>= 2.5 and spy.rating <= 3.5:
                    print colored('You can always do better','green')
                else:
                    print colored('We can always use somebody to help in the office.','red')
                spy.is_online = True
                print "\nAuthentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"
                start_chat(spy)
            else:
                print colored('Sorry you are not of the correct age to be a spy','red')

        else:
            print colored("A spy needs to have a valid name. Try again please.",'red')
    else:
        print colored("error: Enter valid choice",'red')
