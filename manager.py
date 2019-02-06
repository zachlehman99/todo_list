# Make a class called Manager. A single object of this class should be created when you run your script. It should do the following:
# Print all of the to-do items in the list.
# Add a new item to the list.
# Mark an item as completed.
# f = open("todos.txt", "r")
# print(f.read('zach'))
class Manager(object):

    # The skeleton of the manager
    def __init__(self, list, completed):
        self.list = list
        self.completed = completed

    # This so the file can be read through the terminal
    def to_do_list():
        lists = open("todos.txt", "r")
        print(lists.read())

    # They add it through the terminal and the input goes into the text file through the input
    #
    def add():
        lists = open("todos.txt", "a")
        f = input('-> ')
        print(lists.write(f))

    def completed(self):
        lists = open("todos.txt", "a")
        print(lists)


def start():
    print("""Which one do you want?
             1. See the to-do list
             2. Add to the to-do list
             3. Change status of completion
             """)

    beginning = input('-> ')

    if beginning == '1':
        return Manager.to_do_list()
    elif beginning == '2':
        return Manager.add()
    elif beginning == '3':
        return Manager.to_do_list()
