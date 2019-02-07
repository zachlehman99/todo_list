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

    def text():
        lists = open("todos.txt", "r")
        close.lists()
