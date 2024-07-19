#start

iq: int = 0
sum: int = 0;
count: int = 0;

iq = int(input("what is your iq?"))

while iq < 30 or iq > 300:
    sum = sum + iq;
    count = count + 1
    iq = int(input("what is your iq?"))

avg: float = sum / count
print(f"the average at the beginning of the year is: {avg}")
print("")

#After a year
newiq: int = 0;
newsum: int = 0;
newcount: int = 0;

print("one year of python has been completed")

newiq = int(input("please enter your new iq:"))

while newiq < 30 or newiq > 300:
    newsum = newsum + newiq ;
    newcount = newcount + 1
    newiq = int(input("please enter your new ip:"))

newavg: float = newsum / newcount
print(f"the average at the end of the year is: {newavg}")

dif: float = newavg - avg
print(f"the average increased at the end of the year by: {dif}")


#end