from urllib import request
from urllib import parse

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(QUERY):
    #print("http://www.wdylike.appspot.com/?q="+QUERY)
    connection = request.urlopen("http://www.wdylike.appspot.com/?q="+parse.quote(QUERY))
    output = connection.read().decode('utf-8')
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("No curse words")
    else:
        print("Could not scan document")

read_text()
