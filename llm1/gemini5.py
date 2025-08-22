from PIL import Image
from llm3.geminiAPI.MyApi import geminiModel

def test():
    img = Image.open("img/img.png")
    model = geminiModel()
    print(response.text)

if __name__ == '__main__':

    question = "인공지능이란 무엇인가요?"

    prompt = f"'{question}'에 대해 설명해 줘."

    test(prompt)