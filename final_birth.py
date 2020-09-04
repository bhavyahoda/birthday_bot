from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time
import datetime
import json

wat_name = None

# definnig the birtday wish


def birth_wish(name):
    return "Happy Birthday " + name.split(" ")[0] + "hope you enjoy the day! 😀"

# reading from the jason file that is you get the name returned according to the
# date on that particular day


def readjson(data_file, attr_ret, att1, att2, attr_va1, attr_val2):

    # load the json datafile
    data = json.load(data_file)
    values = []

    # comapring the attribute and atting the name accordingly
    for i in data:
        if(i[att1] == attr_va1 and i[att2] == attr_val2):
            values.append(i[attr_ret])
    return values


# opening the json file in read formaat
data_file_read = open("data_1.json", "r")
names_people = []
print("Script running !!!")
# to run the file at 11:59 everybody
while True:
    try:
        # getting current data
        datt = datetime.datetime.now()
        names_people = readjson(data_file_read, "name", "birth_month", "birth_date", str(
            datt.month), str(datt.day))

    except json.decoder.JSONDecodeError:
        continue
    if(names_people != []):
        
        break


chropt = webdriver.ChromeOptions()
chropt.add_argument("C:/Program Files(x86)/Google/Chrome/Application")
#PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(executable_path="C:/Program Files (x86)/chromedriver.exe",
                          options=chropt)

driver.get("https://web.whatsapp.com/")
time.sleep(5)

print(names_people)

# finding the contacts
for name in names_people:
    try:
        wat_name = driver.find_elements_by_xpath(
            "//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span")
    except Exception as ex:
        print(ex)
        continue
        # a click
    wat_name.click()

    while(True):
        msg_box = driver.find_element_by_xpath(
            "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        msg_box.send_keys(birth_wish(name))

        send_bt = driver.find_elements_by_class_name("_1U1xa")
        send_bt.click()
        break
