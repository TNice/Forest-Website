try:
    f = open("uploads/test.txt")
    f.read()
    for line in f:
        print(line)
    
finally:
    f.close()
