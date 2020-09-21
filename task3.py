commandCount = int(input("command count\n"))
array = []
for value in range(commandCount):
    # Splits a string into parts using a separator (if empty used space)
    commandsArray = input().split()
    # Checking command name by 0 index
    if commandsArray[0] == "insert":
        if len(commandsArray) == 3:
            # Transfer data from one array to another
            array.insert(int(commandsArray[1]), int(commandsArray[2]))
    if commandsArray[0] == "remove":
        array.remove(int(commandsArray[1]))
    if commandsArray[0] == "print":
        print(array)
    if commandsArray[0] == "append":
        array.append(int(commandsArray[1]))
    if commandsArray[0] == "sort":
        array.sort()
    if commandsArray[0] == "pop":
        array.pop()
    if commandsArray[0] == "reverse":
        array.reverse()