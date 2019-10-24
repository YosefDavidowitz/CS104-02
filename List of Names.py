names  = []


i = 0
while i < 10:
    names.append (input("Enter a name:"))
    i+=1

searching = True
while searching == True:
    search = input("Enter a name to search for or 'End' to end the program:")
    if "End" in search:
        break
    if search in names:
        print("The name was found")
    else:
        print ("The name was not found")
