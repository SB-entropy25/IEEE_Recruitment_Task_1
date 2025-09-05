#I have made code more user friendly by asking user himself to enter the values for list 1 and lsit2
#then I print the list1 and list2 independently
#then I print the intersection values of list1 and list 2
p=input("Enter list 1 values seperated by spaces only:") #input from user for list1 values seperated by spaces only no commas
q=input("Enter list 2 values seperated by spaces only:")#similarly for list2
list1=[]
list2=[]
num=""
num2=""
p=p+" "
#here i store the values recived into list1(My own thinking no chatgpt used)
for k in p:
    if k!=" ":
        num2=num2+k
   
    else:
        list1.append(int(num2))
        num2=""
#here i store the values recived into list2 (My own thinking no chatgpt used)
q=q+" "
for m in q:
    if m!=" ":
        num=num+m
   
    else:
        list2.append(int(num))
        num=""
print("list1:",list1)
print("list2:",list2)
intersection = list(set(list1) & set(list2))
intersection.sort()
print(intersection)