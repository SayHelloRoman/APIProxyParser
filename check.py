from threading import Thread
from DateBase.PyDB import DB
from pars import parsing
from time import time
import requests
import uuid

DateBase = DB("DateBase/BD.pydb")


def check(IP_PORT):
	record = {
		"_id" : int(uuid.uuid4()),
		"IP"  : IP_PORT[0],
		"PORT": IP_PORT[1],
		"COUNTRY": IP_PORT[2],
		"WORK": False,
	}

	proxies = {
		"https": f"{IP_PORT[0]}:{IP_PORT[1]}",
		"http": f"{IP_PORT[0]}:{IP_PORT[1]}"
	}

	try:
		start = time()

		requests.get(
			"https://www.google.com.ru/",
			proxies=proxies,
			headers=headers,
		)

		record.update({"WORK": True, "TIME": time() - start})

	except requests.exceptions.ProxyError:
		pass
	
	DateBase.create(record)


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

for i in parsing():
	Thread(target=check, args=(i,)).start()
