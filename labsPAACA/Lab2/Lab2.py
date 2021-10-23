#mytest 15, 14, 26, 19, 28, 22, 7, 29, 1, 17, 3, 4, 27, 8, 0, 9
import os
class tree_node:
    def __init__(data):
        _right = None
        _left = None
        _data = data

class tree:
    def __init__():
        _root = None
    def add_node(data):
        pass
        



with open('labsPAACA\Lab2\console.txt', 'w') as file:   
    masiv = input("Введите корень и вершины дерева перечислением через запятую: ").replace(" ", "").split(',')
    masiv = [int(x) for x in masiv]
    print(masiv)