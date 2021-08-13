class Cart():
    # Creating a shopping cart using classes
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items

    # Method that shows items already selected
    def currentCart(self):
        print("Here is what you have already grabbed: ")
        for item in self.items:
            print (item)

    # Add items to your cart
    def tossItemIn(self):
        snackos = input("What do we need to throw in the cart? ('back' moves you to previous menu, 'exit' to quit)")
        if snackos == 'exit':
            for item in self.items:
                print(item)
                print("Hopefully we didn't forget something this time.")
                break
        else:
            self.items.append(snackos)

    # Remove items from the cart
    def putItBack(self):
        decadence = input("What did Bailey tell you to put back?")
        if decadence == 'exit':
            for item in self.items:
                print(item)
                print("Hopefully we didn't forget something this time.")
                break
        else:
            self.items.remove(decadence)


bdoubleE_doubleR_un = Cart(15, [])

#Defining a function to run the Cart()
def run():
    while True:
        response = input("What would you like to do? (add/remove/view list/exit)")

        if response.lower() == 'exit':
            bdoubleE_doubleR_un.currentCart()
            print("IT'S BEER O'CLOCK SOMEWHERE!")
            break
        elif response.lower() == 'add':
            bdoubleE_doubleR_un.tossItemIn()

        elif response.lower() == 'remove':
            bdoubleE_doubleR_un.putItBack()
        
        elif response.lower() == 'view list':
            bdoubleE_doubleR_un.currentCart()
        


run()
