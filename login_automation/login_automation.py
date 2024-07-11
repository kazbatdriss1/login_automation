from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to login to GitHub
def login_github(driver, username, password):
    driver.get("https://github.com/login")
    driver.find_element(By.ID, "login_field").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.NAME, "commit").click()
    print("login to GitHub Successfully")


# Function to login to Zone01oujda
def login_zone(driver, username, password):
    driver.get("https://learn.zone01oujda.ma/")
    driver.find_element(By.ID, "email-field").send_keys(username)
    driver.find_element(By.ID, "password-field").send_keys(password)
    driver.find_element(By.ID, "authenticate-button").click()
    print("login to Zone01oujda Successfully")


# Function to login to Spotify
def login_spotify(driver, username, password):
    driver.get("https://accounts.spotify.com/en/login")
    driver.find_element(By.ID, "login-username").send_keys(username)
    driver.find_element(By.ID, "login-password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    print("login to Spotify Successfully")

# Main script
if __name__ == "__main__":
    
    github_username = "username"
    github_password = "password"
    zone_username = "username"
    zone_password = "password"
    spotify_username = "username"
    spotify_password = "password"
    
    driver = webdriver.Chrome()

    # Open a new tab and switch to it for GitHub login
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    login_github(driver, github_username, github_password)

    # Open another new tab and switch to it for Zone login
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[2])
    login_zone(driver, zone_username, zone_password)

    # Switch back to the first tab for Spotify login
    driver.switch_to.window(driver.window_handles[0])
    login_spotify(driver, spotify_username, spotify_password)

    # Optionally, you can close the browser at the end
    # Keep the browser open for interaction
    input("Press Enter to close the browser...")
    driver.quit()
