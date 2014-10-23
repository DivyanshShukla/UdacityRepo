import webbrowser
import time

breaks = 3
count = 0
print("This program started on" + time.ctime())
while(count < breaks):
    print("Browser open number" + (str)(count))
    time.sleep(10)
    webbrowser.open("http://www.youtube.com")
    count = count+1
