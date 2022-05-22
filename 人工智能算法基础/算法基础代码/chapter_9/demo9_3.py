def hanoi(n,start,mid,end):
    #只有一个的情况
    if n==1:
        print(f'{start}-{end}')
    #如果大于1，就要递归
    else:
        #移动上面的一堆，从A-B
        hanoi(n-1,start,end,mid)
        #移动最后一个,A-C
        hanoi(1,start,mid,end)
        #移动上面的一堆,B-C
        hanoi(n-1,mid,start,end)
if __name__ == '__main__':
    hanoi(3,'a','b','c')
