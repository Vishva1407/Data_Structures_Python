def linear_search(key,num_list):
    for i in num_list:
        if i == key:
            return 1
    return 0

print(linear_search(1,[5,4,3,2,1]))