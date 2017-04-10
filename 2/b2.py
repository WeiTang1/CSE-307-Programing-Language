import sys

def CalculateFun(num, token, cap, refill, currentfun, funList, totalfun,counter):
    if num > 0:
        currentfun = currentfun + funList[counter]
        print(currentfun)
        CalculateFun(num-1,token,cap,refill,currentfun,funList,totalfun,counter+1)
        print(currentfun)
    if num == 1:
        totalfun.append(currentfun)
        return;



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



print ("num = ",num,"cap= ",cap,"refill =", refill,"fun = ",funList)
f.close();
totalfun = []
token = cap
CalculateFun(num,token,cap,refill,0,funList,totalfun,0)
print(totalfun)
