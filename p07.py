import sys
import math
def makeHeader(cols):
    reps = math.floor(cols / 16)
    string1 = "XX:"
    count = 0
    for i in range(reps):
        if(count == 0):
            string1 += " "*16
        else:
            string1 += str(count)+ " "*15
        #string += string
        count += 1
    #print(string1)
    string2 = "XX:" + "0123456789ABCDEF"*reps
    #print(string2[0:cols+3])
    return string1 + "\n"+ string2
def makeRows(rows, cols):
    rowList = {}
    for i in range(int(rows)):
        if(hex(i)[2:].zfill(2).upper() == "00"):
            #print("triggered")
            rowList[hex(i)[2:].zfill(2).upper()] = "0"+hex(i+1)[2:].zfill(2).upper()+"0"*(int(cols)-3)
        elif(i == int(rows)-1):
            rowList[hex(i)[2:].zfill(2).upper()] = "1"+hex(0)[2:].zfill(2).upper()+"0"*(int(cols)-3)
        else:
            rowList[hex(i)[2:].zfill(2).upper()] = "1"+hex(i+1)[2:].zfill(2).upper()+"0"*(int(cols)-3)
    return rowList




if(__name__ == "__main__"):
    name=sys.argv[1]
    rows=int(sys.argv[2])
    cols=int(sys.argv[3])
    header = makeHeader(cols)
    rows = makeRows(rows,cols)
    #print(header)

    f= open(name+".txt","w+")
    f.write(header + "\n")
    for thing in rows:
        f.write(thing+":"+rows[thing] + "\n")
    print("done!")
    f.close()


