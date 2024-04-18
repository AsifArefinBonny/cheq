from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Path to the directory where the file is expected to be downloaded
download_directory = "/"

# URL of the webpage containing the link to download the PDF file
url = "https://intellipaat.com/blog/tutorial/selenium-tutorial/selenium-cheat-sheet/"

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get(url)

# Find the link to download the PDF file using CSS selector
pdf_link = driver.find_element(By.CSS_SELECTOR, "a[href*='Selenium-Cheat-Sheet']")

# Get the href attribute of the <a> element
pdf_link_url = pdf_link.get_attribute("href")

# Click on the link to initiate the download
pdf_link.click()

# Wait for the file to download
time.sleep(5)  # Adjust the sleep time as needed

# Verify if the file has been downloaded successfully
file_path = os.path.join(download_directory, "Selenium-Cheat-Sheet-2022.pdf")
if os.path.exists(file_path):
    print("PDF file downloaded successfully.")
    # You can also add further checks on the file if needed
else:
    print("PDF file download failed.")

# Close the WebDriver
driver.quit()
