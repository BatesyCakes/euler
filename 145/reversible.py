

result = 0

def are_odds(n):
  x = str(n)
  for i in x:
    if int(i)%2 == 0:
      return False
  return True

for i in range(11, 10**9):
 if i %10 == 0:
   continue
 j = i + int(str(i)[::-1])
 if j%2 == 0:
   continue
 else:
   if are_odds(j):
     result += 1

print(result)
