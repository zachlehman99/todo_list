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
        lists = open("todos.txt", "r+")
        lines = lists.readlines()
        reading = input("What do you want to mark complete? What Todo? ")
        str(lines.endswith(reading))
        lists.write(reading.strip('Not')).replace
        lists.close()

# lists.endswith(reading)
# For 1st line. print(lists[stripper])



def start():
    print("""Which one do you want?
             1. See the to-do list
             2. Add to the to-do list
             3. Change status of completion
             4. Finished with a todo
             5. Exit
             6. Stored Text
             """)

    beginning = input('-> ')

    if beginning == '1':
        return Manager.to_do_list()
    elif beginning == '2':
        return Manager.add()
    elif beginning == '3':
        return Manager.completed()
    elif beginning == '4':
        finished = input('What did you complete? ')
        lists = open("todos.txt", "a")
        print(lists.write(finished + ' completed' + '\n')), item.Item.time()
        lists.close()
    elif beginning == '5':
        print('Have a great day!')
        exit(0)
    elif beginning == '6':
        return item.Item.store_text()
    else:
        print('What was that?')

# readline(): It returns the entire line from the file. line = f.readline()
# readlines(): It returns a List containing all lines. lines = f.readlines() print(lines[0]) → For 1st line. print(lines[1]) → For 2nd line (assuming that the file has multiple lines)
