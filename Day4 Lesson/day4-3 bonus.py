
filenames = ['1.something.txt', '2.whatever.txt', '3.maybe.txt']

for filename in filenames:
    
    # replace("original", "new", how many times)
    filename = filename.replace('.', '-', 1)
    print(filename)

print(filenames)

print()


x = ('aaa', 'bbb', 'ccc')

print(x)
print(type(x))

# can't reassign the values in tuple, cuz tuple is immutable
# x[1] = "ok" (this will cause error)

print(x)
