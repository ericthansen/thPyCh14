def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if name == 'main': 
    print(linecount('wc.py'))
#print(linecount('wc.py'))
