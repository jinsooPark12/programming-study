def solution(phone_book):
    hash = dict()
    for i in phone_book:
        hash[i] = 1
    for j in phone_book:
        target = ""
        for k in j:
            target += k
            if target in hash and target != j:
                return False
    return True