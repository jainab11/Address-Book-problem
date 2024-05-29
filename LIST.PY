lst = ["jainab","amit","ram","farzana"]
lst.sort(key=lambda x:x[0])
print(lst)
def swap_i(lst,i,j):
    lst[i],lst[j]=lst[j],lst[i]
for item in range(len(lst)-1):
    if lst[item][0] > lst[item+1][0]:
        swap_i(lst,item,item+1)
print(lst)

