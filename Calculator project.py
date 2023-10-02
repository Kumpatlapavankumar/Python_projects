import random
Name=input("enter a name:")
print("{},guess any number from 1 to 100 i will tell you")
min=1
max=100
randomnumber=random.randint(min,max)
result="no"
count=1
while(result=='no'):
    print("{} this number is correct or not(correct for yes wrong for no)".format(randomnumber))
    result=input()
    if(result=="yes"):
        print("Hey,{} this is your number".format(randomnumber))
    else:
        count=count+1
        print("number is greater than {} or less than {}(enter greater or less)".format(randomnumber,randomnumber))
        greaterorless=input()
        if(greaterorless=="greater"):
            min=randomnumber+1
            randomnumber=random.randint(min,max)
        else:
            max=randomnumber-1
            randomnumber=random.randint(min,max)
print("I guessed this number {} in  on {} chances".format(randomnumber,count))
