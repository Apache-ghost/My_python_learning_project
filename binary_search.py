def binary_search(list,target):
    middle=0
    start=0
    end=len(list)
    step=0

    while(start<=end):
        print("steps",step,':',str(list[start:end+1]))
        step=step+1
        middle=(start+end)//2
        if target==list[middle]:
            return middle
        if target<list[middle]:
            end=middle-1
        else:
            start=middle+1
    return -1

list=[1,2,3,4,5,6,7,8,9]
target=2
binary_search(list,target)
