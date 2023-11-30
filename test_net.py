import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.parametrize("username, password, email",
                         [
                             ("gardenligh", "hellowworld12345", "gardenligh3@gmail.com"),
                             ("mandgard", "alice2345", "mandgard4@example.com"),
                             ("akashgray", "alice2345", "akashgray@gmail.com"),
                             # Add more data sets here
                         ]
                         )
def test_submit_login_form(username, password, email):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.thiscodeworks.com/extension/signup")

    # Fill out the form using the provided values
    username_field = driver.find_element(By.ID, "username-login")
    password_field = driver.find_element(By.ID, "password-login")
    email_field = driver.find_element(By.ID, "email-login")

    username_field.send_keys(username)  # Use the username argument
    password_field.send_keys(password)  # Use the password argument
    email_field.send_keys(email)        # Use the email argument

    #Submit the form
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    # Wait for success message to appear in the title
    WebDriverWait(driver, 10).until(EC.title_contains("Success"))

    #Check for success message in title
    title = driver.title

    # Check if the expected success message is present in the title
    assert "Success" in title, "'Success' is not in the title"
    driver.quit()


