import pytest
from selenium import webdriver
import time
#                Не валид лог:пас       Вписать валидные данные
test_log_pass = [('12345', 'qwerty'), ('валид_лог', 'валид_пас')]


class TestLoginPassYandex:

    @pytest.mark.parametrize('log, password', test_log_pass)
    def test_log_pass_valid_test(self, log, password):
        driver = webdriver.Firefox()
        driver.get('https://passport.yandex.ru/auth/')

        # Для удобства сохраняем XPath формы авторизации
        # Заполняем форму авторизации
        username = '//*[@id="passp-field-login"]'
        driver.find_element_by_xpath(username).send_keys([log])
        time.sleep(1)
        press_enter_log = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button'
        driver.find_element_by_xpath(press_enter_log).click()

        password_form = '//*[@id="passp-field-passwd"]'
        driver.find_element_by_xpath(password_form).send_keys([password])
        time.sleep(1)

        press_enter_pass = '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button'
        driver.find_element_by_xpath(press_enter_pass).click()
        time.sleep(3)

        result = driver.page_source
        result_url = driver.current_url
        print('*' * 40)
        print(result_url)
        print('*' * 40)

        time.sleep(1)

        if result_url == 'https://passport.yandex.ru/profile':
            assert True
        else:
            driver.close()
            assert False

        driver.close()
