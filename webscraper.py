from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%204814%20601201888%20601203793%20601204369%20601296707%20601301599&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1'

#Opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#Grabs all products
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

# Header names
headers = "brand, product_name, price, shipping\n"

# Write the header files to the csv file
f.write(headers)

# Loops and grabs all the infromation 
for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text

	price_container = container.findAll("li",{"class":"price-current"})
	price = price_container[0].strong.text

	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()



# Prints to the console
	print("brand" + " : " + brand)
	print("product_name" + " : " + product_name)
	print("price" + " : $" + price)
	print("shipping" + " : " + shipping)

	# Writes data to the csv file
	f.write(brand + "," + product_name.replace(",","|") + "," + " $" + price + "," + shipping + "\n")
# Close the file
f.close()
