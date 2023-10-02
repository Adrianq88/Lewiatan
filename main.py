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


# #Dropdown menu with sizing (IN PROGRESS)
# dropdown = driver.find_element_by_id("projector_sizes_cont");
# dropdown.click();
# time.sleep(1);

# sizing = driver.find_element_by_id('projector_sizes')
# drop = Select(sizing)
# drop.select_by_value("J")
# drop.click();
# time.sleep(4)


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

    blik = driver.find_elements_by_xpath('//*[@id="blik_payment"]').click();

    #time.sleep(1);


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

