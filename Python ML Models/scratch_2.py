def heapify(arr,n):
    for i in range(len(arr)-1,-1,-1):
        if 2*i<=n:
            a=arr[2*i]
        if 2*i+1<=n:
            b=arr[2*i+1]

        c=max(a,b)

        if c>arr[i]:
            arr[i],c=c,arr[i]



arr=[4,1,3,9,7]
len(arr)
heapify(arr,len(arr))

