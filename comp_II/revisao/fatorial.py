# Só pra ver se eu lembro como se faz um fatorial

def fatorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result

print(fatorial(5))