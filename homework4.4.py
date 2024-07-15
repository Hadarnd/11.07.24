#start

for a in range(10,21):
   print(a, end=",");
#_______________________________________________________________________________

for b in range(10,21,2):
   print(b, end=",")

#___________________________________________________________________________________

num: int= int(input("how many gap should I write?"))

for c in range(10,21,num):
   print(c, end=",")

#____________________________________________________________

num1: int = int(input("please enter the start point:"))
num2: int = int(input("please enter the end point:"))
num3: int = int(input("please enter the gap you want:"))

for d in range(num1,num2,num3):
    print(d, end=",")



#end