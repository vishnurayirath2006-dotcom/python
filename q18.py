
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome browser
driver = webdriver.Chrome()

try:
    # Open DemoQA webpage
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()

    # Create wait object
    wait = WebDriverWait(driver, 15)

    # User details
    name = "Vishnu"
    email = "vishnu@gmail.com"
    current_address = "Thrissur, Kerala"
    permanent_address = "Kochi, Kerala"

    # Enter full name
    wait.until(EC.visibility_of_element_located(
        (By.ID, "userName")
    )).send_keys(name)

    # Enter email
    driver.find_element(By.ID, "userEmail").send_keys(email)

    # Enter current address
    driver.find_element(By.ID, "currentAddress").send_keys(
        current_address
    )

    # Enter permanent address
    driver.find_element(By.ID, "permanentAddress").send_keys(
        permanent_address
    )

    # Submit the form
    submit = wait.until(EC.element_to_be_clickable(
        (By.ID, "submit")
    ))

    driver.execute_script("arguments[0].click();", submit)

    # Wait for output
    output = wait.until(EC.visibility_of_element_located(
        (By.ID, "output")
    ))

    # Verify entered details
    result = output.text

    if (name in result and
        email in result and
        current_address in result and
        permanent_address in result):

        print("Form submitted successfully!")
        print("All details verified successfully.")

    else:
        print("Verification failed!")

    # Display submitted details
    print("\nSubmitted Details:")
    print(result)

finally:
    # Close browser
    driver.quit()
    print("\nBrowser closed successfully.")
