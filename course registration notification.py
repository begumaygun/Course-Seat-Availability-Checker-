#quota means kontenjan
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound


driver = webdriver.Chrome()


driver.get("*URL*")


username = "XXXXXXX"
password = "XXXXXXX"


username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='ctl06_txtKullaniciAdi']")) #username Xpath
)
username_input.send_keys(username)


password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='ctl06_txtSifre']"))#password Xpath
)
password_input.send_keys(password)


password_input.send_keys(Keys.RETURN)


onay_butonu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*buttons Xpath*'))
)
onay_butonu.click()


kontenjan_xpath_1 = "//*class Xpath*"
kontenjan_xpath_2 = "//*another class Xpath*"


kontenjan_xpaths = [kontenjan_xpath_1, kontenjan_xpath_2]

print("Checking ...")

while True:
    try:
        driver.refresh()

        
        for xpath in kontenjan_xpaths:
            kontenjan_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            kontenjan_text = kontenjan_element.text.strip()

           
            if "Kalan:" in kontenjan_text:
                kontenjan_value = kontenjan_text.split(":")[1].strip()  
                if kontenjan_value.isdigit():
                    kontenjan_value = int(kontenjan_value)
                    print(f"quota: {kontenjan_value}")
                    if kontenjan_value > 0:
                        print(f"🎉 found quota: {kontenjan_value}")
                        winsound.Beep(1000, 1000)
                        break

    except Exception as e:
        print(f"error: {e}")
    
    time.sleep(30)
