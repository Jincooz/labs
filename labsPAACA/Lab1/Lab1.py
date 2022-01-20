import random
def insertion_sort(list):
    comparison_amount, switch_amount = 0, 0
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j>=0:
            comparison_amount += 1
            if( key >= list[j]):
                break
            else:               
                switch_amount += 1
                list[j+1]=list[j]
                j -= 1
                
        list[j+1] = key
        #comparison_amount += 1
    return comparison_amount, switch_amount

def heap_sort(list):
    comparison_amount = 0
    switch_amount = 0
    def parent(i):
        return (i - 1)//2
    def left(i):
        return 2*i + 1
    def right(i):
        return 2*i + 2
    def max_heapify(list, index, size):
        nonlocal comparison_amount, switch_amount
        l = left(index)
        r = right(index)
        if (l < size and list[l] > list[index]):
            largest = l
        else:
            largest = index
        if (r < size and list[r] > list[largest]):
            largest = r    
        comparison_amount += 2
        if (largest != index):
            list[largest], list[index] = list[index], list[largest]
            switch_amount += 1
            comparison_amount += 1
            max_heapify(list, largest, size)
    def build_max_heap(list):
        nonlocal comparison_amount, switch_amount
        length = len(list)
        start = parent(length - 1)
        while start >= 0:
            comparison_amount += 1
            max_heapify(list, index=start, size=length)
            start = start - 1
        comparison_amount += 1
    build_max_heap(list)
    for i in range(len(list) - 1, 0, -1):
        list[0], list[i] = list[i], list[0]
        switch_amount += 1
        max_heapify(list, index=0, size=i)
    return comparison_amount, switch_amount

def radix_sort(list):
    comparison_amount, switch_amount = 0,0
    amount_of_digit_max = 0
    max_digit = 0
    for i in range(0,len(list)):
        comparison_amount += 1
        if(max_digit < list[i]):
            amount_of_digit_max = len(str(list[i]))            
            max_digit=int(('9' * amount_of_digit_max))
    big_list = [[0 for x in range(amount_of_digit_max)] for y in range(len(list))]
    big_list2 = [[0 for x in range(amount_of_digit_max)] for y in range(len(list))]
    for i in range(0,len(list)):
        for j in range(0,amount_of_digit_max):
            big_list[i][j] = int(list[i] // (10**(amount_of_digit_max-j-1)) % 10)
    for i in range(0, amount_of_digit_max):
        C = [0] * 10
        for j in range(0,len(list)):
            C[big_list[j][amount_of_digit_max -i-1]] += 1
        for j in range(1,10):
            C[j] += C[j-1]
        for j in reversed(range(0, len(list))):
            C[big_list[j][amount_of_digit_max -i-1]] -= 1
            big_list2[C[big_list[j][amount_of_digit_max -i-1]]] = big_list[j]
            switch_amount += 1
        big_list = big_list2[:]
    for i in range(0,len(list)):
        list[i]=0
        for j in range(0,amount_of_digit_max):
            list[i] += big_list2[i][j] * (10**(amount_of_digit_max-j-1))
    return comparison_amount, switch_amount

def print_for_size(size):
    file = open('suck.txt', 'w')
    lists1 = [[0 for x in range(size)] for y in range(3)]
    lists1[0][0] = 0
    lists1[2][0] = random.randint(size,size*10)
    for i in range(1,size):    
        lists1[0][i] = lists1[0][i-1] + random.randint(1,size*10)
        lists1[1][i] = random.randint(1,size*10000)
        lists1[2][i] = lists1[2][i-1] + random.randint(1,size*10)
    lists1[2] = lists1[2][::-1]
    lists2 = [row[:] for row in lists1]
    lists3 = [row[:] for row in lists2]
    comparison_amount, switch_amount = [[0 for x in range(3)] for y in range(3)] , [[0 for x in range(3)] for y in range(3)]
    comparison_amount[0][0], switch_amount[0][0] = heap_sort(lists1[0])
    comparison_amount[0][1], switch_amount[0][1] = insertion_sort(lists2[0])
    comparison_amount[0][2], switch_amount[0][2] = radix_sort(lists3[0])
    comparison_amount[1][0], switch_amount[1][0] = heap_sort(lists1[1])
    comparison_amount[1][1], switch_amount[1][1] = insertion_sort(lists2[1])
    comparison_amount[1][2], switch_amount[1][2] = radix_sort(lists3[1])
    comparison_amount[2][0], switch_amount[2][0] = heap_sort(lists1[2]) 
    comparison_amount[2][1], switch_amount[2][1] = insertion_sort(lists2[2])
    comparison_amount[2][2], switch_amount[2][2] = radix_sort(lists3[2])
    print("Купа sort comparison_amount for 1000:")
    for i in range(3):
        print(comparison_amount[i][0])
    print("Вставка sort comparison_amount for 1000:")
    for i in range(3):
        print(comparison_amount[i][1])
    print("Розряди sort comparison_amount for 1000:")
    for i in range(3):
        print(comparison_amount[i][2])
    print("Купа sort switch_amount for 1000:")
    for i in range(3):
        print(switch_amount[i][0])
    print("Вставка  sort switch_amount for 1000:")
    for i in range(3):
        print(switch_amount[i][1])
    print("Розряди sort switch_amount for 1000:")
    for i in range(3):
        print(switch_amount[i][2])
    for i in range(0, size):
        if(lists1[2][i] != lists2[2][i] or lists1[2][i]!=lists3[2][i]):
            file.write("Error")
    file.close()


print_for_size(1000)
print_for_size(10000)
print_for_size(100000)
input()