def solution(phone_number):
    answer = phone_number[-4:]
    blind = ""
    length = len(phone_number) - 4
    for i in range(length):
        blind += "*"
    return blind + answer
