i, j, sum = 0, 1, 0

while j < 4e6 do
  i, j = j, i+j
  if j % 2 == 0
    sum += j
  end
end

puts sum
