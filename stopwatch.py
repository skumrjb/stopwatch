"""
From the book Automate the Boring stuff with Python pdf - Chapter 15 Pg 338

• Find the current time by calling time.time() and store it as a timestamp at the start of the program,
   as well as at the start of each lap.
• Keep a lap counter and increment it every time the user presses enter.
• Calculate the elapsed time by subtracting timestamps.
• Handle the KeyboardInterrupt exception so the user can press ctrl-C to quit.
"""
import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit')
input()
print('Started')

startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\n Done')