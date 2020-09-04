import time 
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
#the above line is to use chrome driver
#I have set the path to absolute
driver.get("https://web.whatsapp.com")#this line opens the whatsapp web on chrome


input("press anything after QR scan")

time.sleep(2)#a small time for the process to go on smoothly


names=["Person"]
#Here Person represents the name in your contact list 
#here the list can be appended for more number of epople 
for name in names:

    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    person.click()

    for i in range(1,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]
    print(msg[-1])
    if msg[-1] == "Happy Diwali":
        reply = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        reply.clear()
        reply.send_keys("Thanks and same to you!")
        reply.send_keys(Keys.RETURN)
    else :
        reply = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        reply.clear()
        reply.send_keys("Happy Diwali!")
        reply.send_keys(Keys.RETURN)