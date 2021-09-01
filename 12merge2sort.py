l1=[1,3,5]
l2=[0,2,4]
for i in l2:
    l1.append(i)
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]<l1[j]:
            l1[i],l1[j]=l1[j],l1s[i]
print(l1)
#new
   def merge(self, nums1, nums2, n, m): 
        # code here
        for i  in range(n):
            for j in range(m):
                if nums1[i]>nums2[j]:
                    nums2[j],nums1[i]=nums1[i],nums2[j]
        nums1.sort()
        nums2.sort()
