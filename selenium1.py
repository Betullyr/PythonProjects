#"Selenium ile github bot"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Github:
  def __init__(self, username, password):
      self.browser = webdriver.Chrome()
      self.username = username
      self.password = password
      self.followers=[]
  def sigIn(self):
      self.browser.get("https://github.com/login")
      time.sleep(2)

      self.browser.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(self.username)
      self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)
      self.browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]').click()

  def loadFollowes(self):
      items = self.browser.find_elements(By.CSS_SELECTOR(".d-table.table-fixed"))

      for i in items:
          self.followers.append(i.find_element(By.CSS_SELECTOR(".link-gray.pl-1")).text)

  def getFollowers(self):
      self.browser.get("https://github.com/Betullyr?tab=followers")
      time.sleep(2)
      self.loadFollowes()

      while True:
          links=self.browser.find_element(By.CLASS_NAME("BtnGroup")).find_elements(By.TAG_NAME("a"))
          if(len(links))==1:
              if(links[0].text=="Next"):
                  links[0].click()
                  time.sleep(1)
                  self.loadFolowars()
              else:
                  break
          else:
              for link in links:
                  if link.text=="Next":
                      link.click()
                      time.sleep(1)
                      self.loadFollowes()
                  else:
                      continue




github=Github("github_name","github_sifre")
time.sleep(2)
github.sigIn()
time.sleep(2)
print(github.getFollowers())
print()


