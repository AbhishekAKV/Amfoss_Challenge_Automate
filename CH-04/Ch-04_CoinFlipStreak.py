import random 
numberOfStreaks=0
list=[]
streak=0
for experimentNumber in range(10000):
    ran=random.randint(0,1)
    if ran==0:
        list.append('H')
    else:
        list.append('T')
    
for head_tail in range(len(list)-5):
    if list[head_tail]==list[head_tail+1]==list[head_tail+2]==list[head_tail+3]==list[head_tail+4]==list[head_tail+5]:
        numberOfStreaks+=1
    else:
        continue
print('Chance of streak: %s%%' % (numberOfStreaks / 100))