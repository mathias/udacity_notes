# Python is named after Monty Python? Ok.

# 1.6
weeks = 7

daysInWeek = 7
hoursInDay = 24
minutesInHour = 60

print weeks * daysInWeek * hoursInDay * minutesInHour

# 1.10 Backus Naur Form
# <non-terminal> -> replacement
# Once we get to a terminal, we're done, we're finished
# We start at the top of the rules, and keep replacing until we're at the terminal for each.

# 1.17
speed_of_light = 299792458.0 # m / s
cycles_per_second = 2700000000.0 # cycles / s

print speed_of_light * (1 /cycles_per_second)
# 0.11 => roughly 11 centimeters
