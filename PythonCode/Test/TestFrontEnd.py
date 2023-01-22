"""
System testing for the right execution of the app (FrontEnd)

As for now it's not working.
Included in the project to save the progress for future reference.
"""

from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome(executable_path=r'./chromedriver')
# driver.get('https://employeeprediction.streamlit.app/')
# WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div[1]/div/div[5]/div/button/div/p'))).click()

# driver.implicitly_wait(60)
# l = driver.find_element("xpath",
#                         '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div[1]/div/div[5]/div/button/div/p')
# driver.execute_script("arguments[0].click();", l)

# print("Page title is: ")
# print(driver.title)
# /html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div[1]/div/div[5]/div/button/div/p


class AppTesting(BaseCase):

    def test_leaves(self):
        self.open("https://employeeprediction.streamlit.app/")
        self.sleep(30)
        self.click_xpath(
            '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div[1]/div/div[5]/div/button/div/p')
        self.click('button:contains("Begin!")', timeout=30)
        self.select_option_by_text("select_age", "37")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_gender", "Female")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_city", "Pune")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_education", "Bachelor")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_year", "2014")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_experience", "5")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_payment_tier", "2")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_ever_benched", "No")
        self.click('button:contains("See Results!")')
        self.assert_text(
            "WATCH OUT! Our prediction says that, in two years, " +
            "the employee WILL LEAVE the company!!!")

    def test_stays(self):
        self.open("https://employeeprediction.streamlit.app/")
        self.click('button:contains("Begin!")')
        self.select_option_by_text("select_age", "18")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_gender", "Male")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_city", "Bangalore")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_education", "Bachelor")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_year", "2012")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_experience", "0")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_payment_tier", "3")
        self.click('button:contains("Next")')
        self.select_option_by_text("select_ever_benched", "No")
        self.click('button:contains("See Results!")')
        self.assert_text(
            "Our prediction says that, probably, the employee will NOT " +
            "leave the company for the next two years.")
