number = (1,2,3,4,5,6,7,8,9)

count_even=0
count_odd=0
for i in number:
    if(i%2==0):
        count_even+=1
    else:
        count_odd+=1
print("number of even numbers:",count_even)
print("number of odd numbers:",count_odd)