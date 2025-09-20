# Taking inputs into a list 

n=int(input("Enter the number of elements: ")) 
lst =[] 

for i in range(n):
    l = int(input("Enter the element: ")) 
    lst.append(l) 

print("The list is: ", lst)