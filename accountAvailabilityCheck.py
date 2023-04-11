from selenium import webdriver

# Open Google sign-up page
driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signup")

# Quit driver
driver.quit()


