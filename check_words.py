import urllib

def read_text():
    #open
    document = open("/Users/Cperry24/Desktop/movie_quotes.txt")
    #read
    content = document.read()
    #print
    print(content)
    #close
    document.close()
    check_words(content)

def check_words(word):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+word)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("We have detected bad words in your program!")
    elif "false" in output:
        print("You have written a clean document!")
    else:
        print("Could not scan your document!")


read_text()
