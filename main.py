import math
#variables are a container for values.
#Python has : string, bool, int , float


#typecasting is done using str(), float(), int(), bool()

#type() is used to get the type of variable

a = 3.55
print(int(a))
#decimal is removed no ceil or floor fn

a=0
b="False"
print(bool(a))
#empty string is false
print(bool(b))

#input

#easy validations:
def inputvalidate():
    while True:
        try:
            name = input("What is your name? :")
            float(name)
        except ValueError:
            break
        else:
            continue

    while True:
        try:
            age = input(f"Hi {name}, How old are you? : ")
            int(age)
        except ValueError:
            continue
        else:
            if int(age) > 0:
                break
            else:
                continue

#inputvalidate()

print(math.ceil(3.11))
print(math.floor(3.11))
print(abs(-3.11))
print(abs(3.11))

print(math.pi)
print(math.e)

print(math.pow(5,3))

# r =  float(input("Enter radius:"))
# print(f"Area is {math.pi * r * r}cm^2")


# mystr = input("Enter a string:")
mystr = "lollipop"
print(len(mystr))

#for finding occurence of sub-string in a string
# not found means -1, else index
#first occurence
print(mystr.find("l"))
#last occurrence
print(mystr.rfind("l"))

print(mystr.find("z"))
print(mystr.rfind("u"))

print(mystr.isdigit())
print(mystr.isalpha())

print(mystr.count("l"))

# print(help(str))

#indexing [start:end:step]

sentence = "yummy yummy in my tummy!"
print(sentence[0])
print(sentence[-1])
print(sentence[:5])
print(sentence[::2])
#String reversal using indexing
print(sentence[::-1])

array= [1,2,3,4,5,6,7]
print(array[0])
print(array[-1])
print(array[:5])
print(array[::2])
#String reversal using indexing
print(array[::-1])

#format specifiers for printing outputs

#<,> are used to left or right justify the values with added padding.
#'no. of decimals'f for precision.
#+ for explicitly showing +ve values
#^ centering

price1 = 111.999
price2 = 22.12
price3 = 1.992
price4 = -49
total = price1 + price2 + price3 + price4

print("\nUnformatted mess:\n")
print(f"Price1: ${price1}")
print(f"Price2: ${price2}")
print(f"Price3: ${price3}")
print(f"Price4: ${price4}")
print(f"total : ${total}")

print("\n\nFormatted bliss:\n\n")
print(f"Price1: ${price1:>10,.2f}")
print(f"Price2: ${price2:>10,.2f}")
print(f"Price3: ${price3:>10,.2f}")
print(f"Price4: ${price4:>10,.2f}")
print("----------------------------")
print(f"total : ${total:>10,.2f}")
