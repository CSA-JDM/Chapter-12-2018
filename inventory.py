# Jacob Meadows
# Computer Programming, 4th Period
# February 28th, 2018
"""
Create a dictionary 'inventory'
In the inventory have 4 different fruits (add them however you want)
Give values of course to those fruits
Have on function that asks the user how many to remove from the inventory, and then do so and print the resulting value.
Example:
What item do you need to change: [apples]
How many to remove: [10]
You now have 40 apples
"""
inventory = {
        "apples": 4,
        "bananas": 8,
        "oranges": 3,
        "grapes": 7
    }  # Predefined dictionary


def inventory_py(inv):  # Main function
    x = input("What item do you need to change: ")  # Asks user for one of the keys of the inventory dictionary
    if x not in inv:  # Checks if the input was a key of the dictionary
        print("This item is not in the inventory, please try again.")
        inventory_py(inv)
    x2 = input("How many to remove: ")  # Asks the user how many they wish to remove
    inv[x] = inv[x] - int(x2)  # Removes the requested amount
    print("You now have %s %s" % (inv[x], x))  # Tells the user the subtracted amount
    inventory_py(inv)


inventory_py(inventory)  # Runs the main function
