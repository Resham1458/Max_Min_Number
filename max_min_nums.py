total=int(input("How many numbers you want to enter?")) #asks user the total number he/she wants to                                          enter

numbers = [int(input("Enter any whole number:")) for i in range(total)] # lets the user to enter desired number of numbers

print("The list of numbers you entered is:",numbers) #displays list of numbers

print("The largest number you entered is:",max(numbers)) #out puts largest number

print ("The smallest number you entered is:",min(numbers)) #out puts smallest number
