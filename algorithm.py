

def LCSuff(DNA1,DNA2):
    table1 = [[[] for i in range(len(DNA2)+1)] for j in range(len(DNA1)+1)]
    table2 = [[[] for i in range(len(DNA2)+1)] for j in range(len(DNA1)+1)]
    result =''
    for i in range(len(DNA1)+1):
        for j in range(len(DNA2)+1):

            if (j==0 or i==0):
                table1[i][j] = 0
                table2[i][j]='.' 

            else:
                if ((i>0 and j>0) and (DNA1[i-1]!=DNA2[j-1])):
                    if (table1[i-1][j]>=table1[i][j-1]):
                        table1[i][j] = table1[i-1][j]
                        table2[i][j] = 'u'                  #up arrow ↑ 
                    else:
                        table1[i][j] = table1[i][j-1]
                        table2[i][j] = 'l'                  #left arrow ←
                
                else :
                    table1[i][j] = table1[i-1][j-1]+1
                    table2[i][j] = 'd'                  #Diagonal arrow ↖   


    return find_string(DNA1,DNA2,table1,table2)



def find_string(DNA1,DNA2,table1,table2):            #this method find desired substring 
    j = len(DNA2)
    i = len(DNA1) 
    result =''
    while (i!=0 and j!=0):
        if (table2[i][j]== 'd'):
            result = result + DNA1[i-1]
            i-=1
            j-=1
        elif (table2[i][j] == 'l'):
            j-=1
            continue
        elif(table2[i][j]=='u'):
            i-=1
            continue

    return result[::-1]   


if __name__=="__main__":
    print(LCSuff(DNA2="ABSDHS",DNA1="ABDHSP"))

