# import requests
# cid ="1000.WT9XBLJ9CLQ5L450UVT6X2JROIKXEC"
# cse = "ff37de0e0eac65e983e3e1b4fb68c0b15405dfbd8e"
# code = "1000.56ab6f9b3dfccb9da21e988804eb052f.9bf9a5e81615e9c36239a30e6dc59934"
# url = "https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&code={2}&client_id={1}&redirect_uri=https://creator.zoho.in/appbuilder/indinfravit/tas-poc&client_secret={0}".format(cse,cid,code)
# r = requests.post(url = url)
# print(r.text)
import requests
urls = "https://accounts.zoho.in/oauth/v2/token"
test = {"client_id":"1000.WT9XBLJ9CLQ5L450UVT6X2JROIKXEC","client_secret":"ff37de0e0eac65e983e3e1b4fb68c0b15405dfbd8e","code":"1000.6ffc4597012abd1b606eb784ac2f34e4.2d079000317035f30ea8d7415e79183c","grant_type":"authorization_code"}
r = requests.post(url = urls,data = test)
f = open("cred.txt","w")
f.write(r.text)
f.close()