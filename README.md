# Collatz Conjecture Sequence Generator
An attempt at writing a Collatz sequence generator in Python.

```python
current_n = int(input("Enter a starting value: "))
original_n = current_n
iterations = 0
highest_number_reached = 0
times_above_n = 0

print("")

while current_n != 1:
  if current_n % 2 == 0:
    current_n = current_n / 2
  else:
    current_n = (3 * current_n) + 1
  
  if current_n > highest_number_reached:
    highest_number_reached = int(current_n)

  if current_n > original_n:
    times_above_n += 1

  iterations += 1
  print(int(current_n))

print("\nStopping time: " + str(iterations))
print("Highest number reached: " + str(highest_number_reached))
print("Times above n: "  + str(times_above_n))
```
