import webbrowser
import time

#program
i = 0
print("This program started one " + time.ctime())
while i < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=uq-gYOrU8bA")
    i = i + 1

