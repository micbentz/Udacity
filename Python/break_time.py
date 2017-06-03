import webbrowser
import time


print("Program started on: " + time.ctime())
while True:
    # Sleep for 1.5 hours
    time.sleep(60 * (60))
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
