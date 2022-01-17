from bs4 import BeautifulSoup
import requests
import cv2
import numpy as np

def generate_image(image_name: str) -> str:
    url = f'https://www.google.com/search?q={image_name}&tbm=isch'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    image_index = np.random.randint(1, len(images) - 1)
    static_path = 'img/design/generated/' + 'img' + '.jpg'
    image = images[image_index]
    link = image.get('src')
    image = cv2.imdecode(np.frombuffer(requests.get(link).content, dtype=np.uint8), flags=1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C  , cv2.THRESH_BINARY, 11, 1)
    cv2.imwrite('static/' + static_path, threshold)
    return static_path
