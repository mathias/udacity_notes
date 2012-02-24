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

# 1.38 Extracing Links
# ... <a href="{url}"> ...
page = '<div id="top_bin">	<div id="top_content" class="width960">		<div class="udacity float-left">			<a href="/">'
page  # has the content of a web page as a string

a_href = '<a href='

start_link = page.find(a_href)

# 1.39 Final quiz
page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'
start_link = page.find('<a href=')

link_tag = page[start_link:]

url_str_open = link_tag.find('"')+1

url_str_close = link_tag.find('">', url_str_open)

url = link_tag[url_str_open:url_str_close]

# Instructor's answer to 1.39:
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote+1)
url = page[start_quote+1:end_quote]
