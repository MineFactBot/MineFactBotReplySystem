import re

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import pickle
import time

options = Options()
options.add_argument("--headless")
print("Starting chrome driver...")
driver = webdriver.Chrome(chrome_options=options)
driver.get("about:blank")


# noinspection PyBroadException
def sendReply(text, url):
    """
    Sends a tweet with the given text
    :param url: The url of the tweet
    :param text: The text of the tweet
    """
    start = time.perf_counter()
    print("Logging in...")
    driver.get(url)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(url)
    time.sleep(2)
    print(f"Logged in in {time.perf_counter() - start} seconds")
    while True:
        try:
            field = driver.find_element("class name", 'public-DraftEditor-content')
            break
        except Exception as e:
            pass
    print("Sending tweet...")
    field.send_keys(
        deEmojify(text.strip()))
    time.sleep(7)
    field.send_keys(
        Keys.LEFT_CONTROL, Keys.ENTER)
    time.sleep(7)
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    driver.get("about:blank")


def deEmojify(text):
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)
