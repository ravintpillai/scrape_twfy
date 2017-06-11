from BeautifulSoup import BeautifulSoup
import re
import requests

full_page = requests.get("https://www.theyworkforyou.com/mps/?o=l")
full_page_soup = BeautifulSoup(full_page.text)

names = full_page_soup.findAll("a", {"class":"people-list__person"})
memberships = full_page_soup.findAll("p", {"class":"people-list__person__memberships"})
party = re.compile("party")

with open("mps_details.csv", 'w+') as mp_details:
	for x in range(len(names)):
		mp_details.write('"')
		mp_details.write(names[x].find("h2").string.encode('utf-8'))
		mp_details.write('"')
		mp_details.write(",")
		mp_details.write('"')
		mp_details.write(memberships[x].find("span").string.encode('utf-8'))
		mp_details.write('"')
		mp_details.write(",")
		mp_details.write('"')
		mp_details.write(memberships[x].find("span", {"class":party}).string.encode('utf-8'))
		mp_details.write('"')
		mp_details.write("\n")