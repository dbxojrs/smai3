from llm3.geminiAPI.MyApi import geminiModel

def test(prompt):
    response = model.generate_content(prompt)
    model = geminiModel()
    print(response.text)
    response = model.generate_content(prompt)

if __name__ == '__main__':
    code_prompt = "Python으로 피보나치 수열을 계산하는 함수를 작성해 줘."
    test(code_prompt)