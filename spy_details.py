from datetime import datetime
from termcolor import colored
class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None


spy = Spy('bond', 'Mr.', 24, 4.7)
friend_one = Spy('Raja', 'Mr.', 27, 4.9)
friend_two = Spy('Mata Hari', 'Ms.', 21, 4.39)
friend_three = Spy('No', 'Dr.', 37, 4.95)
friend = [friend_one, friend_two, friend_three]


class ChatMessage:

  def __init__(self, message,time, sent_by_me):
    self.message = message
    self.time = time
    self.sent_by_me = sent_by_me