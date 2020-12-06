import requests,concurrent.futures,time,sys
print('usage: python3 grapper.py subs.txt')
print("\n")
def speed():
	_file=sys.argv[1]
	open_file= open(_file ,"r").read().splitlines()
	for i in open_file:
		try:
			url=requests.get("https://"+i)
			print(url.url,"\t","status_code is: ",url.status_code)
		except:
			print("http not work i will try https")
			try:
				url1=requests.get("http://"+i)
				print(url.url,"\t","status_code is: ",url.status_code)
			except:
				print("bad url" ,i)

with concurrent.futures.ThreadPoolExecutor() as pl:
	time.sleep(0.2)
	pl.submit(speed)
