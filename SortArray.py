arr = [1, 2]
if arr == sorted(arr):
    print ('yes, ascending')
elif arr == sorted(arr)[::-1]:
    print ('yes, desending')
else:
    print ('no')