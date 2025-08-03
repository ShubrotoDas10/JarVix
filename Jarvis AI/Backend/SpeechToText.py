from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def SpeechRecognition():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--use-fake-ui-for-media-stream')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Launch Chrome browser
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.get("https://watson-speech-to-text-demo.ng.bluemix.net/")


    print("Speak something... (waiting for 10 seconds)")
    time.sleep(10)  # Allow user to speak

    try:
        # Wait up to 20 seconds for the output element to be present
        wait = WebDriverWait(driver, 20)
        output_element = wait.until(EC.presence_of_element_located((By.ID, "output")))

        # Get the text from the output
        text = output_element.text.strip()

        if not text:
            print("No speech detected.")
        else:
            print(f"You said: {text}")

    except Exception as e:
        print(f"Error: {e}")
        text = None
    finally:
        driver.quit()

    return text

# Run the function
if __name__ == "__main__":
    result = SpeechRecognition()
