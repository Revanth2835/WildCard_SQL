# dict as a input 

n = int(input("Enter the number of elements: ")) 
dic ={}
for i in  range(n):
    k = input("Enter the key: ") 
    v = int(input("ENter the value for key : "))
    dic[k] = v 
print(dic)