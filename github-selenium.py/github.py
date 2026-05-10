from githubUserInfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Github:
    def __init__(self,username,password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.username=username
        self.password=password
        self.followers=[]
    
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        
        time.sleep(2)
        
        self.browser.find_element(By.NAME, "commit").click()
    
    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        
        followers=self.browser.find_elements(By.CSS_SELECTOR, "div.d-table-cell a.d-inline-block")
        
        for user in followers:
            link_text=user.text.strip()
            if link_text:
                print(link_text)
        
github=Github(username,password)
github.signIn()
github.getFollowers()