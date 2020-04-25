
def solution(N):
    # write your code in Python 3.6
    # take into account when something starts and stop
    #
    # checking bits one by one
    count_start = False
    counter = 0
    max_counter = 0
    for i in range(32):
        print(i)
        id_one = (N & (1 << i)) > 0
        print(id_one)
        if id_one:
            if count_start:
                max_counter = max(max_counter, counter)
            count_start = True
            counter = 0
        else:
            if count_start:
                counter += 1
    return max_counter

print(solution(1041))
