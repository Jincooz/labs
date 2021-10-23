import os

def dprint(string):
    global outfile
    print(string)
    outfile.write(string)
    pass

def main():
    with open('labsCM\Lab2\Input.txt', 'r') as infile:
        matrix = [[float(element) for element in line.replace('\n','').split(' ')] for line in infile.readlines()]
    if(matrix.__len__() + 1 != matrix[0].__len__()):
        dprint("Error, with input data")
        return
    vector = []
    for row in matrix:
        vector.append(row.pop(-1))        
    print(vector)
    print(matrix)
    


os.remove('labsCM\Lab2\Console.txt')
with open('labsCM\Lab2\Console.txt', 'w') as outfile:
    main()