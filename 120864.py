import re


def solution(my_string):
    answer = 0
    numbers = re.findall("\d+", my_string)

    for i in range(len(numbers)):
        answer += int(numbers[i])

    return answer