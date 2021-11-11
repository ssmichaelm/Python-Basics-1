# Michael Moreland - Smoothstack, Python Basics 1; 11/10/2021
import array

# 1. Add two numbers 50 + 50 and 100 - 10, and print it
print("Part 1")
print(50+50)
print(100-10)

# 2. See if each expression returns 36
print("\nPart 2")
arr = array.array("i", (30+6, 6^6, 6**6, 6+6+6+6+6+6))
for arrvalue in arr:
    print(arrvalue)

# 3. Print “Hello World” on the console output. Print output “Hello World : 10” Make sure capitalization and spacing matches.
print("\nPart 3")
helloworld = {"Hello World" : 10}
print([key for key in helloworld.keys()][0])
for key, value in helloworld.items():
    print(key, ' : ', value)

# 4. Math problem
print("\nPart 4")
p, r, l =  [ int(i) for i in input("Please input your P-, R-, and L-values: ").split() ]

def get_m(p, r, l):
    r = r/100/12
    numerator = p*r*(1+r)**l
    denominator = ((1+r)**l - 1)
    m = numerator / denominator

    return int(m + (m % 1 > 0)) # Round up and return

print(get_m(p, r, l))

