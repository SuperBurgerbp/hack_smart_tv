import requests
ip = input("Введите IP: ")
port = input("Введите порт: ")
app = input("App name: ")
print("\n" + "Y -- Выключить N -- Включить")
desc = input()
if desc == "Y":
    url = "http://" + ip + ":" + port + "/ws/apps/" + app
    myobj = {'allowStop': "True"}
    x = requests.post(url, data = myobj)
else:
        url = "http://" + ip + ":" + port + "/ws/apps/" + app
        myobj = {'allowStop': "False"}
        x = requests.post(url, data = myobj)
