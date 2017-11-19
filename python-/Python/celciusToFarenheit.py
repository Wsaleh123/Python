#Multiply by 9, then divide by 5, then add 32

temperatures = [10, -20, -289, 100]

file = open("example.txt", "a+")

def cel_to_far(cel):
    if cel < -273.15:
        return "That doesn't make sense"
    else:
        far = ((cel * 9)/5)+32
        file.write(str(far) + "\n")
        return far

for i in temperatures:
    print(cel_to_far(i))
file.close()

print("-"*10)

money = {"saving_account": 200, "checking_account":100, "under_bed":[500, 10, 100]}

print(money["under_bed"][1])
