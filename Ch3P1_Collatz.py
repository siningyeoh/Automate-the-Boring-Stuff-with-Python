def collatz(number):
    print (number)
    while int(number)>1:
        if int(number)%2==0:
            number=int(number)//2
        elif int(number)%2==1:
            number=3*int(number)+1
        print (number)

print ('Please type a number.')
collatz(input())
