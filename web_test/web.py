import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


link = 'http://www.asusrouter.com/Main_Login.asp'

response = requests.get(link, verify=True)

if response.status_code >= 400:
    print(f"- Возникла ошибка: {response.status_code}")

print(response.content)

#with open(r"C:\Users\Grand Riph\Desktop\img.png", "wb") as img_file:
    #img_file.write(response.content)

#link_cats = 'https://catfact.ninja/fact'

#response = requests.get(link_cats, verify=True)

#print(response.json())

#print(response.url)


#app = FastAPI()

'''
@app.get("/")
def read_root():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)
'''











