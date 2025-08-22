from io import BytesIO

import requests
from PIL import Image

from llm3.geminiAPI.MyApi import geminiModel
def test(prompt, img):
    response = model.generate_content(prompt)
    model = geminiModel()
    print(response.text)
    response = model.generate_content([prompt,img])

if __name__ == '__main__':
    image_url = "https://img.danawa.com/prod_img/500000/492/722/img/1722492_1.jpg?_v=20200819161846"  # 실제 이미지 URL로 교체
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    prompt = "이 이미지의 있는 음료의 영양성분과 칼로리를 알려줘"
    test(prompt,img)