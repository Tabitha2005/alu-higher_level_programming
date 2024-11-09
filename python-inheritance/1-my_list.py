>>> MyList = _import_('1-my_list').MyList


>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list
[1]
>>> my_list.append(2)
>>> my_list
[1, 2]
>>> my_list.pop()
2
>>> my_list
[1]
>>> my_list.append(4)
>>> my_list.append(6)
>>> my_list.append(3)
>>> my_list.print_sorted()
[1, 3, 4, 6]
>>> my_list
[1, 4, 6, 3]

>>> my_list.clear()
>>> my_list.append(1)
>>> my_list.append(5)
>>> my_list.append(8)
>>> my_list.append(7)
>>> my_list.append(9)
>>> my_list.append(2)
>>> my_list.append(0)
>>> new_l = my_list.copy()
>>> new_l
[1, 5, 8, 7, 9, 2, 0]
>>> my_list.count(2)
1
>>> my_list.index(3)
Traceback (most recent call last):
        ...
ValueError: 3 is not in list

>>> my_list.pop(3)
7
>>> my_list
[1, 5, 8, 9, 2, 0]

>>> my_list.insert(9, 0)
>>> my_list
[1, 5, 8, 9, 2, 0, 0]

>>> my_list.pop(20)
Traceback (most recent call last):
        ...
IndexError: pop index out of range

>>> my_list.print_sorted(8)
Traceback (most recent call last):
        ...
TypeError: print_sorted() takes 1 positional argument but 2 were given

>>> my_list.clear()
>>> my_list.print_sorted()
[]
>>> my_list.append(9)
>>> my_list.append(-2)
>>> my_list.append(8)
>>> my_list.print_sorted()
[-2, 8, 9]
