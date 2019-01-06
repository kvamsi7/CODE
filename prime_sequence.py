''' prime sequence generation program
'''
import math

def check_prime(num):

    k = int(math.sqrt(num))

    flag = 1
    for i in range(2,k+1):
        if num % i == 0:
            return False
    return True

seq_num = int(input())
j = 2
while(seq_num !=0):

    if(check_prime(j)):
        print(j)
        seq_num = seq_num - 1
    j= j+1
        
