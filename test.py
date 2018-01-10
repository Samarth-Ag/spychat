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