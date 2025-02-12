'''
Program : currency.py
 Takes an integer from the user,representing the number of knuts, and output the number of Galleons, Sickels, amd Knuts it translates to.
'''
def closestMulitple(n,m):
    for i in range(1,n+1):
        if i*m <= n:
            continue;
        else:
            return i-1
            break
        
one_sickle = 29 
one_galleon = 17 
knuts,sickles,galleons = 0,0,0
money = int(input("Enter the currency in knuts \n"))
sickles = closestMulitple(money,one_sickle)
if (sickles * one_sickle) <= money:
    knuts = money - (sickles * one_sickle )
galleons = closestMulitple(sickles,one_galleon)
if (galleons * one_galleon) <= sickles:
    sickles = sickles - (galleons * one_galleon)
print("{} knuts = {} galleons {} sickles and {} knuts.".format(money,galleons,sickles,knuts))