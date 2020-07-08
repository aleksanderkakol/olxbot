import os
import codecs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pyautogui


class OLX:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.browser.get('https://www.olx.pl/')
        self.browser.implicitly_wait(5)

    def page_loading(self):
        while True:
            page_state = self.browser.execute_script('return document.readyState;')
            if page_state == 'complete':
                return page_state
            sleep(2)

    def accept_cookies(self):
        try:
            cookies = self.browser.find_element_by_class_name('cookie-close')
            cookies.click()
            self.page_loading()
        except NoSuchElementException:
            print(NoSuchElementException)
            return False
        return True

    def enter_phone_number(self):
        try:
            number = self.browser.find_element_by_name('verification[phone]')
            number.send_keys('123456789')
        except NoSuchElementException:
            print(NoSuchElementException)
            return False
        return True

    def new_advertisement(self):
        try:
            if self.page_loading():
                sleep(2)
                add_advertisement = self.browser.find_element_by_id('postNewAdLink')
                add_advertisement.click()
                self.page_loading()
        except NoSuchElementException:
            print(NoSuchElementException)
            return False
        return True

    def login(self):
        try:
            if self.page_loading():
                sleep(3)
                email = self.browser.find_element_by_id('userEmail')
                password = self.browser.find_element_by_id('userPass')
                email.send_keys('william211@wp.pl')
                password.send_keys('Mamalala11')
                login = self.browser.find_element_by_id('se_userLogin')
                login.click()
                self.page_loading()
        except Exception as ex:
            print(ex)
            return False
        return True

    def add_advertisement(self):
        try:
            if self.page_loading():
                self.title("Wynajem Kwater")
                self.category()
                self.icon()
                self.data_category()
                self.price("35")
                self.room_type()
                self.number_of_people()
                self.business_type()
                self.description()
                self.photos()
                self.location()
                self.phone_number("516 193 616")
                # self.submit()
                self.page_loading()
        except Exception as ex:
            print(ex)
            return False
        return True

    def title(self, text):
        try:
            title = self.browser.find_element_by_id('add-title')
            title.send_keys(text)
        except Exception as ex:
            print(ex)
            return False
        return True

    def category(self):
        try:
            category = self.browser.find_element_by_tag_name('dt')
            category.click()
        except Exception as ex:
            print(ex)
            return False
        return True

    def icon(self):
        try:
            icon = self.browser.find_element_by_id('cat-3')
            icon.click()
        except Exception as ex:
            print(ex)
            return False
        return True

    def data_category(self):
        try:
            data_category = self.browser.find_element_by_css_selector("a[data-category='1289']")
            data_category.click()
        except Exception as ex:
            print(ex)
            return False
        return True

    def price(self, value):
        try:
            price = self.browser.find_element_by_name('data[param_price][1]')
            price.send_keys(value)
        except Exception as ex:
            print(ex)
            return False
        return True

    def room_type(self):
        try:
            type_rooms = self.browser.find_element_by_id('targetparam137')
            type_room = type_rooms.find_element_by_tag_name('dt')
            type_room.click()
            room = type_rooms.find_element_by_tag_name('dd')
            room = room.find_element_by_xpath("//a[text()='Pokój']")
            room.click()
        except Exception as ex:
            print(ex)
            return False
        return True

    def number_of_people(self):
        try:
            number_of_people = self.browser.find_element_by_id('param203')
            number_of_people = number_of_people.find_element_by_xpath("//span[text()='Trzy lub więcej']")
            number_of_people.click()
        except Exception as ex:
            print(ex)
            return False
        return True

    def business_type(self):
        try:
            business_type = self.browser.find_element_by_id('targetid_private_business')
            private = business_type.find_element_by_xpath("//span[text()='Osoba prywatna']")
            private.click()
        except Exception as ex:
            print(ex)
            return False
        return True

    def description(self):
        try:
            description = self.browser.find_element_by_id('add-description')
            text_file = codecs.open("opis.txt", "r", "utf-8")
            lines = text_file.read().split('\n')
            for line in lines:
                description.send_keys(line)
                description.send_keys("\n")

        except Exception as ex:
            print(ex)
            return False
        return True

    def photos(self):
        try:
            included_extension = ['jpeg', 'jpg', 'png']
            files_name = [fn for fn in os.listdir(self.dir_path + '\\zdjecia')
                          if any(fn.endswith(ext) for ext in included_extension)]

            for i in range(8):
                element_id = str(i + 1)
                picture = self.browser.find_element_by_id('add-file-' + element_id)
                picture.click()
                sleep(2)
                pyautogui.write(self.dir_path + '\\zdjecia\\' + files_name[i])
                pyautogui.press('enter')
                sleep(2)

        except Exception as ex:
            print(ex)
            return False
        return True

    def location(self):
        try:
            location = self.browser.find_element_by_id('mapAddress')
            location.clear()
            location.send_keys('Krynica Morska, nowodworski, Pomorskie')
            self.browser.implicitly_wait(5)
            city = self.browser.find_element_by_class_name('geo-suggest-li')
            city.click()
        except Exception as ex:
            print(ex)
            return False
        return True

    def phone_number(self, number):
        try:
            add_phone = self.browser.find_element_by_id('add-phone')
            add_phone.clear()
            add_phone.send_keys(number)
        except Exception as ex:
            print(ex)
            return False
        return True

    def submit(self):
        try:
            submit = self.browser.find_element_by_id('save')
            submit.click()
        except Exception as ex:
            print(ex)
            return False
        return True

    def close(self):
        self.browser.close()


olx = OLX()
olx.accept_cookies()
olx.new_advertisement()
olx.login()
olx.enter_phone_number()
olx.add_advertisement()
