from selenium import webdriver

# Take user input for email
email = input("Enter email to check availability: ")

# Open Google sign-up page
driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signup")

# Quit driver
driver.quit()


