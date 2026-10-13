# sorting the array in ascending order
# a=[25,16,38,10,35,48,20,50]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)



# max1=0
# max2=0

# a=[25,16,38,10,35,48,20,50]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i]>a[j]:
#             max1=a[i]
#             max2=a[j]
#         else:
#             max1=a[j]
#             max2=a[i]
#             if a[i]>max1:
#                 max2=max1
#                 max1=a[i]

# print(max2)
# # print(max1)
#         # if a[i]>max1:
#         #     max2=max1
#         #     max1=a[i])

#------------------------------------------
#TWO POINTERS APPROACH
#-----------------------------------------
# 1.arr=[1,2,3,5,7,10,11,15] ----------->[brute force approach]
# #ouput targest is 15
# target=15
# sum=0
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         sum=arr[i]+arr[j]
#         if sum==target:
#             print(sum)

###optimal approach
# arr=[1,2,3,5,7,10,11,15]
# target=15
# left=0
# right=len(arr)-1
# while left < right:
#     sum=arr[left]+arr[right]
#     if sum== target:
#         print(sum)
#         break
#     elif sum>target:
#         right-=1
#     else:
#         left+=1


# 3sum ----------->[brute force approach]
#output=[[-1,0,1],[-1,-1,2]]
# sum=0
# num=[-1,0,1,2,-1,-4]
# for i in range(len(num)-3):
#     for j in range(i+1,len(num)-2):
#         for k in range(i+2,len(num)-1):
#             if((num[i]+num[j]+num[k]==0)):
#                 print([num[i], num[j], num[k]])
#             else:
#                 sum=0
              

# # optimal approach
# num=[-1,-1,-1,0,0,0,1,2,2,3]
# nums=sorted(num)
# sum=[]
# for i in range(len(nums)-2):
#     j=i+1
#     k=len(nums)-1
#     while (j<k  and nums[i]==nums[i-1]):
#         sum=nums[i]+nums[j]+nums[k]
#         if (sum==0):
#             print([nums[i], nums[j], nums[k]])
#             break
#         elif sum>0:
#             k-=1
#         else:
#             j+=1

# nums=[2,0,2,1,1,0]
# # nums=[2,0,2,1]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]>nums[j]:
#             nums[i],nums[j]=nums[j],nums[i]
# print(nums)


class Solution(object):
    def sortColors(self, nums):

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        print(nums)
Solution=Solution().sortColors([2,0,2,1,1,0])




class Solution(object):
    def sortColors(self, nums):

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        print(nums)
Solution=Solution().sortColors([2,0,1])
             
