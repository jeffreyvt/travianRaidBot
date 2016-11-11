from selenium import webdriver
import time
import random
import datetime

iterations = int(input("How many iterations would you like to run?"))

browser = webdriver.Firefox()

for i in range(iterations):
    print("This is iteration number: ", str(i), "The current time is: ",str(datetime.datetime.now().time()))
    browser.get('http://ts4.travian.com.au')
    login_name = browser.find_element_by_name("name")
    login_name.send_keys("jeffreyvt")
    password = browser.find_element_by_name("password")
    password.send_keys("***********") #write ur password here

    wait_time = random.randrange(0,10)
    # print(wait_time)
    time.sleep(wait_time)
    login_btn = browser.find_element_by_name("s1")
    login_btn.click()
    time.sleep(random.randrange(10,20))

    browser.get('http://ts4.travian.com.au/build.php?tt=99&id=39')
    wait_time = random.randrange(0,10)
    # print(wait_time)
    time.sleep(wait_time)
    select_close = browser.find_element_by_id("raidListMarkAll45") #check raid all
    select_close.click()
    start_raid = browser.find_element_by_xpath("//button[@value='Start raid']") #find the first start raid button
    start_raid.click()

    time.sleep(random.randrange(10,20))
    browser.get('http://ts4.travian.com.au/logout.php')

    sleep_minutes = random.randint(25,35)
    print("The next raid will be in ",sleep_minutes ," minutes.")
    for j in range(sleep_minutes):
        time.sleep(60)
        print("The next raid will be in ", sleep_minutes-j-1, " minutes.")
    time.sleep(random.randint(1,59))