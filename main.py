from spy_details import spy_name, spy_salutation, spy_age, spy_rating


friend_name=[]
friend_age=[]
friend_is_online=[]
friend_rating=[]


def add_friend():
    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    new_name = new_name + " " + new_salutation
    new_age = input("Age?")
    new_rating = input("Spy rating?")
    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friend_name.append(new_name)
        friend_age.append(new_age)
        friend_is_online.append(True)
        friend_rating.append(new_rating)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friend_name)


def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    current_status_message = None
    while show_menu :
        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend"
        menu_choice = input(menu_choices)

        if menu_choice == 1:
            current_status_message=add_status(current_status_message)
        elif menu_choice == 2:
            number_of_friends = add_friend()
            print 'You have %d friends' % (number_of_friends)
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


'Let\'s get started'
question = "Continue as " + spy_salutation + " " + spy_name + "(Y/N)?"
existing = raw_input(question)

if (existing == "Y"):
    print "Welcome %s %s with rating %.2f" %(spy_salutation,spy_name,spy_rating)
    start_chat(spy_name, spy_age, spy_rating)

else:
    name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(name) >0 :
        print 'Welcome ' + name + '. Glad to have you back with us.'
        spy_salutation = raw_input("choose your salutation Mr./Mrs")
        spy_name = spy_salutation + " " + name
        print "Alright " + spy_name + '.I\'d ;ike to know a little bit more about ...'
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False

        spy_age = input("What is your age?")
        if spy_age > 12 and spy_age < 50:
            spy_rating = input("What is your spy rating?")
            if spy_rating > 4.5:
                print 'Great ace!'
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'
            spy_is_online = True
            print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
            start_chat(spy_name, spy_age, spy_rating)
        else:
            print 'Sorry you are not of the correct age to be a spy'

    else:
        print "A spy needs to have a valid name. Try again please."




