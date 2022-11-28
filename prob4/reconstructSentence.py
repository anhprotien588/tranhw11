import sys
f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
flines1= f1.readlines()
flines2= f2.readlines()
list1=[]
list2=[]
out = []
for i in range(len(flines1[0].split())):
    list1.append(flines1[0].split()[i])
for i in range(len(flines2[0].split())):
    list2.append(flines2[0].split()[i])
if len(list1) > len(list2):
    a = list1
    b = list2
else:
    a = list2
    b = list1
count1 = len(a)
count2 = len(b)
while count1 > 0:
    out.append(a[count1-1])
    if not count2 == 0:
        out.append(b[count2-1])
        count2-=1
    count1-=1
space = "\n"
f3=open("output.txt","w")
f3.write(' '.join(out))
f3.write(space)
print("list1 is: ",list1)
print("list1Length: ", len(list1))
print("\n")
print("list2 is: ",list2)
print("list2Length: ", len(list2))
print("\n")
print("The list out is: ",out)
