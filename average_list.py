#here is how to calculate using while statement

total=0
count=0
while True:
    inp=input('Enter a number:')
    if inp=='done':
        break
    value=float(inp)
    total=total+value
    count=count+1 

average=total/count 
print('Average:',average)

#here is how to calculate using list

numlist=list() #creates an empty list
while True:
    inp=input('Enter a number:')
    if inp=='done':
        break
    value=float(inp)
    numlist.append(value)
average2=sum(numlist)/len(numlist)
print('Average:',average2)