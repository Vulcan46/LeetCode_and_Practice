veggies = ["tomatoes","onions","cabbage","green peppers","chillies","spinach", "potatoes","eggplant"]
meats = ["fish","chicken","lamb","mutton","crab"]
cost_v = [0.68, 0.8,2.43,0.98,0.5,3.44,3,5]
cost_m = [10,8,19,15,13]
cost_veggie={}
cost_meats={}
i,j=0,0
for veggie in veggies:
    cost_veggie[veggie]=cost_v[i]
    i+=1
for meat in meats:
    cost_meats[meat]=cost_m[j]
    j+=1

buylist=[]
cost = 0.0
while True:
    item = input("What do you want to buy? enter 'x' to calculate final bill:")
    if item in veggies:
        buylist.append(item)
        cost += cost_veggie[item]
    elif item in meats:
        buylist.append(item)
        cost += cost_meats[item]
    elif item == "x":
        break
    else:
        print(":( Sorry we do not have that.")

print("\nToday you bought:\n")
for item in buylist:
    print(f"{item}\n")
print(f"Thank You for shopping with us!\n Your total is: ${cost + cost * 0.1:.2f}")