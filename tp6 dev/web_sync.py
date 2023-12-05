import requests
import argparse

#Gestion des arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", action="store")
args = parser.parse_args()

# je renome les Variables pour pas que ce soit le bordelle
url = args.url

#Les variable global
html_path = "/tmp/web_page"

def get_content(url):
    reponse = requests.get(url)
    return reponse

def write_content(content, file):
    open()


