# Make a class called Manager. A single object of this class should be created when you run your script. It should do the following:
# Print all of the to-do items in the list.
# Add a new item to the list.
# Mark an item as completed.
import item

class Manager(object):

    def to_do_list():
        lists = open("todos.txt", "r")
        print(lists.readlines())
        lists.close()
        return start()

    def add():
        lists = open("todos.txt", "a")
        task = input('What is your todo? Time and Item? ')
        next = print(lists.write(task)), item.Item.mark_item(), lists.write('\n'), item.Item.time()
        lists.close()

    def completed():
        lists = open("todos.txt", "r+")
        reading = lists.read()
        delete_line = input('What did you complete? ')
        if delete_line == '':
            lists.close()
            return start()
        else:
            item.Item.get_rid(delete_line)
            lists.close()
            return start()


def start():
    print("""Which one do you want?
             1. See the todo list
             2. Add to the todo list
             3. Delete a line from the todo list
             4. Exit
             5. Stored Text
             6. Delete Everything
             7. Mark Something Complete
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
    elif beginning == '6':
        return item.Item.delete_everything()
    elif beginning == '7':
        return item.Item.mark_something()
    else:
        print('What was that?')
        return start()
