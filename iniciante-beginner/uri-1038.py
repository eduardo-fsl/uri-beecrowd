# submissão: 26/08/2021

x, y = map(int, input().split())

if x == 1:
    print(f"Total: R$ {(4.00 * y):.2f}")
if x == 2:
    print(f"Total: R$ {(4.50 * y):.2f}")
if x == 3:
    print(f"Total: R$ {(5.00 * y):.2f}")
if x == 4:
    print(f"Total: R$ {(2.00 * y):.2f}")
if x == 5:
    print(f"Total: R$ {(1.50 * y):.2f}")