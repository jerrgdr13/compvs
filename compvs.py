from lib2to3.pgen2 import driver
from selenium import webdriver
PATH= "/Users/jguerrad/Documents/Jerry/Code/deps/chromedriver"
driver = webdriver.Chrome(PATH)

drvier.get("https://jguerrad.akamaidemos.com/")