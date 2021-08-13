class proclaimIt():
    
    def __init__(self, message):
        self.message = message
        
    
    def print_string(self):
        print(self.message)

message = input("What would you like to say?")

hello = proclaimIt(message)

hello.print_string()