# 1.39 Final quiz
page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'
start_link = page.indexOf('<a href=')
start_quote = page.indexOf('"', start_link)
end_quote = page.indexOf('"', start_quote+1)

url = page[start_quote+1..end_quote-1]

# Note that we have to place with indexes differently here in JavaScript strings! Otherwise, it is basically the same.
