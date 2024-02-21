def eq2g(a:int, b:int, c:int):
  if a == 0:
    return -c/b
  else:
    d = (b**2 - 4*a*c) ** 0.5
    x1 = (-b - d) / (2 * a)
    x2 = (-b + d) / (2 * a)
    return x1, x2
  
print(eq2g(1, -2, 0))
help(eq2g)

# anotações
print(eq2g.__annotations__)