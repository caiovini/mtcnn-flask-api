# importing the requests and base64 library 
import requests 
import base64
import pprint



with open('file.jpg', 'rb') as image:
  img = base64.b64encode(image.read()).decode("utf-8")


headers = { 'Content-Type': 'application/json', 'Accept': '*/*'}

rf = requests.post(
    url = 'http://localhost:8080/selfie' ,
    headers = headers ,
    json = { "img": img }
)

pp = pprint.PrettyPrinter(indent=4)
data = rf.json()
pp.pprint(data)
