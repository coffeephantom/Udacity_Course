import urllib

def read_text():
    quotes=open("/Users/coffeephantom/Downloads/movie_quotes.txt")
    contents_of_file=quotes.read()
    check_profanity(contents_of_file)
    print contents_of_file
    quotes.close()


def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true":
        print "Profanity Alert"
    else:
        print "No curse Words"

read_text()