from selenium import webdriver
import json

debug = True
uid = ""
upw = ""

if debug:
    with open("config/debug_config.json") as f:
        config = json.load(f)
        uid = config["id"]
        upw = config["pw"]
else:
    with open("config/config.json") as f:
        config = json.load(f)
        uid = config["id"]
        upw = config["pw"]

driver = webdriver.Chrome("webdriver/chromedriver")
driver.get("https://www.sketchuptextureclub.com/login")

elem_login = driver.find_element_by_name("mail")
elem_login.clear()
elem_login.send_keys(uid)

elem_login = driver.find_element_by_name("password")
elem_login.clear()
elem_login.send_keys(upw)

xpath = """//*[@id="loginf"]/div[4]/input"""
driver.find_element_by_xpath(xpath).click()
