n = input()
s1 = set(input().split())
b = input()
s2 = set(input().split())
nb = s1.intersection(s2)

print(len(nb))