with open("rgb.txt", 'r') as file1:
    clines = file1.readlines()
with open('depth.txt', 'r') as file2:
    plines = file2.readlines()
i=0
with open('associations.txt.txt',"w") as file3:
    for i in range(0,2542):
        line = clines[i].strip() + " "+plines[i]
        file3.write(line)
