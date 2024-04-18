# cheq

An automation test script that downloads pdf file from a website and stores in local system.

The main challenge here was to avoid using ChromeOptions, FirefoxOptions and Keyboard shortcuts - KeyEvents.

I've investigated and found some other possible ways to do that and some of the ways are:

1. Utilizing the requests library
2. Using the execute_script method of Selenium
3. Employing the urllib module
4. Integrating with a headless browser

But I could only successfully make the script with Utilizing the requests library & Using the execute_script method of Selenium.

1. The script with Utilizing the requests library:
2. The script using the execute_script method of Selenium:

# Setting up the environment

I used virtual environment and to setting up the virtual environment follow:

Command needs to run:

1. pip3 install pipenv
2. pipenv shell (It should launch a virtual environment & create a Pipfile)
3. pipenv install selenium (It'll create Pipfile.lock)
4. python script-request.py (The browser should open with the URL and should start executing the script automatically)

Note: My chrome browser version is: Version 124.0.6367.62 (Official Build) (x86_64)
