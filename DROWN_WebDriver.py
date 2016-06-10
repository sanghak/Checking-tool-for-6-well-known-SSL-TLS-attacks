from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


sites = []
web_i = 0

f = open("top500.txt", encoding = "utf-8", mode = "r")
while True:
	line = f.readline()
	if not line: break
	sites.append(line.rstrip())

#print (sites)

wf = open("result_500_week4.txt", encoding = "utf-8", mode = "w")
#web_i = 475
while web_i < 500:
	website = sites[web_i]
	table = ""
	check_updating = ""
	flag = 0
	red = 0
	green = 0
	orange = 0
	blue = 0
	grey = 0

	driver = webdriver.Firefox()
	driver.get('https://test.drownattack.com/?site=' + str(website))
	'''
	try:
	    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
	except TimeoutException:
		driver.close()
	'''

	f1 = open("test.txt", encoding = "utf-8", mode = "w")
	f1.write(driver.page_source)
	f1.close()

	driver.close()

	f2 = open("test.txt", encoding = "utf-8", mode = "r")
	i = 0
	while True:
		line = f2.readline()
		if not line: break
		if i == 40:
			check_updating = line
		if i == 42:
			table = line
		i += 1
	f2.close()

	for k in range(0, len(check_updating)-8):
		if check_updating[k:k+8] == "updating":
			print ("updating!!")
			flag = 1
			break

	if flag == 1:
		print ("flag", website)
		continue


	#print (check_updating)
	#print (table)

	if table[3] == "W":
		wf.write(website + "\t" + str(red) + "\t" + str(green) + "\t" + str(orange) + "\t" + str(blue) + "\t" + str(grey) +"\n")
	else:
		for j in range(0,len(table)):
			#print ("len : ", len(table))
			#print (table[j:j+7])
			if table[j:j+7] == "update-":
				#print (table[j:j+7], table[j-11:j-1])
				if table[j:j+10] == "update-cve" and table[j-11:j-1] == "key-change": ### update-key-change
				 	#print ("here")
				 	blue = blue + 1
				elif table[j:j+12] == "update-sslv2" and table[j-11:j-1] == "key-change":
					blue = blue + 1
				elif table[j:j+10] == "update-cve":### update-cve
					red = red + 1
				elif table[j:j+12] == "update-fixed": ### update-fixed
					green = green + 1
				elif table[j:j+12] == "update-error": ### update-error
					grey = grey + 1
				elif table[j:j+13] == "update-export" or table[j:j+12] == "update-sslv2": ### update-export
					orange = orange + 1
				j = j + 1
			else:
				j = j + 1
		wf.write(website + "\t" + str(red) + "\t" + str(green) + "\t" + str(orange) + "\t" + str(blue) + "\t" + str(grey) +"\n")

	web_i = web_i + 1



wf.close()