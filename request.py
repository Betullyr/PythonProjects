import requests
import json
class Github:
    def __init__(self):
      self.api_url = "api url "
      self.token = "token"
    def getUser(self, username):
        response = requests.get(self.api_url+"/users/"+username)
        return response.json()   #response değişkenini bizim için json hale getirir
    def getRepositories(self,username):
        response = requests.get(self.api_url + "/users/" + username+"/repos")
        return response.json()
    def crateRepository(self,name):
        reponse = requests.post(self.api_url+ "/user/repos?access_token="+ self.token, json={   #get ile bilgi alıyorduk post ile gönderiyoruz
            "name": name,                                #temel bir reponun içindekiler
            "description": "This is your first repository",
            "homepage": " ",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return reponse.json()

github = Github()
while True:
    secim = int(input("1-Find User\n2-Get Repositories\n3-Create Repository\n4-Exit\nSecim:"))
    if(secim == 4):
        break
    else:
        if(secim == 1):
          username = input("Kullanacı adını giriniz")
          result = github.getUser(username)
          print(result)
        elif(secim == 2):
            username=input("Kullanıcı adı giriniz")
            result = github.getRepositories(username)
            for i in result:
              print(i["name"])
        elif(secim == 3):
            repo_name = input("Repository adı giriniz:")
            result = github.crateRepository(repo_name)
            print(result)

        else:
            print("Hatalı secim")