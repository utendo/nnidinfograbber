import sys, json, requests

url = requests.get("https://pf2m.com/mii/" + sys.argv[1])
text = url.text

data = json.loads(text)

print("NNID Info Grabber by utendo")
print("-----------------------------")

if "id" in data:
  print("Display Name: " + data['name'])
  print("-----------------------------")
  print("Mii Hash (For WaraWara Plaza): " + data['data'])
  print("-----------------------------")
  print("Mii Hash (For mii-secure.cdn.nintendo.net): " + data['hash'])
  print("-----------------------------")
  print("Nintendo Network ID: " + data['user_id'])
else:
  print("The Nintendo Network ID could not be found.")