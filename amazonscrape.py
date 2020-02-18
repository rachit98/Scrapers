import requests
from bs4 import BeautifulSoup
import smtplib

URL="https://www.amazon.in/VivoBook-Windows-X409FA-EK555T-Transparent-Silver/dp/B07WNGR8GQ/ref=pd_sbs_147_1/260-5958339-2461009?_encoding=UTF8&pd_rd_i=B07WNGR8GQ&pd_rd_r=bb5a0a41-2006-43eb-b7da-95559c50d18f&pd_rd_w=F0lsE&pd_rd_wg=bKyf8&pf_rd_p=fbf43daf-8fb3-47b5-9deb-ae9cce3969a9&pf_rd_r=C8N86AXP7832C04CY56C&psc=1&refRID=C8N86AXP7832C04CY56C"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
def check_price():
	page = requests.get(URL,headers=headers)

	soup=BeautifulSoup(page.content,"html.parser")

	price=soup.find(id="priceblock_ourprice").get_text()

	print(price)
	converted_price = float(price[2:8].replace(",","."))

	if converted_price>44.000:
		send_mail()
	print(converted_price)


def send_mail():
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login("rachity@gmail.com","vdgaikrfjhgmbswi")

	subject="Price Drop"
	body="Check the amazon link  https://www.amazon.in/VivoBook-Windows-X409FA-EK555T-Transparent-Silver/dp/B07WNGR8GQ/ref=pd_sbs_147_1/260-5958339-2461009?_encoding=UTF8&pd_rd_i=B07WNGR8GQ&pd_rd_r=bb5a0a41-2006-43eb-b7da-95559c50d18f&pd_rd_w=F0lsE&pd_rd_wg=bKyf8&pf_rd_p=fbf43daf-8fb3-47b5-9deb-ae9cce3969a9&pf_rd_r=C8N86AXP7832C04CY56C&psc=1&refRID=C8N86AXP7832C04CY56C"


	msg=f"Subject: {subject}\n\n\n{body}"
	server.sendmail('rachity@gmail.com','rachity@gmail.com',msg)
	print("Mail has been sent")
	server.quit()


check_price()
