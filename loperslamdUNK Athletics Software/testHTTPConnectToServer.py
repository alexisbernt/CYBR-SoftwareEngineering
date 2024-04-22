import requests

url = 'http://localhost:8080/licenseserver/v1/insert'
data = {
    "Signature":"YOURSIGNATURE",
    "Name":"Max",
    "Email":"max@example.com",
    "UserID":"0xfe5712d89a"
}

x = requests.post(url, json = data, auth = ("newAdmin","password"))

print(x.text)








# from http.client import HTTPSConnection
# from base64 import b64encode


# # Authorization token: we need to base 64 encode it 
# # and then decode it to acsii as python 3 stores it as a byte string
# def basic_auth(username, password):
#     token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
#     return f'Basic {token}'

# username = "gmbe75"
# password = ""

# #This sets up the https connection
# c = HTTPSConnection("localhost", port=8080)
# #then connect
# headers = { 'Authorization' : basic_auth(username, password) }
# c.request('GET', '/licenseserver/v1/validate', headers=headers)
# #get the response back
# res = c.getresponse()
# # at this point you could check the status etc
# # this gets the page text
# data = res.read() 