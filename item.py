# Make a class called Item. Objects of this class should have the following attributes:
# A timestamp of when they were created.
# A boolean marking the item as completed or not.
# And the text of the actual to-do item.

class Item(object):
    # When something is inserted into the text file it should throw the date everytime
    #import datetime

with open("scr.txt", mode='a') as file:
    file.write('Printed string %s recorded at %s.\n' %
               (scr, datetime.datetime.now()))

from datetime import datetime
with open('todos.txt', 'a') as main:
    main.write('Printed string %s. Recorded at: %s\n' % scr %datetime.now())


from tabulate import tabulate
outputList = dictOfOutputs.items()
table = outputList
print tabulate(table)

f = open('table.txt', 'w')
f.write(tabulate(table))
f.close()
