from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def SpeechRecognition():
    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--use-fake-ui-for-media-stream')  # auto allow mic
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--headless')  # mic won't work in headless mode

    driver = webdriver.Chrome(service=Service(), options=options)
    try:
        print("Opening Google Web Speech API demo...")
        driver.get("https://www.google.com/intl/en/chrome/demos/speech.html")

        wait = WebDriverWait(driver, 20)

        # Click "Start" button to begin listening
        start_button = wait.until(
            EC.element_to_be_clickable((By.ID, "start_button"))
        )
        start_button.click()
        print("Speak now... recording for 8 seconds")

        time.sleep(8)  # Let Chrome listen to you

        # Stop button click is optional — Google demo stops automatically on silence
        try:
            start_button.click()
        except:
            pass

        print("Processing speech...")

        # Wait for transcription text to appear
        result_span = wait.until(
            EC.presence_of_element_located((By.ID, "final_span"))
        )

        # Keep checking until we have some text or timeout
        start_time = time.time()
        text = ""
        while time.time() - start_time < 5:  # 5 seconds max wait
            text = result_span.text.strip()
            if text:
                break
            time.sleep(0.5)

        if text:
            print(f"You said: {text}")
        else:
            print("No speech detected.")

    except Exception as e:
        print(f"Error: {e}")
        text = None
    finally:
        driver.quit()

    return text

if __name__ == "__main__":
    SpeechRecognition()
