def countNumbers(arr):
    for pair in arr:
        count=0
        for num in range(pair[0], pair[1]+1):
            if len(set(str(num)))==len(str(num)):
                count+=1
        print(count)
arr=[[1,20], [9,19]]
countNumbers(arr)
#print(res)