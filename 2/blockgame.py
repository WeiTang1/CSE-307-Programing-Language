import sys

def CalculateFun(num, token, cap, refill, currentfun, funList, totalfun,counter):
    tempfun = currentfun
    temptoken = token
    # base cases
    if token < 0:
        print("No more token and current fun = ",currentfun)
        return totalfun.append(currentfun)
    if num==0:
        print(" No more game to play currentfun = ",currentfun)
        return totalfun.append(currentfun)
    for i in range(1,token+1):
        currentfun = tempfun + i * funList[counter]
        token = temptoken - i + refill
        if token > cap :
            token = cap
        print("play game ", counter+1 ,i,"times","token left",token)

        CalculateFun(num-1,token,cap,refill,currentfun,funList,totalfun,counter+1)


# open file and parse input
f = open(str(sys.argv[1]))
num = int(f.readline()[4:5])
cap = int(f.readline()[4:5])
refill = int(f.readline()[7:8])
line = f.readline()
funList=[]
while line:
    if line[6:7]=='-':
        funList.append(int(line[6:8]))
    else:
        funList.append(int(line[6:7]))
    line = f.readline()


# print input
print ("num = ",num,"cap= ",cap,"refill =", refill,"fun = ",funList)
f.close();
totalfun = []
token = cap
CalculateFun(num,token,cap,refill,0,funList,totalfun,0)
# print all possible funs
print(totalfun);
print("total_fun(",max(totalfun),")")
