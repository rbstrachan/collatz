current_n = int(input("Enter a starting value: "))
original_n = current_n
iterations = 0
highest_number_reached = original_n
times_above_n = 0
odd_count = 0
longest_even_run = 0
# number of even numbers between each odd instance
even_between_odd = [0]
index = 0

print("")

while current_n != 1:
  if current_n % 2 == 0:
    current_n = current_n / 2
    # adds one to the even count for the current index
    even_between_odd[index] += 1
  else:
    current_n = (3 * current_n) + 1
    odd_count += 1
    # creates a new value in the set and increments index value
    even_between_odd.append(0)
    index += 1
  
  if current_n > highest_number_reached:
    highest_number_reached = int(current_n)

  if current_n > original_n:
    times_above_n += 1

  iterations += 1
  print(int(current_n))

if even_between_odd[0] == 0:
  del even_between_odd[0]

for run in even_between_odd:
  if run > longest_even_run:
    longest_even_run = run

print("\nStarting number:..............  " + str(original_n))
print("Highest number reached:.......  " + str(highest_number_reached))
print("Number of Iterations:.........  " + str(iterations))
print("Number of times higher than n:  "  + str(times_above_n))
print("Odd number count:.............  " + str(odd_count))
print("Longest even-number run:......  " + str(longest_even_run))
print("\nLength of even runs: ")
print(str(even_between_odd))
