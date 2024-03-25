def count_triplets(arr, d):
    n=len(arr)
    count=0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if(arr[i]+arr[j])%d==0:
                    count+=1
    return count
arr=[2,3,1,6]
d=3
print(count_triplets(arr,d))
#pass