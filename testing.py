

def cvtnum(n):
    res = []
    while True:
        res.append(n%2)
        n=n//2
        if n==0:
            break
    return res

def tonum(a):
    sum = 0
    mult = 1
    for i in range(0,len(a)):
        sum = sum + (a[i]*mult)
        mult = mult * 2
        
    return sum

def add_(a,b):
    res = []
    carry = 0
    for i in range(len(a)):
        if a[i]==1 and b[i]==1:
            if carry==1:
                res.append(1)
            else:
                res.append(0)
            carry = 1
        if a[i]==0 and b[i]==0:
            if carry == 1:
                res.append(1)
            else:
                res.append(0)
            carry = 0
        if (a[i]==0 and b[i]==1) or (a[i]==1 and b[i]==0):
            if carry == 1:
                res.append(0)
                carry = 1
            else:
                res.append(1)
                carry = 0
        
    if carry==1:
        res.append(1)

    print("res",res)
    return res

def test1():
    # this is little endian
    thirteen = [1,0,1,1]
    ten = [0,1,0,1]

    print("thirteen", thirteen)
    print("tonum on thirteen", tonum(thirteen))
    res = add_(ten,thirteen)
    print("res tonum",tonum(res))


def test2():
    a = cvtnum(13)
    print("res of cvtnum13",a)
    a = cvtnum(12)
    print("res of cvtnum12",a)


def test3():
    nums = []
    for i in range(1,3):
        nums.append(cvtnum(i))
    res = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            print("add_ called on",nums[i],nums[j])
            tmp = add_(nums[i],nums[j])
            res.append(tmp)

test3()
