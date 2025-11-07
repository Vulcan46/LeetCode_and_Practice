principle = 0
rate = 0
time = 0

while principle<=0:
   principle = float(input("Enter Princple amount"))
   if principle<=0:
       print("Re-enter +ve number")

while time<=0:
   time = float(input("Enter time amount"))
   if time<=0:
       print("Re-enter +ve number")

while rate<=0:
   rate = float(input("Enter rate amount"))
   if rate<=0:
       print("Re-enter +ve number")

total =  principle*(pow((1+rate/100),time))

print(f"Total balance:{total}")