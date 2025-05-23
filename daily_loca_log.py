from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from selenium.webdriver.support.ui import Select
import traceback
import holidays

today = datetime.datetime.today().weekday() 
today_year_month_day = datetime.date.today()

username = "username"  
password = "password"

if today_year_month_day in holidays.UnitedStates(years=datetime.date.today().year):
    print("휴일입니다.")
    exit()
elif today in [1,2,3]: 
    location_name = "HAEA (HMA)"
elif today in [0,4]:  
    location_name = "SOLOMON (Irvine Office)"
else:
    exit()

options = webdriver.ChromeOptions()
# options.add_argument("incognito")
options.add_argument('--window-size=360,640')
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://hr.solomonamerica.com")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.ID, "pw"))).send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(),' Log In ')]").click()


    time.sleep(3)  
    location_dropdown = Select(driver.find_element(By.ID, "predefinedLocation"))
    location_dropdown.select_by_visible_text(location_name)

    driver.find_element(By.ID, "saveButton").click()

    time.sleep(2)
except Exception as e:
    print("오류 발생: 코드 확인 필요[" + str(e) + "]")
    # traceback.print_exc()

finally:
    driver.quit()
