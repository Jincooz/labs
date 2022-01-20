import time
def Ford_Bellmen(matrix_vesov, matrix_soedenenii, length=30):
    matrix_result = [[0] for vec in matrix_vesov]
    for n in range(length):
        vector_result = [inf] * length
        vector_result[n] = 0 
        for m in range(length):
            for j in range(length):
                for i in range(length):
                    if vector_result[j] + matrix_vesov[j][i] < vector_result[i] and matrix_soedenenii[j][i] == 1:
                        vector_result[i] = vector_result[j] + matrix_vesov[j][i]
        matrix_result[n] = vector_result
        print(vector_result)
    return matrix_result

def make_max(matrix_vesov, length=30):
    for i in range(length):
        for j in range(length):
            if matrix_vesov[i][j] == 0:
                matrix_vesov[i][j] = inf


def Dijkstra_2(index, matrix_vesov, length=30):
    If_true = [True]*length
    weight = [inf]*length
    weight[index] = 0
    for i in range(length):
        min_weight = inf + 1
        index_min_weigth = -1
        for j in range(length):
            if If_true[j] and weight[j] < min_weight:
                min_weight = weight[j]
                index_min_weigth = j
        for k in range(length):
            if weight[index_min_weigth] + matrix_vesov[index_min_weigth][k] < weight[k]:
                weight[k] = weight[index_min_weigth] + matrix_vesov[index_min_weigth][k]
        If_true[index_min_weigth] = False
    return weight


def Dijkstra(matrix_vesov, length=30):
    changed_W = [list(vec) for vec in matrix_vesov]
    make_max(changed_W)
    result = [[0] for i in range(30)]
    for i in range(length):
        result[i] = Dijkstra_2(i, changed_W)
        print(result[i])
    return result

def Floyd_Warshall(matrix_vesov, length=30):
    changed_W = [list(vec) for vec in matrix_vesov]
    make_max(changed_W)

    matrix_result_now = [[inf for first_index in range(length)] for second_index in range(length)]
    matrix_result_next = [[inf for first_index in range(length)] for second_index in range(length)]
    for i in range(length):
        for j in range(length):
            matrix_result_now[i][j] = changed_W[i][j] 
    for k in range(0, length):
        for i in range(length):
            for j in range(length):
                matrix_result_next[i][j] = min(matrix_result_now[i][j], matrix_result_now[i][k-1] + matrix_result_now[k-1][j])
        matrix_result_now = matrix_result_next[:]

    for i in range(length):
        for j in range(length):
            if i==j:
                matrix_result_next[i][j]=0
        print(matrix_result_next[i])
    return matrix_result_next

def Johnson(matrix_soedenenii, matrix_vesov, length=30):
    new_W = [[0 for j in range(length+1)] for i in range(length+1)]
    new_E = [[0 for j in range(length+1)] for i in range(length+1)]
    for i in range(length+1):
        for j in range(length+1):
            if i == 0 or j == 0:
                new_W[i][j] = 0
                new_E[i][j] = 1
            else:
                new_W[i][j] = matrix_vesov[i - 1][j - 1]
                new_E[i][j] = matrix_soedenenii[i - 1][j - 1]
    def Ford_Bellmen2(matrix_soedenenii, matrix_vesov, length = 30):
        vector_result = [inf] * length
        vector_result[0] = 0 
        for m in range(length):
            for j in range(length):
                for i in range(length):
                    if vector_result[j] + matrix_vesov[j][i] < vector_result[i] and matrix_soedenenii[j][i] == 1:
                        vector_result[i] = vector_result[j] + matrix_vesov[j][i]
        return vector_result
    H = Ford_Bellmen2(new_E, new_W, length + 1)
    changed_W = [list(vec) for vec in matrix_vesov]    
    for i in range(length):
        for j in range(length):
            changed_W[i][j] += H[i] - H[j]
    result = Dijkstra(changed_W)
    return result

#Start of the program
inf = 10**8

E = [[1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0], [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]] 
W = [[3, 6, 0, 0, 4, 10, 0, 5, 0, 0, 0, 0, 8, 7, 0, 4, 4, 7, 0, 4, 5, 0, 5, 2, 0, 0, 9, 5, 0, 0], [1, 9, 2, 0, 4, 0, 8, 0, 7, 0, 0, 9, 10, 7, 8, 4, 0, 0, 0, 0, 6, 2, 8, 2, 0, 9, 7, 1, 0, 7], [0, 9, 8, 2, 0, 0, 5, 6, 5, 0, 0, 0, 2, 0, 5, 0, 5, 6, 2, 0, 6, 0, 0, 0, 0, 0, 1, 6, 0, 0], [3, 8, 2, 0, 0, 5, 0, 3, 0, 0, 0, 1, 0, 4, 0, 0, 7, 0, 7, 3, 0, 6, 3, 0, 0, 0, 7, 0, 0, 0], [8, 0, 2, 8, 6, 0, 4, 0, 0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 2, 3, 0, 6, 0, 0, 10, 10, 5, 8, 5, 0], [0, 3, 0, 0, 1, 1, 0, 3, 0, 8, 1, 0, 0, 0, 5, 7, 6, 0, 2, 8, 0, 8, 0, 0, 0, 5, 9, 9, 1, 0], [3, 0, 0, 7, 10, 2, 7, 0, 0, 0, 6, 4, 0, 4, 1, 0, 1, 0, 3, 0, 0, 3, 7, 2, 0, 0, 6, 0, 0, 10], [4, 0, 0, 0, 1, 0, 8, 0, 0, 8, 0, 0, 6, 0, 9, 0, 9, 0, 5, 6, 0, 0, 1, 0, 7, 9, 0, 0, 0, 0], [7, 0, 1, 0, 10, 0, 0, 5, 0, 5, 0, 0, 7, 0, 3, 4, 0, 0, 9, 7, 0, 9, 9, 6, 0, 6, 5, 5, 0, 0], [2, 10, 1, 0, 4, 0, 9, 0, 2, 0, 0, 0, 0, 0, 0, 9, 7, 0, 8, 0, 4, 0, 0, 5, 1, 0, 2, 1, 0, 10], [9, 2, 0, 6, 2, 9, 0, 0, 2, 10, 4, 0, 2, 0, 0, 6, 0, 8, 1, 0, 7, 0, 0, 4, 7, 0, 0, 0, 1, 0], [9, 0, 1, 0, 0, 1, 1, 0, 6, 7, 0, 0, 10, 0, 9, 5, 0, 0, 5, 0, 0, 0, 10, 0, 8, 0, 1, 0, 9, 8], [10, 2, 4, 0, 8, 0, 8, 0, 9, 6, 7, 0, 0, 0, 7, 0, 3, 9, 9, 3, 10, 3, 0, 5, 0, 1, 0, 3, 0, 0], [0, 0, 2, 4, 0, 8, 8, 0, 0, 1, 0, 0, 8, 0, 4, 0, 9, 7, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 7, 0, 5, 8, 0, 5, 0, 0, 0, 6, 0, 0, 0, 0, 4, 8, 3, 7, 0, 0, 0, 0, 6], [0, 3, 5, 0, 0, 0, 2, 0, 5, 5, 1, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 0, 9, 1, 0, 9, 5, 0, 0], [8, 8, 0, 10, 4, 8, 1, 0, 5, 0, 0, 1, 10, 2, 8, 0, 10, 3, 10, 1, 0, 5, 8, 0, 0, 0, 1, 0, 0, 1], [10, 0, 0, 0, 3, 3, 4, 0, 0, 0, 9, 7, 6, 0, 9, 1, 0, 6, 0, 6, 2, 6, 10, 10, 7, 10, 0, 2, 0, 4], [6, 0, 2, 1, 8, 1, 0, 6, 0, 1, 3, 6, 0, 8, 0, 0, 1, 1, 0, 0, 2, 1, 4, 0, 8, 0, 0, 4, 0, 0], [2, 0, 6, 0, 0, 2, 8, 4, 8, 0, 0, 8, 5, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 6, 1, 1, 0, 0, 0, 0], [10, 0, 0, 0, 4, 6, 9, 10, 6, 0, 0, 1, 0, 0, 0, 6, 6, 1, 0, 0, 2, 0, 6, 4, 9, 0, 2, 9, 10, 6], [1, 0, 0, 9, 0, 8, 0, 3, 0, 0, 0, 8, 0, 5, 10, 0, 0, 0, 0, 7, 0, 5, 9, 10, 0, 4, 9, 1, 4, 0], [0, 6, 0, 1, 0, 3, 2, 4, 1, 7, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 2, 0, 0, 0, 0, 0, 0, 0], [0, 5, 0, 2, 8, 3, 9, 10, 0, 5, 0, 5, 0, 1, 8, 0, 2, 0, 0, 0, 6, 1, 7, 0, 5, 2, 0, 8, 2, 0], [0, 0, 5, 0, 0, 0, 1, 4, 3, 8, 0, 0, 0, 2, 1, 8, 10, 3, 0, 0, 0, 10, 0, 0, 9, 0, 0, 1, 2, 10], [0, 0, 2, 1, 0, 4, 3, 10, 0, 10, 0, 9, 0, 1, 0, 0, 5, 0, 5, 5, 4, 9, 0, 0, 4, 0, 4, 1, 0, 7], [4, 0, 5, 0, 6, 0, 1, 0, 9, 0, 8, 0, 10, 3, 6, 0, 0, 0, 5, 1, 4, 1, 0, 3, 0, 0, 10, 0, 9, 0], [9, 1, 0, 0, 7, 0, 5, 3, 0, 9, 10, 1, 10, 0, 9, 3, 1, 0, 8, 6, 0, 10, 0, 4, 2, 0, 10, 10, 3, 3], [1, 0, 6, 0, 5, 0, 2, 0, 0, 0, 0, 6, 7, 6, 0, 0, 0, 0, 8, 0, 7, 1, 0, 0, 0, 0, 3, 6, 7, 9], [6, 5, 0, 0, 1, 0, 10, 0, 0, 5, 10, 2, 3, 4, 0, 5, 3, 8, 0, 5, 5, 5, 0, 6, 0, 0, 0, 7, 8, 10]]

print('Ford_Bellmen')
start_time = time.time()
res1 = Ford_Bellmen(W, E)
print("--- %s seconds ---" %(time.time() - start_time))
print('\n\n-------------------------------------------------------------------------------------------------------\n\n')
print('Dijkstra')
start_time = time.time()
res2 = Dijkstra(W)
print("--- %s seconds ---" %(time.time() - start_time))
print('\n\n-------------------------------------------------------------------------------------------------------\n\n')
print('Floyd_Warshall')
start_time = time.time()
res3 = Floyd_Warshall(W)
print("--- %s seconds ---" %(time.time() - start_time))
print('\n\n-------------------------------------------------------------------------------------------------------\n\n')
print('Johnson')
start_time = time.time()
res4 = Johnson(E, W)
print("--- %s seconds ---" %(time.time() - start_time))
print('\n\n-------------------------------------------------------------------------------------------------------\n\n')
no_error = True
for i in range(30):
    for j in range(30):
        if(res1[i][j] != res2[i][j] or res1[i][j] != res3[i][j] or res1[i][j] != res4[i][j]):
            print('Graph error')
            no_error = False
if no_error:
    print('Vse rezultati odinakovie')

def Dijkstra2(matrix_soedenenii, matrix_vesov, start_index, end_index, length=30):
    changed_W = [list(vec) for vec in matrix_vesov]
    make_max(changed_W)
    If_true = [True]*length
    weight = [inf]*length
    weight[start_index] = 0
    weight_path = [[((j) if i == 0 else 0) for i in range(length+1)] for j in range(30)]
    s = 1
    for i in range(length):
        min_weight = inf + 1
        index_min_weigth = -1
        for j in range(length):
            if If_true[j] and weight[j] < min_weight:
                min_weight = weight[j]
                index_min_weigth = j
        for k in range(length):
            if weight[index_min_weigth] + changed_W[index_min_weigth][k] < weight[k]:
                weight[k] = weight[index_min_weigth] + changed_W[index_min_weigth][k]
                weight_path[k] = (weight_path[index_min_weigth])[:]
                weight_path[k][s] = index_min_weigth
            else:
                weight_path[k][s] = weight_path[k][s-1]            
        s += 1
        If_true[index_min_weigth] = False
    matrix = Dijkstra_2(start_index, changed_W)
    return weight_path[end_index]


while(True):
    print("Знайти шлях від початкового до кінечного?(y/n)")
    check = input()
    if check == "y":
        print("Початкова вершина : ", end ="")
        start_index = int(input())
        print("Кінцева вершина : ", end ="")
        end_index = int(input())
        print(Dijkstra2(E, W, start_index, end_index))
    elif check == "n":
        break
    else: 
        print("Помилка у вводі, спробуйте ще раз")

