def countDigits(n: int) -> int:
    temp = n
    count = 0
    while temp>0:
        num = temp%10
        if num != 0 and n%num == 0:
            count+=1
        temp = temp//10
    return count
