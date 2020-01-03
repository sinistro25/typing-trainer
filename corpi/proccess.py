import unidecode
with open("names.txt", "r") as file:
    w = open("p.txt",'w')
    line = file.readline()
    while line != "":
        line = line.split()
        print(line)
        w.write(unidecode.unidecode(line[1]) + "\n")
        w.write(unidecode.unidecode(line[2]) + "\n")
        line = file.readline()
    file.close()
    w.close()