A = int(input("Enter a number A:"))
B = int(input("Enter a number B:"))
C = int(input("Enter a number C:"))

if (A==B==C): #A=10, B=10, C=10
    print("All numbers are equal")
    
#NORMAL CODE(MORE SPACE COMPLEXITY)

# elif(A>B and B>C or A>C and C>B): #
#     print("A is greater than both B and C") 
# elif(B>A and B>C or B>C and C>A): #
#     print("B is greater than both A and C") 
# elif(C>B >A or C>A >B):
#     print("C is greater than both B and A") 
# elif(A==B >C): #
#     print("Both A and B are equal and greater than C") constant linear log exponential quadratic nlogn
# elif(A==B <C): #
#     print("Both A and B are equal and less than C")
# elif(B==C >A): #
#     print("B and C are equal and greater than A")
# elif(B==C <A): #
#     print("B and C are equal and less than A")
# elif(A==C >B): #
#     print("Both A and C are equal and greater than B")
# elif(A==C <B):
#     print("Both A and C are equal and less than B")  6>5,6<8

#(LESS SPACE COMPLEXITY)

if A>B:
    if A>C:
        print("A is the greatest")
    else:
        print("C is the greatest")
elif B>A:
    if B>C:
        print("B is the greatest")
    else:
        print("C is the greatest")
elif C>A:
    if B>C:
        print("B is the greatest")
    else:
        print("C is the greatest")
elif A==B:
    if A>C:
        print("A and B are equal and greater than C")
    else:
        print("A and B are equal and less than C")
elif A==C:
    if A>B:
        print("A and C are equal and greater than B")
    else:
        print("A and C are equal and less than B")
elif B==C:
    if B>A:
        print("B and C are equal and greater than A")
    else:
        print("B and C are equal and less than A")
