# Make a class called Item. Objects of this class should have the following attributes:
# A timestamp of when they were created.
# A boolean marking the item as completed or not.
# And the text of the actual to-do item.
import datetime
import manager

class Item(object):
    # When something is inserted into the text file it should throw the date everytime
    #import datetime

    def time():
        with open("todos.txt", 'a') as now_time:
            if manager.Manager.add() == ' ':
                return ''
            elif manager.Manager.add() == 'exit':
                return exit(0)
            else:
                return now_time.write(str(datetime.datetime.now())), now_time.write('\n')
                now_time.close()
