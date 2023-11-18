def solution(num_list):
    product = 1
    for i in num_list:
        product *= i 
        all_sum = sum(num_list)
        
    if product < all_sum **2:
        return 1
    else:
        return 0
