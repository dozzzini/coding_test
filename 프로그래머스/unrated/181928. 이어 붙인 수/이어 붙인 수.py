def solution(num_list):
    odd = 0
    even = 0
    for num in num_list:
        if num % 2 == 0:
            even = even*10 + num
        else:
            odd = odd*10 + num
    return even+odd