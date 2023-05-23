from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

import time
import os
import pickle
import login_details
import pandas as pd
from pathlib import Path

username = login_details.username
password = login_details.password
netflix_user = login_details.netflix_user

class LoadActivityNetflix():
    def __init__(self, username, password, netflix_user, download_path, webdriver_path) -> None:
        self.login = "https://www.netflix.com/de/login"
        self.acitvity = "https://www.netflix.com/viewingactivity"
        self.nf_user = netflix_user
        self.username = username
        self.password = password
        self.pickle_file = f"cookies-{self.nf_user}.pkl"
        os.makedirs(download_path, exist_ok=True)

        chrome_options = Options()
        # chrome_options.add_argument("--headless=new")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        # Erstelle eine neue Instanz des Chrome-Webdrivers mit den angegebenen Optionen
        self.driver = webdriver.Chrome(executable_path=webdriver_path, chrome_options=chrome_options)
        self.wait = WebDriverWait(self.driver, 60)

    def login_user(self):
        # Öffne Netflix-Anmeldeseite
        if not self.load_pickle():
            self.wait.until(ec.visibility_of_element_located((By.ID, "id_userLoginId"))).send_keys(self.username)
            self.wait.until(ec.visibility_of_element_located((By.ID, "id_password"))).send_keys(self.password)
            self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-submit"))).click()

            time.sleep(10)
            elements = self.driver.find_elements(By.CLASS_NAME, "profile-name")

            # Durchsuche die gefundenen Elemente nach dem gewünschten Text
            element = None
            for elem in elements:
                if elem.text == self.nf_user:
                    element = elem
                    break

            # Überprüfe, ob das Element gefunden wurde
            if element:
                # Warte auf die Sichtbarkeit des Elements
                self.wait.until(ec.visibility_of(element)).click()
            else:
                print("Das Element wurde nicht gefunden.")

            # time.sleep(60)
            cookies = self.driver.get_cookies()

            # Speichere die Cookies in einer Datei
            with open(self.pickle_file, "wb") as file:
                pickle.dump(cookies, file)

    def load_pickle(self):
        self.driver.get(self.login)
        if os.path.exists(self.pickle_file):
            with open(self.pickle_file, "rb") as file:
                cookies = pickle.load(file)

            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get(self.login)
            return True
        else:
            return False

    def dl_activity(self):
        self.driver.get(self.acitvity)
        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "viewing-activity-footer-download"))).click()
        
        # Warte auf den erfolgreichen Download
        time.sleep(50)
        self.driver.quit()


path = Path(__file__).parent.absolute()
download_path = os.path.join(path, "downloads/")
webdriver_path = "chromedriver.exe"

nf = LoadActivityNetflix(
    username=username,
    password=password,
    netflix_user=netflix_user,
    download_path=download_path,
    webdriver_path=webdriver_path
)

# nf.login_user()
# nf.dl_activity()

# Schließe den Webdriver und beende den Browserprozess
file_list = os.listdir(download_path)
file_list.sort(key=lambda x: os.path.getmtime(os.path.join(download_path, x)))
newest_file = file_list[-1]
file_path = os.path.join(download_path, newest_file)
df = pd.read_csv(file_path) 
print(df.head())