from PIL import Image
from llm3.geminiAPI.MyApi import geminiModel

def test():
    img = Image.open("img/img.png")
    model = geminiModel()
    response = model.generate_content(["제시한 이미지를 3문장 이내의 한국어로 설명해주세요",img])
    print(response.text)

if __name__ == '__main__':
    test()