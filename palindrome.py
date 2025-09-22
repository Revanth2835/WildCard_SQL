n=input("Enter a Word: ") 
n_p=n[::-1]
if n==n_p:
    print("Palindrome")
else:
    print("Not Palindrome")