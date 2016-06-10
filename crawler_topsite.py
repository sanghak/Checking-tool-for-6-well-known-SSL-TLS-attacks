import requests
from bs4 import BeautifulSoup

def spider(max_pages):
	page = 0
	f = open("result.txt", encoding = "utf-8", mode = "w")
	while page < max_pages:
		url = 'http://www.alexa.com/topsites/global;' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		#plain_text.encode('utf-8')
		
		f.write(plain_text)
		
		#print (len(plain_text))
		#print (plain_text)
		page += 1
	f.close()
def pick_site(text_file):
	f1 = open(text_file, encoding = "utf-8", mode = "r")
	f2 = open("topsites_raw.txt", encoding = "utf-8", mode = "w")
	while True:
		line = f1.readline()
		if not line: break
		if line[12:20] == "listings" or line[11:23] == "site-listing":
			f2.write(line)

	f1.close()
	f2.close()	

if __name__ == "__main__": 
	spider(20)

	#pick_site("result.txt")

