def collatz(N):
    if N%2==0:
        N=N//2
    else:
        N=3*N+1
    print(N)
    return(N)
N=int(input('Enter the number here :'))
print(N)
while True:
    if N==1:
        break
    else:
        N=collatz(N)
    

        
    