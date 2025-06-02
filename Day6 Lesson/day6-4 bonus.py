contents = ['hello', 'world', 'python']

filenames = ['doc1.txt', 'doc2.txt', 'doc3.txt']

# zip function is used to combine two lists for the for loop
for content, filename in zip(contents, filenames):
    
    # file = open(f"Day6 Lesson/day6 bonus/{filename}", 'w')
    # file = open("Day6 Lesson/day6 bonus/"+filename, 'w')
    # file = open(f"day6 bonus/{filename}", 'w')
    
    # if the target folder is not in the same folder as the python file and outside of the folder use ../
    file = open(f"../testing/{filename}", 'w')
    
    file.write(content)
    file.close()
    
print(zip(contents, filenames))

print(list(zip(contents, filenames)))
# [('hello', 'doc1.txt'), ('world', 'doc2.txt'), ('python', 'doc3.txt')]

x = "lorem ipsum dolor" \
    "sit amet consectetur" \
    "adipiscing elit"
print(x)