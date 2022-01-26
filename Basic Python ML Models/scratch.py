b=int(input("Enter the size of array"))

array=[]
for i in range(b):
    a=int(input("Enter Your Numbers to be sorted"))
    array.append(a)

def heapifying(arr,n):
    for j in range(len(arr)-1,-1,-1):

        if 2*j <= n:
            c=arr[2*j]


        if 2*j+1 <= n:
            child.append(arr[2*j+1])

        print(child)




