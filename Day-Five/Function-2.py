# this asterisk is showing that we're passing various amounts like a tuple, 
# a tuple  of which is like a list of values were passing in here 
# which is we dont know how many it's passing

def greetings_function(*name):
    
    print("Hello "+ name[1])


greetings_function("Richard" , "John" , "Tim")