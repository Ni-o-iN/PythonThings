with open('FileIO', 'r') as datei:
    my_string = datei.read().split()
    längste = max(my_string, key=len)
    print(längste)