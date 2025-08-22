from llm3.geminiAPI.MyApi import openAiModelArg, makeMsg


def test(prompt):
    modelName = "gpt-4o"
    msg=makeMsg("",prompt)
    result= openAiModelArg(modelName,msg)
    print(result)

if __name__ == '__main__':
    prompt = "sk하이닉에 대해서 알려줘"
    test(prompt)