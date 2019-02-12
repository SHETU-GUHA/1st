'''birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
       print('Enter a name: (blank to quit)')
       name = input()
       if name == '':
           break

     if name in birthdays:
         print(birthdays[name] + ' is the birthday of ' + name)
     else:
           print('I do not have birthday information for ' + name)
           print('What is their birthday?')
           bday = input()
         birthdays[name] = bday
           print('Birthday database updated.')'''

###
           
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):    
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(stuff.get(k, 0)) + ' ' + k)

    print("Total number of items: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inv.setdefault(addedItems[i], 0)
        inv[addedItems[i]] = inv[addedItems[i]] + 1

    return inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

###
1.{}
2. {'foo':42}
3.items stored in dictionary are unordered bt in list items stored are ordered way.
4. key Error
5.
6.
7.spam.setdefault('color','black')
8.
