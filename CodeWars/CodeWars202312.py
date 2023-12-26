# arr = [1,2,3,6,4,1,2,3,2,1]
# ans = {"pos":[3,7], "peaks":[6,3]}
# The first and last elements of the array will not be considered as peaks 
# (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

[-2, 20, 11, -2, -2, 14, 17, 7]
[-2, 20, 11, -2, -2, 14, 17, 7]

# 定義波峰波谷再切割 再比
def pick_peaks(arr):
    pos = []
    peaks = []
    min_pos = []
    min_num = ''
    max_pos = []
    max_num = ''
    
    if len(arr) == 0 or max(arr) == min(arr):
        return {'pos':[], 'peaks':[]}
    else:
        # 跟左邊右邊比就好 所以左右邊都要有數字, 波谷會有兩個一樣的數字, 這兩個數字都比左右邊數字小
        for i in range(len(arr)):
            min_count = 0
            max_count = 0
            if i-1 >= 0 and i+1 != len(arr): #邊角不算
                # 波谷一個數字, 需要做if arr[i] == arr[j]
                for j in range(i-1, i+2, 2):
                    if j-1 >= 0 and j+1 != len(arr):
                        if arr[i] < arr[j]: min_count+=1
                        if arr[i] > arr[j]: max_count+=1
                        if j+1 < len(arr):
                            if arr[i] == arr[j] and arr[i] and arr[i] < arr[i-1] and arr[j] < arr[j+1]: min_count+=1
                        if i+1 < len(arr):
                            if arr[i] == arr[j] and arr[i] and arr[i] < arr[i+1] and arr[j] < arr[j-1]: min_count+=1
                if min_count == 2:
                    min_pos.append(i)
                    min_num += str(arr[i]) + ', '   
                if max_count == 2: 
                    max_pos.append(i)
                    max_num += str(arr[i]) + ', '

        print(f'波谷位置= {min_pos}\n波谷: {min_num}') #波谷定義: 這個數字比兩邊數字都小
        print(f'波峰位置= {max_pos}\n波峰: {max_num}') #波峰定義: 這個數字比兩邊數字都大

        # 分割Lists
        Lists = []
        for i in range(len(min_pos)):
            if len(min_pos) == 1:
                Lists.append(arr[0:min_pos[i]+1])
                Lists.append(arr[min_pos[i]:])
            else:
                if i == 0:
                    Lists.append(arr[0:min_pos[i]+1])
                    Lists.append(arr[min_pos[i]:min_pos[i+1]+1])
                elif i == len(min_pos)-1:
                    Lists.append(arr[min_pos[i]:])
                else:
                    Lists.append(arr[min_pos[i]:min_pos[i+1]+1])
        print(f'Lists: {Lists}')

        
        List_Pos = 0
        for i in range(len(Lists)):
            count = len(Lists[i])
            #處理無效Lists
            for j in range(len(Lists[i])):
                if len(Lists[i]) > 2:
                    if Lists[i][0] == max(Lists[i]): Lists[i].pop(0)
                    if Lists[i][-1] == max(Lists[i]): Lists[i].pop(-1)
            #比大小
            if len(Lists[i]) > 2:
                non_added = True
                for k in range(len(Lists[i])):
                    if Lists[i][k] == max(Lists[i]) and non_added:
                        pos.append(List_Pos + k - i) #5 + 1 - 1
                        non_added = False
                peaks.append(max(Lists[i]))
            List_Pos+=count
    return {'pos':pos, 'peaks':peaks}


# [1,2,3,6,4,1,2,3,2,1]
# [1,2,3,6,4,1] [1,2,3,2,1]

basic = [3, 4, 9, 13, 0, -3]
ans = {'pos': [3], 'peaks': [13]}

test = [-4, 8, 7, -1, 11, 12, -2, -5, 5, -2, 20, 11, -2, -2, 14, 17, 7, 16, -4, 3, 5, -5, 1, 2, -3, -4, 17, -1, 20, 5] #要拆開來
ans = {'pos': [1, 5, 8, 10, 15, 17, 20, 23, 26, 28], 'peaks': [8, 12, 5, 20, 17, 16, 5, 2, 17, 20]}
# -2,-2 沒分割到

test2 = [18, 14, -1, 11, 5, 5, 17, 19, 16, 16]
ans = {'pos': [3, 7], 'peaks': [11, 19]}

test3 = [19, 6, 6, 16, 12, 0, 15, 17]
ans = {'pos': [3], 'peaks': [16]}

test4 = [16, 3, 16, -2, 15, 18, 11, -3, 16, 1, -2, 3, 14, 8, 19, 10, -1, -5, 11, 4, 4, 1, 1, 15, 2, 2]

print(pick_peaks(test))


[19, 6, 6, 16, 12, 0, 15, 17]
[19, 6, 6, 16, 12, 0, 15, 17]


def pick_peaks_best(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}