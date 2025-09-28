sum = float(0)
n=5

for i in range (n):
    num = float(input("What is the next number?\n"))
    sum = sum + num
    i += 1
    

print(f"Sum = {sum} ")
print(f"Average = {sum/5}")