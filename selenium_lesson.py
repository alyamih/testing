import time
from _ast import Assert

from data import mail
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'C:\Users\Alya\PycharmProjects\selenium\chromedriver.exe')
browser.get('https://www.facebook.com/')
search = browser.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 g5gj957u rj1gh0hx buofh1pr hpfvmrgz i1fnvgqd bp9cbjyn owycx6da btwxx1t3 b5q2rw42 lq239pai mysgfdmx hddg9phg']").click()
clickLogin = browser.find_element_by_xpath("//button[@name='login']").click()
clickSearch = browser.find_element_by_xpath("//div[@class='l6v480f0 f10w8fjw pybr56ya']").click()
clickNewAccount = browser.find_element_by_xpath("//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
clickreg = browser.find_element_by_xpath("//button[@name='websubmit']").click()


def login(mail):
    time.sleep(2)
    login = browser.find_element_by_xpath('//input[@id="email"]').send_keys(mail['username'])
    time.sleep(2)


def password(mail):
    time.sleep(2)
    password = browser.find_element_by_xpath('//input[@id="pass"]').send_keys(mail['password'])
    time.sleep(2)

def firstname(mail):
    time.sleep(2)
    firstname = browser.find_element_by_xpath('//input[@name="firstname"]').send_keys(mail['firstname'])
    time.sleep(2)

def lastname(mail):
    time.sleep(2)
    lastname = browser.find_element_by_xpath('//input[@name="lastname"]').send_keys(mail['lastname'])
    time.sleep(2)

def friend(mail):
    time.sleep(2)
    friend = browser.find_element_by_xpath('//input[@class="oajrlxb2 rq0escxv f1sip0of hidtqoto e70eycc3 lzcic4wl hzawbc8m ijkhr0an aaoq3grb sgqwj88q b3i9ofy5 oo9gr5id b1f16np4 hdh3q7d8 dwo3fsh8 qu0x051f esr5mh6w e9989ue4 r7d6kgcz br7hx15l h2jyy9rg n3ddgdk9 owxd89k7 ihxqhq3m jq4qci2q k4urcfbm iu8raji3 qypqp5cg l60d2q6s hv4rvrfc hwnh5xvq ez2duhqw rmlgq0sb dzqu5etb aj8hi1zk r4fl40cc kd8v7px7 m07ooulj mzan44vs"]').send_keys(mail['friend'])
    time.sleep(2)

currentUrl = browser.getCurrentUrl()
login(mail)
password(mail)
time.sleep(3)
clickLogin
isOpen = browser.assertEquals(currentUrl, "https://www.facebook.com/checkpoint/1501092823525282/?next=https%3A%2F%2Fwww.facebook.com%2F%3Fsk%3Dwelcome" );
time.sleep(3)
friend(mail)
time.sleep(3)
search
time.sleep(3)
clickSearch



browser.get('https://www.facebook.com/')
login(mail)
time.sleep(3)
clickLogin
time.sleep(5)
password(mail)
time.sleep(3)
clickLogin
time.sleep(4)



browser.get('https://www.facebook.com/')
password(mail)
time.sleep(3)
clickLogin
time.sleep(3)
login(mail)
time.sleep(3)
password(mail)
time.sleep(3)
clickLogin
time.sleep(5)



browser.get('https://www.facebook.com/')
clickNewAccount
firstname(mail)
time.sleep(3)
lastname(mail)
time.sleep(3)
clickreg