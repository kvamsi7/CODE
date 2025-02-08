result = []
def f(i,arr,target,res):
    global result
    if target == 0:
        result.append(res)
        # print(' '.join([str(i) for i in res]))
        return 
    if i >= len(arr)-1:
        return 

    if arr[i] <= target:
        f(i+1,arr,target-arr[i],res+[arr[i]])
        f(i+1,arr,target,res)
    else:
        f(i+1,arr,target,res)

def pairSum(arr,target):
    global result
    res = []
    f(0,arr,target,res)
    for i in result:
        print(i[0],i[1])


if __name__ == '__main__':
    arr = [1,3,7,5,9,8]
    target = 10
    pairSum(arr,target)
    