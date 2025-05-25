def check(n):
    if n==3:
        return True

    if n%3!=0:
        return False
    return check(n//3)
numbers=int(input())
print(check(numbers))
