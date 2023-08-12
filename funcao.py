from itertools import combinations as combinacoes
def fatorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(result)
    return result

def fatorial_(n):
    if n == 1:
      return n
    else:
      return n * fatorial_(n-1)



def escrever(x):
    with open("chat.txt", "w") as f:
        f.write(x)