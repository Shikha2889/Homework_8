import os
directory_path = os.getcwd()

for x in os.listdir(directory_path):
    line_no = 1
    if x.endswith(".py"):
        
        fo = open(directory_path +"/"+ x)
        line = fo.readline()
    
        #initialise the counter
    
        while line != '':
            index = line.find('Lecture')
            if(index!=-1):
                print(x)
            line = fo.readline()
            line_no+=1
        fo.close()