def fib(num):
    answer = 0
    curr_ans = 1
    prev_ans = 0

    if num == 1:
        return 1 
    
    else:
        for i in range(1, num):
            answer = curr_ans + prev_ans
            prev_ans = curr_ans
            curr_ans = answer

    return answer

print(fib(1))