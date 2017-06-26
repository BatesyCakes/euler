#Computes the difference between the square sum and the sum of squares of a number 'n'
def sum_square_difference(n):

  total = 0
  sum_squares = 0
  square_sums = 0

  for i in range(n+1):
    sum_squares += i * i
    total += i

  square_sums = total * total
  difference = (square_sums - sum_squares)
  return difference

print(sum_square_difference(100))
  
