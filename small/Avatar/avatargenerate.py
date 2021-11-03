import random, os
import requests

COLOR_SATURATION_LIMIT = {
	'property_name':'colorSaturation',
	'lowerLimit':0,
	'higherLimit':100
}
GRAYSCALE_SATURATION_LIMIT = {
	'property_name':'grayscaleSaturation',
	'lowerLimit':0,
	'higherLimit':100,
}
HUES_LIMIT = {
	'property_name':'hues',
	'lowerLimit':0,
	'higherLimit':360
}
BASE_URL = "https://avatars.dicebear.com/api/jdenticon/"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR,'Images')
if not os.path.exists(IMG_DIR):
	os.makedirs(IMG_DIR,exist_ok = True)

def swapper(name):
	length = len(name)
	limit = random.randrange(length)
	swapcased = name
	for _ in range(0, limit):
		rand_idx = random.randrange(0, length)
		swapcased = swapcased.replace(swapcased[rand_idx], swapcased[rand_idx].swapcase())
	return swapcased

def build_url(filename):
	col_strn = f"options[{COLOR_SATURATION_LIMIT['property_name']}]={round(random.randint(COLOR_SATURATION_LIMIT['lowerLimit'],COLOR_SATURATION_LIMIT['higherLimit']),4)}"
	
	gs_strn = f"options[{GRAYSCALE_SATURATION_LIMIT['property_name']}]={round(random.randint(GRAYSCALE_SATURATION_LIMIT['lowerLimit'],GRAYSCALE_SATURATION_LIMIT['higherLimit']),4)}"
	
	hues = f"options[{HUES_LIMIT['property_name']}][]={round(random.randint(HUES_LIMIT['lowerLimit'],HUES_LIMIT['higherLimit']),4)}"
	
	return f"{BASE_URL}{filename}?{hues}&{col_strn}&{gs_strn}"


def generate(name):
	swapcased_name = swapper(name)
	display_name = f'{swapcased_name}{random.randrange(1111,9999)}'
	file_name = f"{display_name}.svg"

	endpoint_url = build_url(file_name)
	data = requests.get(endpoint_url)

	if data.status_code == 200:
		IMAGE_SVG_PATH = os.path.join(IMG_DIR, file_name)
		with open(IMAGE_SVG_PATH,'wb') as f:
			f.write(data.content)
		print("Your AVATAAR is created and svg file is stored")
		print("URL - ", endpoint_url)
	else:
		print("Something went wrong.")

def start():
	name = input("Enter your Name: ").strip()
	generate(name)

if __name__ == '__main__':
	start()