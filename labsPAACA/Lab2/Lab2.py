import math


def element_parent(element_index):
        return element_index//2
    
def element_left(element_index):
        return element_index * 2 

def element_right(element_index):
        return element_index * 2 + 1

def height(Node):
    if Node is not None:
        return Node.height
    else:
        return -1

def power_2_sum(i):
        if i <= -1:
                return 0
        else:
                return (pow(2, i)+power_2_sum(i-1))

class Node:
    def __init__(self, value):
        self.value = value
        self.height = 0
        self.right = None
        self.left = None
    
    def balance(self):
        return height(self.right) - height(self.left)




class Balanced_Binary_Tree:
        def __init__(self):
            self.root = None
            self.size = 0

        def Turn_left(self, Old_root):
            New_root = Old_root.right
            New_root_left = New_root.left
            New_root.left = Old_root 
            Old_root.right = New_root_left
        
            Old_root.height = 1 + max(height(Old_root.left), height(Old_root.right)) 
            New_root.height = 1 + max(height(New_root.left), height(New_root.right)) 
            return New_root     
        def Turn_right(self, Old_root):
            New_root = Old_root.left
            New_root_right = New_root.right
            New_root.right = Old_root 
            Old_root.left = New_root_right
        
            Old_root.height = 1 + max(height(Old_root.left), height(Old_root.right)) 
            New_root.height = 1 + max(height(New_root.left), height(New_root.right)) 
            return New_root     

        def add_value(self, value, Temp_Node):
                Turn = False
                if Temp_Node is not None:
                    if value < Temp_Node.value:
                        Temp_Node.left, Turn = self.add_value(value, Temp_Node.left)
                    elif value > Temp_Node.value:
                        Temp_Node.right, Turn = self.add_value(value, Temp_Node.right)
                else:
                    self.size += 1
                    return Node(value), False

                Temp_Node.height = 1 + max(height(Temp_Node.left), height(Temp_Node.right))
                balance = Temp_Node.balance()

                if balance == 2:
                        if Temp_Node.right.balance() == 1:
                                print("\nНеобхідно зробити лівий поворот у вершині", Temp_Node.value, end="")
                                print(":")
                                print("\nДо повороту:\n")
                                self.print_Balanced_Binary_Tree([self.root], math.trunc(math.log(Balanced_Binary_Tree.size, 2))+1, 0)
                                return self.Turn_left(Temp_Node), True
                        else:
                                print("\nНеобхідно зробити правий поворот у вершині", Temp_Node.right.value, "та лівий поворот у вершині", Temp_Node.value, end="")
                                print(":")
                                print("\nДо повороту:\n")
                                self.print_Balanced_Binary_Tree([self.root], math.trunc(math.log(Balanced_Binary_Tree.size, 2))+1, 0)
                                Temp_Node.right = self.Turn_right(Temp_Node.right) 
                                return self.Turn_left(Temp_Node), True

                if balance == -2:
                        self.print_Balanced_Binary_Tree([self.root], math.trunc(math.log(Balanced_Binary_Tree.size, 2))+1, 0)
                        if Temp_Node.left.balance() == -1:
                                print("\nНеобхідно зробити правий поворот у вершині", Temp_Node.value, end="")
                                print(":")
                                print("\nДо повороту:\n")
                                self.print_Balanced_Binary_Tree([self.root], math.trunc(math.log(Balanced_Binary_Tree.size, 2))+1, 0)
                                return self.Turn_right(Temp_Node), True
                        else:
                                print("\nНеобхідно зробити лівий поворот у вершині", Temp_Node.left.value, "та правий поворот у вершині", Temp_Node.value, end="")
                                print(":")
                                print("\nДо повороту:\n")
                                self.print_Balanced_Binary_Tree([self.root], math.trunc(math.log(Balanced_Binary_Tree.size, 2))+1, 0)
                                Temp_Node.left = self.Turn_left(Temp_Node.left) 
                                return self.Turn_right(Temp_Node), True
                
                return Temp_Node, Turn
        
        def print_values(self, Temp_Node):
                if Temp_Node.left is not None:
                        self.print_values(Temp_Node.left)
                        print(Temp_Node.value, end = ' ')
                if Temp_Node.right != None:
                        self.print_values(Temp_Node.right)
        
        def print_Balanced_Binary_Tree(self, arr, level_counter, values_counter):
                new_arr = []
                if level_counter == 0:
                        for Temp_Node in arr:
                                print(' '*(pow(2, level_counter)-2), end="")
                                if Temp_Node != None:
                                        print('%3d' % Temp_Node.value, end="")
                                        values_counter += 1
                                        new_arr.append(Temp_Node.left)
                                        new_arr.append(Temp_Node.right)
                                else:
                                        print('   ', end="")
                                        new_arr.append(None)
                                        new_arr.append(None) 
                                if values_counter == self.size:
                                        return
                                print(' ', end="")
                        print('')

                else:     
                        print(' '*(power_2_sum(level_counter-1)+1),  end="")   
                        for Temp_Node in arr:
                                print(' '*(pow(2, level_counter)-2), end="")
                                if Temp_Node != None:
                                        print('%3d' % Temp_Node.value, end="")
                                        values_counter += 1
                                        new_arr.append(Temp_Node.left)
                                        new_arr.append(Temp_Node.right)
                                else:
                                        print('   ', end="")
                                        new_arr.append(None)
                                        new_arr.append(None)
                                print(' '*(pow(2, level_counter)), end="")
                                print(' '*(power_2_sum(level_counter)), end="")
                        print('')

                print(' '*(power_2_sum(level_counter-1)+1),  end="")
                i = 0
                while i < len(new_arr):
                        if new_arr[i] != None:
                                print(' ─'*(pow(2, level_counter)-1), end="")
                                i += 1
                                if new_arr[i] != None:
                                        print(' ─'*(pow(2, level_counter)-1), end=" ")
                                        print(' '*(power_2_sum(level_counter)), end="")
                                        i += 1
                                else:
                                        print(' ', end="")
                                        print(' '*(pow(2, level_counter)), end="")
                                        print(' '*(power_2_sum(level_counter)), end="")
                                        i += 1
                        else:
                                print(' '*(pow(2, level_counter)), end="")
                                i += 1
                                if new_arr[i] != None:
                                        print(' ─ '*(pow(2, level_counter)-1), end="")
                                        print(' '*(power_2_sum(level_counter)), end="")
                                        i += 1
                                else:
                                        print(' ', end="")
                                        print(' '*(pow(2, level_counter)), end="")
                                        print(' '*(power_2_sum(level_counter)), end="")
                                        i += 1
                print('')
                self.print_Balanced_Binary_Tree(new_arr, level_counter-1, values_counter)
                return

            

class Binary_Tree:
        def __init__(self, values_list):
                self.root = Node(values_list[0])
                self.size = 0 
                self.values_list = values_list
                

        def print_Tree(self):
            amount_of_vertices_on_level = 1
            values_counter = 0
            amount_of_spaces_on_level = len(self.values_list) // 2
            level_counter = math.trunc(math.log(len(self.values_list), 2))
            for i in range(math.trunc(math.log(len(self.values_list), 2))): 
                    #for i in range(amount_of_vertices_on_level):
                    print(' '*(power_2_sum(level_counter-1)+1),  end="")
                    for y in range(amount_of_vertices_on_level):
                            print(' '*(pow(2, level_counter)-2), end="")
                            print('%3d' % self.values_list[values_counter], end="")
                            values_counter += 1
                            if values_counter == len(self.values_list):
                                    return
                            print(' '*(pow(2, level_counter)), end="")
                            print(' '*(power_2_sum(level_counter)), end="") 
                    print('')
                    print(' '*(power_2_sum(level_counter-1)+1),  end="")
                    if i <= math.trunc(math.log(len(self.values_list), 2)) - 2:
                            for j in range(amount_of_vertices_on_level):
                                    print(' ─'*(pow(2, level_counter)-1), end=" ")
                                    print('─'*(pow(2, level_counter)-1), end=" ")
                                    print(' '*(power_2_sum(level_counter)), end="")

                    else:
                            temp_values_counter = values_counter
                            for j in range(amount_of_vertices_on_level):
                                    temp_values_counter += 1 
                                    print(' ─'*(pow(2, level_counter)-1), end="")
                                    if temp_values_counter == len(self.values_list):
                                            print('┘', end="")
                                            break
                                    print('─ '*(pow(2, level_counter)), end="")
                                    temp_values_counter += 1
                                    if temp_values_counter == len(self.values_list):
                                            break
                                    print(' '*(power_2_sum(level_counter)), end="")    
                    level_counter -= 1
                    amount_of_vertices_on_level *= 2
                    print('')
        
            print('%3d' % self.values_list[values_counter], end="")
            values_counter += 1
            if values_counter == len(self.values_list):
                    print('')
                    return 
            for y in range(amount_of_vertices_on_level):
                    print(' '*(pow(2, level_counter)), end="")
                    print('%3d' % self.values_list[values_counter], end="")
                    values_counter += 1
                    if values_counter == len(self.values_list):
                            print('')
                            return
        
            return

        def sift_down(self, element_index, heap_list):
                while element_index > -1:
                        smallest = element_index
                        right_child = element_right(element_index+1)-1
                        left_child = element_left(element_index+1)-1
                        Heap_lenght = len(heap_list)
                        if right_child < Heap_lenght and heap_list[element_index] > heap_list[right_child]:
                                if heap_list[left_child] > heap_list[right_child]:
                                        smallest = right_child
                                else: 
                                        smallest = left_child
                        else:
                                if left_child < Heap_lenght and heap_list[element_index] > heap_list[left_child]:
                                        smallest = left_child
                                else:
                                        break
                        heap_list[smallest], heap_list[element_index] = heap_list[element_index], heap_list[smallest]
                        element_index = smallest

        def Build_Heap(self):
                for i in reversed(range(len(self.values_list)//2)):
                        self.sift_down(i, self.values_list)

        def HeapSort(self):
                self.Build_Heap()
                auxiliary_list = self.values_list[:]
                Heap_length = len(self.values_list)
                for i in range(Heap_length):
                        auxiliary_list[0], auxiliary_list[len(auxiliary_list)-1] = auxiliary_list[len(auxiliary_list)-1], auxiliary_list[0]
                        self.values_list[i] = auxiliary_list.pop()                   
                        self.sift_down(0, auxiliary_list) 

        def create_Balanced_Binary_Tree(self):
                temp_Balanced_Binary_Tree = Balanced_Binary_Tree()
                for i in range(len(self.values_list)-1):
                        temp_Balanced_Binary_Tree.add_value(self.values_list())



Tree = Binary_Tree([15, 14, 26, 19, 28, 22, 7, 29, 1, 17, 3, 4, 27, 8, 0, 9])
Tree.print_Tree()
Balanced_Binary_Tree = Balanced_Binary_Tree()
print('\n\n\n')
print("Балансування дерева:\n")
Turn = False
for i in range(len(Tree.values_list)):
        print("Крок", i+1, end="")
        print(". Балансування вершини", Tree.values_list[i], end="")
        print(". ")
        Balanced_Binary_Tree.root, Turn = Balanced_Binary_Tree.add_value(Tree.values_list[i], Balanced_Binary_Tree.root)
        if Turn:
                print("\n\nПісля повороту:\n")
                Balanced_Binary_Tree.print_Balanced_Binary_Tree([Balanced_Binary_Tree.root], math.trunc(math.log(Balanced_Binary_Tree.size, 2)), 0)
                print('\n\n')
        else:
                print("Робити поворот не потрібно.")
                print('\n')

print("Результат :\n")
Balanced_Binary_Tree.print_Balanced_Binary_Tree([Balanced_Binary_Tree.root], math.trunc(math.log(Balanced_Binary_Tree.size, 2)), 0)
print("\n")
print("Сортування:\n")
Tree.HeapSort()
Tree.print_Tree()