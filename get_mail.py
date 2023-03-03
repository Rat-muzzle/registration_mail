from selenium_stealth import stealth
from seleniumwire import webdriver
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, wait
from multiprocessing import Queue, cpu_count
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
import os
import pyautogui

# opcgpfmipidbgpenhmajoajpbobppdil
# Расширение: C:\Users\ratmu\AppData\Local\Google\Chrome\User Data\Default\Extensions\opcgpfmipidbgpenhmajoajpbobppdil\22.11.9.0_0.crx
# Файл ключей: C:\Users\ratmu\AppData\Local\Google\Chrome\User Data\Default\Extensions\opcgpfmipidbgpenhmajoajpbobppdil\22.11.9.0_0.pem

chrome = r'C:\Users\ratmu\PycharmProjects\beastfi.org\chromedriver.exe'
options = webdriver.ChromeOptions()

# options.add_argument("--headless")  # прячет браузер
# // Указываем профиль в передаваемых опциях
# ChromeOptions options = new ChromeOptions();
# options.add_argument(r'--user-data-dir=C:\Users\ratmu\AppData\Local\Google\Chrome\User Data\Default')
# options.add_argument(r'--profile-directory="Profile 40"')
# // Создаем браузер
# WebDriver driver = new ChromeDriver(options);
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("prefs", "preferences")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-breakpad")  # Disables the crash reporting. ↪
options.add_argument("--disable-client-side-phishing-detection")
options.add_argument("--disable-cast")
options.add_argument("--disable-cast-streaming-hw-encoding")
options.add_argument("--disable-cloud-import")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-session-crashed-bubble")
options.add_argument("--disable-ipv6")
options.add_argument("--allow-http-screen-capture")
options.add_argument("--start-maximized")
prefs = {"profile.managed_default_content_settings.images": 1}
options.add_experimental_option("prefs", prefs)
# options.add_argument("blink-settings=imagesEnabled=true")
options.add_argument("start-maximized")
options.add_argument("--disable-notifications")

options.add_argument(
    f"user-agent=Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36")
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36
# user-agent=Opera/9.80 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36
# seleniumwire_options=proxy_options включение прокси


driver = webdriver.Chrome(
    options=options,
    executable_path=chrome,
)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
stealth(driver,
        languages=["ru-RU"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        run_on_insecure_origins=True
        )

time.sleep(5)
ls = []
driver.switch_to.window(driver.window_handles[0])
driver.get(url='https://zovut.com/generator-podbora-angliyskikh-imen-familiy/')
global x
x = 0
driver.execute_script("window.open('https://consensys.net/shanghai-capella-upgrade?utm_campaign=Shanghai%2FCapella&utm_"
                      "medium=email&_hsmi=248497168&_hsenc=p2ANqtz-8JcBejUAVjXdE10gp8Azrbptce09xxv8zJrhqjQgskOpOhwGQwW_"
                      "pvnINw6QdxjqWWHn93eYBzTJSGQMTtbfsE5OUJpQ&utm_content=248497168&utm_source=hs_email');")

while True:

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    if x == 0:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[1]/main/article/div/div/div/div[3]/input'))).click()
        x = 1
    if x == 1:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[1]/main/article/div/div/div/div[2]/input'))).click()
        x = 0

    name = WebDriverWait(driver, 3).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="generated-name"]')))
    b = list(name.text.split(' '))
    mail = f'{b[0].lower()}_{b[1].lower()}@etoz.xyz'


    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    inputs_1 = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="email-38705ada-7aca-4178-a8ba-7de502a2229a"]')))

    # driver.execute_script("arguments[10].setAttribute('value',b[0])", inputs_1)
    # driver.execute_script("arguments[11].setAttribute('value',mail)", inputs_2)

    inputs_1.clear()
    inputs_1.send_keys(mail)
    time.sleep(1)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="hsForm_38705ada-7aca-4178-a8ba-7de502a2229a"]/div[5]'))).click()

    WebDriverWait(driver, 3600).until(EC.presence_of_element_located(
        (By.XPATH,
         "//*[contains(text(), 'Thanks for submitting the form.')]")))

    driver.refresh()


    print(mail)

    try:
        with open('mail_red_2.txt', "a") as fw:
            fw.write(f'{mail}\n')
    except Exception:
        pass
    # pyautogui.write(b[0])
    #
    # pyautogui.write(f'{b[0].lower()}_{b[1].lower()}@etoz.xyz')

# try:
#     ok_x, ok_y = pyautogui.locateCenterOnScreen('foxy_not_now.png',
#                                                 confidence=0.97,
#                                                 region=(1050, 201, 100, 60))
#     pyautogui.click(3420, 252)
# except TypeError:
#     pass
