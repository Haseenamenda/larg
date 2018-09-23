def largest(arr,n):
	max=arr[0]
	for i in range(1,n):
                  if arr[i]>max:
                      	max=arr[i]
	return max
arr=[10,324,45,90,9808,2,56,34,56,7]
n=len(arr)
Ans=largest(arr,n)
print(Ans)
