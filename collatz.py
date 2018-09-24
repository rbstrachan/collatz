current_n = int(input("Enter a starting value: "))
original_n = current_n
iterations = 0
highest_number_reached = 0
times_above_n = 0
odd_count = 0
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

print("\nStopping time: " + str(iterations))
print("Highest number reached: " + str(highest_number_reached))
print("Times above n: "  + str(times_above_n))
print("Odd count: " + str(odd_count))
print("Even values between odd numbers: " + str(even_between_odd))
print("No. of y-sets traversed: " + str(len(even_between_odd)))
