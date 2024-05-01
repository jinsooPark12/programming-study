def solution(sticker):
    index = len(sticker)
    dp1 = [sticker[i] for i in range(0, index-1)]
    dp2 = [sticker[j] for j in range(1, index)]

    if index <= 2:
        return max(sticker)

    for i in range(1, index-1):
        if i == 1:
            dp1[i] = max(dp1[i-1], dp1[i])
            dp2[i] = max(dp2[i-1], dp2[i])
        else:
            dp1[i] = max(dp1[i-1], dp1[i-2] + dp1[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + dp2[i])

    return max(dp1[index-2], dp2[index-2])