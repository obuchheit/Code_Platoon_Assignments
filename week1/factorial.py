def factorial(num):
    answer = num
    explanation = ''


    while num > 1: 
        explanation += str(num) + ' * '

        answer += answer * (num - 2)
        print(answer)
        num -= 1

    explanation += '1'
    return answer, explanation

print(factorial(5))