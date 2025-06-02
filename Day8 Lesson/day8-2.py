with open('files/mytext.txt', 'r') as file:
    content = file.read()
    print(content)
    
with open('../testing/mytext.txt', 'r') as file:
    content = file.read()
    print(content)
    

print()

# this will run without 'r' because it is the default mode
with open('files/mytext.txt') as file:
    content = file.read()
    print(content)

print()

with open('files/mytext.txt') as file:
    content = file.read()
    content2 = file.read()
    print(content, "this is content1")
    
    print()
    
    # this will print nothing because the file pointer is at the end of the file
    print(content2, "this is content2")