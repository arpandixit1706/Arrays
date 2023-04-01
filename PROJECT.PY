#PROJECT ON ARRAY/LISTS:- FIND NO OF DAYS ABOVE AVERAGE TEMPRATURE


a=int(input("How many days temprature ?"))
total=0
temp=[]
for i in range(a):
    nextday=int(input("The" + str(i+1) + " 's high temprature="))
    temp.append(nextday)
    total+=temp[i]
avg=(total//a)
print("The average temprature is =",avg)
above=0
for i in temp:
    if (i>avg):
        above+=1
print(str(above) +" is the number of days having temprature above average")
