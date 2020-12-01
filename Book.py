from selenium import webdriver
from selenium.webdriver.common.by import By
print("Press 1 to search for the book")
print("Press 2 to directly download the book using ISBN code")
option = int(input("Enter your selection"))
if option==2:
    isbn = input("Please Enter ISBN no-")
    browser = webdriver.Chrome(executable_path="C:\\Users\\Cosmo\\Downloads\\chromedriver.exe") #Change the path to the chromedriver.exe file
    url = "https://libgen.rs/"
    browser.get(url)
    isbn_button =browser.find_element_by_xpath("//input[@value='identifier']")
    isbn_button.click() 
    search_bar = browser.find_element_by_xpath("//input[@id='searchform']")
    search_bar.send_keys(isbn)
    search_button = browser.find_element_by_xpath("//input[@value='Search!']")
    search_button.click()
    extension = browser.find_element_by_link_text('Extension')
    extension.click()
    link = browser.find_element_by_link_text('[1]')
    link.click()
    download = browser.find_element_by_link_text('GET')
    download.click()
elif option ==1:
    name = input("Enter the name of the book")
    browser = webdriver.Chrome(executable_path="C:\\Users\\Cosmo\\Downloads\\chromedriver.exe") #Change the path to the chromedriver.exe file
    url = "https://libgen.rs/"
    browser.get(url)
    search_bar = browser.find_element_by_xpath("//input[@id='searchform']")
    search_bar.send_keys(name)
    search_button = browser.find_element_by_xpath("//input[@value='Search!']")
    search_button.click()
else:
    print("Please select only 1 or 2")
