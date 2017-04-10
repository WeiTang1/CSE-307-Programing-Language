variable =1
print ("before variable", variable)

def alex():
    global variable
    variable = 2

alex()
print (variable)