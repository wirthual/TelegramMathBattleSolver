# TelegramMathBattleSolver
Short python script to win mathbattle (Telegram gaming bot: https://telegram.org/blog/games)

###What you need:

1. Chrome Browser installed

2. Webdriver for Chrome: https://sites.google.com/a/chromium.org/chromedriver/

3. Python 2

4. Selenium for Python (e.g: install it with pip: ```pip install selenium```)

5. URL to your Mathbattle Game (looks like: https://tbot.xyz/math/#eyJ1IjoyNDUzNzU0NjMsIm4iOiJSYXB...')
   You can get this URL by opening the Mathbattle game from your desktop client. Then just copy the URL from the Browser

6. MathBattleSolver.py script

###Set these Variables in the script:
```python
GAME_URL = 'https://tbot.xyz/math/#eyJ1IjoyNDUzNzU0NjMsIm4iOiJSY...' #See point 5
WEBDRIVER_PATH = '/home/path/to/webdriver'                           #See point 2
NUMBER_OF_WINS = 5000                                                #Dont make it to obvious ;)
```
###Then start the script by typing: 
```python2 MathBattleSolver.py```

See a video here:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/PLc6rqnCgME/0.jpg)](http://www.youtube.com/watch?v=PLc6rqnCgME "Telegram Math Battle Solver")

Have fun :)
