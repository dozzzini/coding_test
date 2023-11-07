def solution(slice, n):
    answer = 0
    # 10조각을 7사람이 한 조각 이상 먹으려면 2판 필요
    # 12조각을 4사람이 한 조각 이상 먹으려면 3판 필요
    # slice 조각을 n사람이 한 조각 이상 먹으려면 몇 판 필요?
    if  n%slice !=0:
        answer = (n // slice)+1
    else:
        answer = n // slice
    return answer