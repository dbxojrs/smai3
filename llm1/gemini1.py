from myllm.myapi import geminiModel

def test(txt):
    model = geminiModel()
    response = model.generate_content(txt)
    return response.text

if __name__ == '__main__':
    print("\n--- Gemini 챗봇 시작 ---")

    while True:
        user_message = input("나: ")

        if user_message.lower() == '종료':
            break

        response_text = test(user_message)

        print("Gemini:", response_text)

    print("--- 챗봇 종료 ---")
