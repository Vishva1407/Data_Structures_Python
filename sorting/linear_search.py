def linear_search(key,num_list):
    for i,num in enumerate(num_list):
        if num == key:
            return 1,i
    return 0

if __name__ == "__main__":
    num_list = [1,2,3,4,5,6,7]
    key = 5
    found,index = linear_search(key,num_list)
    if found:
        print("The given element is found at ",index)
    else:
        print("The element is not found")
