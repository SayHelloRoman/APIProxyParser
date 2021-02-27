from bs4 import BeautifulSoup
import requests


def parsing():
    p = BeautifulSoup(requests.get("https://www.proxynova.com/proxy-server-list").text)
    tbody = p.find_all("tbody")[0].find_all("tr")
    ip_port = []

    for f in tbody:
        try:
            ip = f.find("abbr")["title"]
            port = f.find_all("td")[1].text.strip()
            country = f.find_all("a")[0]["title"][13:].lower()

            ip_port.append([ip, port, country])

        except TypeError:
            pass

    return ip_port
