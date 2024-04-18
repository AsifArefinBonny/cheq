import os
import configparser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests

# Read the URL from the config file
config = configparser.ConfigParser()
config.read('config.ini')
url = config.get('selenium', 'url')

# Initialize the webdriver (in this case, Chrome)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Locate and click on the link using the provided strategy
pdfLink = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Download a Printable PDF of this Cheat Sheet"))
)
pdfLink.click()

# Switch to the new tab
try:
    wait = WebDriverWait(driver, 30)
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
except TimeoutException:
    print("Error: New tab did not open within the specified timeout.")
    driver.quit()
    exit()

# Wait for the PDF to load
time.sleep(5)

# Download the PDF file
pdf_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "Selenium Cheat Sheet 2022.pdf")
pdf_url = driver.current_url
response = requests.get(pdf_url)
with open(pdf_file_path, 'wb') as file:
    file.write(response.content)

# Verify if the PDF file has been downloaded
if os.path.exists(pdf_file_path):
    print(f"PDF file downloaded successfully at: {pdf_file_path}")
else:
    print("PDF file download failed.")

# Close the browser
driver.quit()