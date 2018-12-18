
def is_possible(arr, m, curr_index, prime_list):
    if m == 0 and curr_index == len(arr) -1:
        return True
    if m != 0 and curr_index >= 0 and curr_index < len(arr):
        for prime_factor in prime_list[curr_index]:
            return (is_possible(arr ,m-1, curr_index - prime_factor, prime_list) or
                    is_possible(arr, m-1, curr_index + prime_factor, prime_list))
    return False

if __name__ == '__main__':
    
    prime_list_till_N = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    T = int(raw_input())
    for i in range(T):
        n = int(raw_input())
        prime_list = []
        arr = map(int, raw_input().strip().split())
        for num in arr:
            list1 = []
            for prime in prime_list_till_N:
                if num % prime == 0 and prime < n:
                    list1.append(prime)
            prime_list.append(list1)
                
        print(prime_list)
        m = int(raw_input())
        if is_possible(arr, m, 0, prime_list):
            print('YES')
        else:
            print('NO')
