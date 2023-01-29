#!/usr/bin/env python3
# Simple Auto Adventure DOSI
# Created By Viloid ( github.com/vsec7 )

import requests, time

class DOSI:

	def __init__(self, c):
		self.base = "https://citizen.dosi.world/api/citizen/v1"
		self.cookie = { 'DOSI_SES': c }

	def getBalance(self):
		return requests.get(self.base + '/balance', cookies=self.cookie).json()

	def claimDon(self):
		return requests.post(self.base + '/events/check-in', cookies=self.cookie).json()

	def adventure(self):
		return requests.post(self.base + '/adventures/17/participation', cookies=self.cookie).json()

def main():

	while True:
		for s in open("session_lists.txt").read().splitlines():
			x = DOSI(s)
			print(x.claimDon())
			print(x.getBalance())
			print(x.adventure())
			print("")
		print("+--------------------------------------------+")
		time.sleep(86460) # 24:01 hours

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")
