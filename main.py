from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time


#initializing_NO_PROXY_driver
driver = webdriver.Chrome()
driver.maximize_window()

##PROXY SETUP_start
#proxy_ip_port = 'ip:port'

#proxy = Proxy()
#proxy.proxy_type = ProxyType.MANUAL
#proxy.http_proxy = proxy_ip_port
#proxy.ssl_proxy = proxy_ip_port

#capabilities = webdriver.DesiredCapabilities.CHROME
#proxy.add_to_capabilities(capabilities)

##initializing_PROXY_driver
#driver = webdriver.Chrome(PATH, desired_capabilities=capabilities)

##PROXY_SETUP_end

path = "https://miniramp.pl/product-pol-29735-Buty-Vans-X-Hockey-Skate-Authentic-High.html"

#site_request
driver.get(path)
time.sleep(0.5)

#
#https://miniramp.pl/product-pol-29667-deska-Hockey-Kosovo-White.html


#Dropdown menu with sizing (IN PROGRESS; UPDATE: shows sizes id)
dropdown = driver.find_element(By.ID, "projector_sizes_cont")
dropdown.click()
time.sleep(1)

size = driver.find_element(By.LINK_TEXT, "EU: 42.5")
size.click()
time.sleep(1)


#checkout_process_with_accessibility_check_(in_progress)
if (driver.find_element(By.ID, "oneclick_googlePay")):

    #checkout1
    basket1 = driver.find_element(By.ID, "projector_button_basket")
    basket1.click()
    time.sleep(0.5)

    #checkout2
    basket2 = driver.find_element(By.ID, "basket_go_next")
    basket2.click()
    time.sleep(0.5)

    #checkout3
    basket3 = driver.find_element(By.LINK_TEXT, "Zamów bez rejestracji")
    basket3.click()
    time.sleep(0.5)

    #delivery rules
    firstname = driver.find_element(By.ID, 'client_firstname')
    lastname = driver.find_element(By.ID, 'client_lastname')
    birth_day = driver.find_element(By.ID, 'birth_date')
    street = driver.find_element(By.ID, 'client_street')
    street_number = driver.find_element(By.ID, 'client_street_number')
    zipcode = driver.find_element(By.ID, 'client_zipcode')
    city = driver.find_element(By.ID, 'client_city')
    phone = driver.find_element(By.ID, 'client_phone')
    email = driver.find_element(By.ID, 'client_email')

    #filling delivery
    firstname.send_keys("Adrian"), time.sleep(0.2)
    lastname.send_keys("Prędki"), time.sleep(0.2)
    birth_day.send_keys("2002-08-06"), time.sleep(0.2)
    street.send_keys("Zaciszna 8B"), time.sleep(0.2)
    street_number.send_keys("8B"), time.sleep(0.2)
    zipcode.send_keys("35-326"), time.sleep(0.2)
    city.send_keys("Rzeszów"), time.sleep(0.2)
    phone.send_keys("734467035"), time.sleep(0.2)
    email.send_keys("ap98@op.pl"), time.sleep(0.2)

    #terms_agreement
    terms_agree = driver.find_element(By.ID, "terms_agree")
    terms_agree.click()
    time.sleep(1)

    #sumbitting_form
    submit_form = driver.find_element(By.ID, "submit_clientnew_form")
    submit_form.click()
    time.sleep(1)

    #payment_rules
    cc = driver.find_element(By.ID, "card_payment")
    cod = driver.find_element(By.ID, "dvp_payment")

    #payment_choose
    cc.click()
    #cod.click()

    #summary_button
  
    button_text = "Przejdź dalej"
    e = driver.find_element(By.PARTIAL_LINK_TEXT, button_text)
    e.click()

        #terms_agreement
    terms_agree2 = driver.find_element(By.CLASS_NAME, "order2_terms_conditions")
    terms_agree2.click()
    time.sleep(1)
        #terms_agreement
    terms_cancel = driver.find_element(By.CLASS_NAME, "order2_cancel")
    terms_cancel.click()
    time.sleep(1)

    button_text2 = "Zamawiam i płacę"
    e = driver.find_element(By.PARTIAL_LINK_TEXT, button_text2)
    e.click()

    time.sleep(60000)


# elif (driver.find_element(By.LINK_TEXT, "Powiadom mnie o dostępności produktu")):
#     print("Produkt niedostępny")

# else:
#     driver.quit()







