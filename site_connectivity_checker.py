import urllib.request as urllib
def main(url):
    print("checking connecting!")
    response=urllib.urlopen(url)
    print("connected to",url,"succesfully")
    print("The response code was : ",response.getcode())

print("This is a site connectivity checker program! ")
input_url=input("input the url of the site ")
main(input_url)