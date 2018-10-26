powerful_digits = 0
for i in range(1,50):
  for j in range(1,50):
    if len(str(i**j)) == j:
      powerful_digits += 1

print(powerful_digits)
