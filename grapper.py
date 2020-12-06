import requests,concurrent.futures,sys
print('usage: python3 grapper.py subs.txt')
print("\n")
def speed():
	_file=sys.argv[1]
	open_file= open(_file ,"r").read().splitlines()
	dup_remove=set(open_file)
	for i in dup_remove:
		try:
			url=requests.get("https://"+i)
			print(url.url,"\t","status_code is: ",url.status_code)
		except:
			try:
				url1=requests.get("http://"+i)
				print(url.url,"\t","status_code is: ",url.status_code)
			except:
				pass

with concurrent.futures.ThreadPoolExecutor() as pl:
	pl.submit(speed)
