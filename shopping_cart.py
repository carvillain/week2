# from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def shopping_cart():
    """Function that builds a virtual shopping cart where the customer
        can add items, remove items, and print their list."""
    
    cart = {}
    action = input("What would you like to do? (add/remove/view list/exit)")
    action = action.lower()
    
    while True:

        if action == 'exit':
            print(cart)
            break
            # clear_output()
        elif action == 'add':
            new_item = input("What do we need to add to the list? ('back' moves you to previous menu, 'exit' to quit)")
            new_item = new_item.lower()
            if new_item == 'back':
                action = input("What would you like to do? (add/remove/view list/exit)")
            elif new_item == 'exit':
                print(cart)
                break
            else:
                cost = input("What is the price?")
                cart[new_item] = cost
                # cart.append(new_item)
        elif action == 'remove':
            del_item = input("What do we need to remove from the list? ('back' moves you to previous menu, 'exit' to quit)")
            del_item = del_item.lower()
            if del_item == 'back':
                action = input("What would you like to do? (add/remove/view list/exit)")
            elif del_item == 'exit':
                print(cart)
                break
            else:
                # cart.remove(del_item)
                item_1 = del_item
                del cart[item_1]

        elif action == 'view list':
            print(cart)
            action = input("What would you like to do? (add/remove/view list/exit)")
        else:
            action = input("Uknown entry. Please try again (add/remove/view list/exit) ")

            

shopping_cart()