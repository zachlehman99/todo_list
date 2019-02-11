# Make a class called Manager. A single object of this class should be created when you run your script. It should do the following:
# Print all of the to-do items in the list.
# Add a new item to the list.
# Mark an item as completed.
import item

class Manager(object):

    def to_do_list():
        lists = open("todos.txt", "r")
        print(lists.readlines())
        next = str(lists.readlines())
        next.split(',')
        lists.close()

    def add():
        lists = open("todos.txt", "a")
        task = input('What is your todo? Time and Item? ')
        next = print(lists.write(task)), item.Item.mark_item(), lists.write('\n'), item.Item.time()
        lists.close()

    def completed():
        finished = input('What did you complete? ')
        lists = open("todos.txt", "a")
        print(lists.write(finished + ' completed' + '\n')), item.Item.time()
        lists.close()


def start():
    print("""Which one do you want?
             1. See the to-do list
             2. Add to the to-do list
             3. Change status of completion
             4. Exit
             5. Stored Text
             """)

    beginning = input('-> ')

    if beginning == '1':
        return Manager.to_do_list()
    elif beginning == '2':
        return Manager.add()
    elif beginning == '3':
        return Manager.completed()
    elif beginning == '4':
        print('Have a great day!')
        exit(0)
    elif beginning == '5':
        return item.Item.store_text()
    else:
        print('What was that?')
