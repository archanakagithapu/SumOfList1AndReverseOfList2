'''Find the total sum of 2 list by adding lisst1 and reverse of list2'''
'''

def reverse(list, left, right):
    if left > right:
        return list
    list[left], list[right] = list[right], list[left]
    return reverse(list, left + 1, right - 1)

list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

n = len(list1)
m = len(list2)

list2 = reverse(list2, 0, m - 1)

sum_list = [a + b for a, b in zip(list1, list2)]
total_sum = sum(sum_list)

print("List1:", list1)
print("Reverse of List2:", list2)
print("Sum of lists:", sum_list)
print("Total sum:", total_sum)
'''

'''
-----------------------------------------------------------------------
List1 = [6, 5, 2, 7, 9]
List2 = [2, 4, 9, 6, 7, 4]
res=[]
def recSum(left,right):
  if left==len(List1) and right==-1:
    return
  res.append(List1[left]+List2[right])
  recSum(left+1,right-1)
recSum(0,len(List2)-1)
print(res)

---------------------------------------------------------------------

List1 = list(map(int,input().split()))
List2 = list(map(int,input().split()))
res=[]
def recSum(left,right):
  if left==len(List1) and right!=-1:
      res.extend(List2[right::-1])
      right=-1
  if left!=len(List1) and right==-1:
      res.extend(List1[left:])
      left=0
      return
  if left==len(List1) and right==-1:
      return   
  res.append(List1[left]+List2[right])
  recSum(left+1,right-1)
recSum(0,len(List2)-1)
print(res)
------------------------------------------------------------------------


list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
res=[]
def evenoddsum(i):
    if i>=len(list1) and i+1>=len(list2):
        return
    if i>=len(list1) and i+1<=lwen(list2):
        res.extend(list2[i+1::2])
        return
    if i<=len(list1) and i+1>=len(list2):
        res.extend(list1[i::2])
        return
    res.append(list1[i]+list2[i+1])
    evenoddsum(i+2)
evenoddsum(0)
print(res)


def even_elements(lst):
    return [x for x in lst if x % 2 == 0]
def odd_elements(lst):
    return [x for x in lst if x % 2 != 0]
List1 = list(map(int, input("Enter elements of List1 (space-separated): ").split()))
List2 = list(map(int, input("Enter elements of List2 (space-separated): ").split()))
even_List1 = even_elements(List1)
odd_List2 = odd_elements(List2)
res = [even_elem + odd_elem for even_elem in even_List1 for odd_elem in odd_List2]
print("res =", res)
-----------------------------------------------------------------------------
def even_elements(lst):
    return [x for x in lst if x % 2 == 0]
def odd_elements(lst):
    return [x for x in lst if x % 2 != 0]
def compute_sums(even_lst, odd_lst, res, even_index, odd_index):
    if even_index >= len(even_lst):
        return res
    if odd_index >= len(odd_lst):
        return compute_sums(even_lst, odd_lst, res, even_index + 1, 0)
    res.append(even_lst[even_index] + odd_lst[odd_index])
    return compute_sums(even_lst, odd_lst, res, even_index, odd_index + 1)
List1 = list(map(int, input().split()))
List2 = list(map(int, input().split()))
even_List1 = even_elements(List1)
odd_List2 = odd_elements(List2)
res = compute_sums(even_List1, odd_List2, [], 0, 0)
print("res =", res)
-----------------------------------------------------------------------------------
'''
def allEvenOddSum(L1,L2,i=0,j=0,result=None):
    if result == None:
        result = []
    if i >= len(L1):
        return result
    if L1[i] % 2 != 0:
        return allEvenOddSum(L1,L2,i+1,j,result)
    if j < len(L2):
        if L2[j] % 2 != 0:
            result.append(L1[i] +L2[j])
        return allEvenOddSum(L1,L2,i,j+1,result)
    else:
        return allEvenOddSum(L1,L2,i+1,0,result)
List1 = [6, 5, 2, 7, 9, 3]
List2 = [2, 4, 9, 6, 7, 4]
print(allEvenOddSum(List1,List2))
