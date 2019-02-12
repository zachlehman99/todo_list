# Make a class called Item. Objects of this class should have the following attributes:
# A timestamp of when they were created.
# A boolean marking the item as completed or not.
# And the text of the actual to-do item.
import datetime
import manager

class Item(object):

    def time():
        with open("todos.txt", 'a') as now_time:
            return now_time.write(str(datetime.datetime.now())), now_time.write(' ')
            now_time.close()

    def mark_item():
        lists = open("todos.txt", "a")
        print(lists.write('Not completed '))
        lists.close()

    def store_text():
        lists = open("todos.txt", "r")
        print(lists.read())
        lists.close()

    def delete_everything():
        goodbye = input('Are you sure you want everything deleted? Ctrl c if you do not. ')
        lists = open("todos.txt", "r+")
        lists.truncate(0)
        lists.close()

    def mark_something():
        finished = input('What activity did you complete? ')
        lists = open("todos.txt", "a")
        print(lists.write(finished + ' completed' + '\n')), Item.time()
        lists.close()

    def get_rid(text):
        lists = open("todos.txt", "r+")
        file_text = lists.readlines()
        lists.seek(0)
        for i in file_text:
            if not text in i:
                lists.write(i)
        lists.truncate()
        lists.close()
