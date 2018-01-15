from spy_details import spy
from steganography.steganography import Steganography
from datetime import datetime
friend=[]


def read_message():
  sender = select_a_friend()
  output_path = input("What is the name of the file?")
  secret_text = Steganography.decode(output_path)
  new_chat = {
          "message": secret_text,
          "time": datetime.now(),
          "sent_by_me": False
      }
  friend[sender]['chat'].append(new_chat)
  print "Your secret message has been saved!"
  print   friend[sender]['chat']





def send_message():
    friend_choice = select_a_friend()
    original_image = input("What is the name of the image?")
    output_path = 'output.jpg'
    text = input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friend[friend_choice]['chat'].append(new_chat)
    print "Your secret message is ready!"







def select_a_friend():
    x=1
    for friends in friend:
        print '%d %s' %(x,friends['name'])
        x=x+1
    choice=input("Select your friend")
    return choice-1

def add_friend():


    new_friend={
        'name':'',
        'salutation':'',
        'age':0,
        'rating':0.0,
        'chat':[]
    }
    new_friend['name'] = raw_input("Please add your friend's name:")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
    new_friend['name'] =new_friend['salutation']+ " " +  new_friend['name']
    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")
    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friend.append(new_friend)
        print "FRIEND ADDED"
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friend)


def start_chat(spy_name,spy_age,spy_rating):
    show_menu = True
    current_status_message = None
    while show_menu :
        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3.send message \n 4.read message"
        menu_choice = input(menu_choices)

        if menu_choice == 1:
            current_status_message=add_status(current_status_message)
        elif menu_choice == 2:
            number_of_friends = add_friend()
            print 'You have %d friends' % (number_of_friends)
        elif menu_choice== 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        else:
            print  'Exiting'
            show_menu = False

def add_status(current_status_message):
    STATUS_MESSAGES = ['My name is Bond', 'James Bond', 'Shaken', 'not stirred.']
    if current_status_message != None:
        print "your current status message is %s \n" %(current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
            print STATUS_MESSAGES
    elif default.upper()=='Y':
        item_position=1
        for temprorary_status in STATUS_MESSAGES:
            print ("%d %s") %(item_position,temprorary_status)
            item_position=item_position+1
        message_selection=input("ENTER YOUR CHOICE")
        if message_selection <= len(STATUS_MESSAGES):
            updated_status_message = STATUS_MESSAGES[message_selection-1]
    return updated_status_message


print 'Let\'s get started'
question = "Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)?"
existing = raw_input(question)

if (existing == "Y"):
    print "Welcome %s %s with rating %.2f" %(spy['salutation'],spy['name'],spy['rating'])
    start_chat(spy['name'], spy['age'], spy['rating'])

else:

    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }
    name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(name) >0 :
        print 'Welcome ' + name + '. Glad to have you back with us.'
        spy['salutation'] = raw_input("choose your salutation Mr./Mrs")
        spy['name'] = spy['salutation'] + " " + name
        print "Alright " + spy['name'] + '.I\'d ;ike to know a little bit more about ...'
        spy['age'] = 0
        spy['rating'] = 0.0
        spy['isonline'] = False

        spy['age'] = input("What is your age?")
        if spy['age']> 12 and spy['age'] < 50:
            spy['rating'] = input("What is your spy rating?")
            if spy['rating']> 4.5:
                print 'Great ace!'
            elif spy['rating'] > 3.5 and spy['rating'] <= 4.5:
                print 'You are one of the good ones.'
            elif spy['rating']>= 2.5 and spy['rating'] <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'
            spy['is_online'] = True
            print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(spy['rating']) + " Proud to have you onboard"
            start_chat(spy['name'], spy['age'], spy['rating'])
        else:
            print 'Sorry you are not of the correct age to be a spy'

    else:
        print "A spy needs to have a valid name. Try again please."




