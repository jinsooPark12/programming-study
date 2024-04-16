def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        num1 = phone_book[i]
        num2 = phone_book[i+1]
        if num1 == num2[:len(num1)]:
            return False
    return True