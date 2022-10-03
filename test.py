# def shopping_cart():
#     cart = []

#     adding_items = True

#     while adding_items:
#         action = input("Do you want to: Show/Add/Delete or Quit? ")

#         if action.lower() == "show":
#             print(cart)
#         elif action.lower() == "add":
#             new_item = input("What would you like to add?")
#             cart.append(new_item)
#         elif action.lower() == "delete":
#             remove_item = input("What would you like to delete?")
#             cart.remove(remove_item)
#         elif action.lower() == "quit":
#             break
#     print(cart)
 
# shopping_cart()

class cart():
    def __init__(self, grocerylist):
        self.grocerylist = grocerylist

    def add(self):
        self.new_item = str(input("What would you like to add? "))
        self.grocerylist.append(self.new_item)

    def delete(self):
        self.delete_item = str(input("What would you like to delete? "))
        self.grocerylist.remove(self.delete_item)

    def show(self):
        print(self.grocerylist)

s1 = cart([])

def run():
    while True:
        action = input("Do you want to: Show/Add/Delete or Quit? ")
        if action.lower() == "quit":
            reply = input("Are you sure you want to quit? You will lose your cart. Y/N: ")
            if reply.lower() == "y":
                break
            elif reply.lower() == "n":
                continue
            else:
                print("Invalid input, please try again.")
        elif action.lower() == "add":
            s1.add()
        elif action.lower() == "delete":
            s1.delete()
        elif action.lower() == "show":
            s1.show()
        else:
            print("Invalid input, please try again.")


run()