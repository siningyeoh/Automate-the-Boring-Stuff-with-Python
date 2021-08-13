def addToInventory(inventory, addedItems):
    for item in range(len(addedItems)):
        inventory.setdefault(addedItems[item],0)
        inventory[addedItems[item]] += 1
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
