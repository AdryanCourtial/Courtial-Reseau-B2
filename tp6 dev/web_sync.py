import requests
import os
import argparse

#Gestion des arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", action="store")
args = parser.parse_args()

# je renome les Variables pour pas que ce soit le bordelle
url = args.url

#Les variable global
html_path = "/tmp/web_page/fichier.html"

def get_content(url):
    reponse = requests.get(url)
    content = reponse.status_code + reponse.content + reponse.reason
    return str(reponse)

def write_content(content, file):
    file = open(file, mode="w")
    file.write(content)
    file.close()

if __name__ == "__main__":
    write_content(get_content(url), html_path)
    


