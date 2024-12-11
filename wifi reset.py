from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


class Reset:

    options = Options()
    options.add_argument("--headless")

    def __init__(self):
        self.driver = webdriver.Chrome(options=self.options)
        print("Browser window opened")

    def launchbrowserAndlogin(self, wait_time: float):
        wifi_password = "$pongePlug"
        url = "http://192.168.8.1/html/index.html#home"
        self.driver.get(url)
        self.driver.implicitly_wait(10)

        password_field = self.driver.find_element(By.ID, "login_password")
        password_field.clear()
        password_field.send_keys(wifi_password)
        time.sleep(2.5)

        login_button = self.driver.find_element(By.ID, "login_btn")
        login_button.click()
        time.sleep(wait_time)

    def reset(self):
        reboot_button = self.driver.find_element(By.CLASS_NAME, "ic_reboot")
        time.sleep(2)
        reboot_button.click()

        self.driver.implicitly_wait(5)
        continue_button = self.driver.find_element(
            By.XPATH,
            "/html[@id='html']/body/div[@id='submit_light']/div[@class='margin_bottom_box2 color_Darkgray color_background_white']/div[2]/div[@class='btn_normal_short pull-left margin_left_12']",
        )
        time.sleep(2)
        continue_button.click()
        print("Wifi is reset")
        time.sleep(5)

        # change the time.sleep into an implicitly wait after pressing login button


# create the main function outside of the class. only create the object when needed after the input is done


def main():
    # input to choose the method
    correct_option = False
    while not correct_option:
        mode = (
            input("Press '1' to login and '2' to restart the wifi or 'q' to quit: ")
            .upper()
            .strip()
        )
        choices = ["1", "2", "Q"]
        if mode not in choices:
            continue
        elif mode == choices[0]:
            correct_option = True
            reset = Reset()
            reset.launchbrowserAndlogin(200)
        elif mode == choices[1]:
            correct_option = True
            reset = Reset()
            reset.launchbrowserAndlogin(5)
            reset.reset()
        elif mode == choices[2]:
            print("successfully quit")
            time.sleep(2)
            quit()


main()
