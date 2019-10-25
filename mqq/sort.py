#https://blog.csdn.net/weixin_41571493/article/details/81875088
#冒泡
def bubbleSort(list):
    l = len(list)
    for i in range(l):
        for j in range(l-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list
#
def sumTest(n):
    sum1 = 0
    for i in range(n+1):
        sum1 = sum1+i
    return sum1
#递归1+2+。。+100
def sumTest1(n):
    if n==1:
        return 1
    else:
        return n+sumTest1(n-1)

if __name__=="__main__":
    list1=[54, 24, 65, 5, 26, 23, 165, 37, 9, 95]
    list2=bubbleSort(list1)
    print(list1)
    list3=sorted(list1)
    print(list3)
    print(sumTest(5))
    print(sumTest1(5))