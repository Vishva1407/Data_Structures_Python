def Binary_Search(key,num_list):
    start = 0
    end = len(num_list)-1
    while start<=end:
        mid = int((start+end)/2)
        if key == num_list[mid]:
            return 1
        if key<num_list[mid]:
            end = mid-1
        if key>num_list[mid]:
            start = mid+1
    return 0
if __name__ == "__main__":
    print(Binary_Search(33,[1,11,22,33,44,55,66,77]))