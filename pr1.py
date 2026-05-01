nest_lst = [1, [2, [3, 4], 5], 6]

def flatten_lst(l):
    flatten_list = []
    for num in l:
        if isinstance(num, list):
            flatten_list.extend(flatten_lst(num))
        else:
            flatten_list.append(num)
    return flatten_list
print(flatten_lst(nest_lst))


l1 = [1,2,3,4]
l2 = [2,3]

is_subset = True
for num in l2:
    if num not in l1:
        is_subset = False
        break

print(is_subset)
