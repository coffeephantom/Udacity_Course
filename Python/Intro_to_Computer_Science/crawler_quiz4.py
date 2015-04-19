#!usr/bin/python
#-*-coding:utf-8-*-
#crawler_quiz4.py

#!usr/bin/python
#-*-coding:utf-8-*-
# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if start_link != -1:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
    else:
        return None,0

def get_all_links(page):
    links=[]
    while 1:
        url,endpos=get_next_target(page)
        if url:
            links.append(url)
            page=page[endpos:]
        else:
            break
                 

