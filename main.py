from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time


PATH = r"C:\Users\ap9\AppData\Local\Microsoft\WindowsApps\chromedriver.exe"

#initializing_NO_PROXY_driver
driver = webdriver.Chrome(PATH)

#fullscreen
driver.fullscreen_window()

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



#site_request
driver.get("https://miniramp.pl/product-pol-29667-deska-Hockey-Kosovo-White.html")
time.sleep(0.5)

#https://miniramp.pl/product-pol-29735-Buty-Vans-X-Hockey-Skate-Authentic-High.html
#https://miniramp.pl/product-pol-29667-deska-Hockey-Kosovo-White.html


#Dropdown menu with sizing (IN PROGRESS; UPDATE: shows sizes id)
# dropdown = driver.find_element_by_id("projector_sizes_cont");
# dropdown.click();
# time.sleep(1);
#
# select = Select(driver.find_element_by_id('projector_sizes_select'))
# select.select_by_visible_text("Wybierz rozmiar")
# options = select.options
#
# for option in options:
#     print(option)
#
# driver.quit()


#checkout_process_with_accessibility_check_(in_progress)
if (driver.find_element_by_id("oneclick_googlePay")):

    #checkout1
    basket1 = driver.find_element_by_id("projector_button_basket");
    basket1.click();
    time.sleep(0.5);

    #checkout2
    basket2 = driver.find_element_by_id("basket_go_next");
    basket2.click();
    time.sleep(0.5);

    #checkout3
    basket3 = driver.find_element_by_link_text("Zamów bez rejestracji");
    basket3.click();
    time.sleep(0.5);

    #delivery rules
    firstname = driver.find_element(By.ID, 'client_firstname');
    lastname = driver.find_element(By.ID, 'client_lastname');
    birth_day = driver.find_element(By.ID, 'birth_date');
    street = driver.find_element(By.ID, 'client_street');
    street_number = driver.find_element(By.ID, 'client_street_number');
    zipcode = driver.find_element(By.ID, 'client_zipcode');
    city = driver.find_element(By.ID, 'client_city');
    phone = driver.find_element(By.ID, 'client_phone');
    email = driver.find_element(By.ID, 'client_email');

    #filling delivery
    firstname.send_keys("Adrian"), time.sleep(0.2);
    lastname.send_keys("Prędki"), time.sleep(0.2);
    birth_day.send_keys("2002-08-06"), time.sleep(0.2);
    street.send_keys("Zaciszna 8B"), time.sleep(0.2);
    street_number.send_keys("8B"), time.sleep(0.2);
    zipcode.send_keys("35-326"), time.sleep(0.2);
    city.send_keys("Rzeszów"), time.sleep(0.2);
    phone.send_keys("734467035"), time.sleep(0.2);
    email.send_keys("ap9@op.pl"), time.sleep(0.2);

    #terms_agreement
    terms_agree = driver.find_element_by_id("terms_agree");
    terms_agree.click();
    time.sleep(1);

    #sumbitting_form
    submit_form = driver.find_element_by_id("submit_clientnew_form");
    submit_form.click();
    time.sleep(1);

    #payment_rules (in progress)

    labels = driver.find_elements_by_css_selector("#content > form > div > div:nth-child(1) > section > div.order__payments_section")
    for label in labels:
         print(label.text)


    # Lokalizuj wszystkie dostępne metody płatności (NIE DZIALA)
    #labels = driver.find_elements_by_css_selector("#content > form > div > div:nth-child(1) > section > div.order__payments_section")
    #time.sleep(4);
    # Wybierz interesującą Cię metodę płatności, na przykład "BLIK"
    #desired_payment_method = "PayPo - kup teraz, zapłać za 30 dni"

    #for label in labels:
    #    if desired_payment_method in label.text:


    # Kliknij na element reprezentujący wybraną metodę płatności
         #label.click()





elif (driver.find_elements_by_link_text("Powiadom mnie o dostępności produktu")):
    print("Produkt niedostępny");

else:
    driver.quit()









#imię.send_keys("IMIĘ")  #tu wpisz swoję imię
#nazwisko.send_keys("NAZWISKO") #tu wpisz swoję nazwisko
#data_urodzenia.send_keys("DATA_URODZENIA")  #tu wpisz swoją datę urodzenia
#ulica.send_keys("ULICA") #tu wpisz swoją ulicę
#numer_domu.send_keys("NUMER_DOMU")  #tu wpisz swój nr domu
#kod_pocztowy.send_keys("KOD_POCZTOWY") #tu wpisz swój kod pocztowy
#numer_telefonu.send_keys("NUMER_TELEFONU")  #tu wpisz swój numer telefonu
#adres_e-mail.send_keys("ADRES_EMAIL") #tu wpisz swój adres e-mail


