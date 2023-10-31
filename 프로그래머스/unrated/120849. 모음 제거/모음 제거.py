def solution(my_string):
    remove = ['a','e','i','o','u']
    for i in remove:
        my_string = my_string.replace(i,'')
    return my_string