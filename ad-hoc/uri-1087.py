# submissão: 06/04/2024
# há uma forma mais sucinta de fazer este exercício, prestando atenção no padrão ao invés de cobrir todos os casos.

def diagonal_um(m, n, p, q):
    
    while m > 1 and  n > 1: #diagonal esquerda baixo 
        m -= 1
        n -= 1
        
        if m == p and n == q:
            return True
        
    while m < 8 and n < 8: #diagonal direita cima
        m += 1
        n += 1
        
        if m == p and n == q:
            return True
        
    return False

def diagonal_dois(m, n, p, q):
    
    while m < 8 and n > 1: #diagonal direita baixo
         m += 1
         n -= 1
         
         if m == p and n == q:
             return True
            
    while m > 1 and n < 8: #diagonal direita cima
        m -= 1
        n += 1
        
        if m == p and n == q:
            return True
        
    return False

def horizontal(m, n, p, q):
    
    while m > 1: # horizontal esquerda
        m -= 1
        
        if m == p and n == q:
            return True
        
    while m < 8 : #horizontal direita
        m += 1
        
        if m == p and n == q:
            return True
        
    return False

def vertical(m, n, p, q):
    
    while n > 1: # vertical baixo
        n -= 1
        
        if m == p and n == q:
            return True
    
    while n < 8: #vertical cima
        n += 1
        
        if m == p and n == q:
            return True
        
    return False
        
while True:
    
    a, b, c, d = map(int, input().split())
    
    if a == b == c == d == 0:
        break
    
    elif a == c and b == d:
        print(0)
        
    elif  diagonal_um(a,b,c,d) or diagonal_dois(a,b,c,d) or horizontal(a,b,c,d) or vertical(a,b,c,d):
        print(1)
    
    else:
        print(2)
