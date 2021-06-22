def collatz(number):
    try:
        if int(number)%2==0:
            print (int(number)//2)
        if int(number)%2==1:
            print (3*int(number)+1)
    except ValueError:
        print ('Please type an INTEGER.')
        
print ('Please type an integer.')
collatz(input())
