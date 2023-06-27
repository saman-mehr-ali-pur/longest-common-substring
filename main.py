import algorithm as algo
import os
path1 = input("please enter the absolute path first DNA: \n")
path2 = input("please enter the absolute path second DNA: \n")
file1 = None
file2 = None
resultFile = None

while(True):
    try:
        file1 = open(path1,'r')
        break
    except FileNotFoundError:
        print("not found such this file in "+path1)
        
while(True):
    try:
        file2 = open(path2,'r')
        break
    except FileNotFoundError:
        print("not found such this file in "+path2)

DNA1 = file1.readline()
DNA2 = file2.readline()
print(DNA1)
print(DNA2)
commen_string = algo.LCSuff(DNA1,DNA2)
if (not os.path.exists("result")):
    os.mkdir("result")


resultFile = open("result/result.txt",'w')
print(commen_string)
resultFile.write(commen_string)



