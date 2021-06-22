def collatz(number):
    if int(number)%2==0:
        print (int(number)//2)
    if int(number)%2==1:
        print (3*int(number)+1)

print ('Please type a number.')
collatz(input())
