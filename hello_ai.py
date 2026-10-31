import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. 读取 .env 文件里的密钥
load_dotenv()

# 2. 连接大模型
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("正在呼叫 AI，请稍等...")

# 3. 发送请求
try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个机器人夹爪设计专家。"},
            {"role": "user", "content": "我想抓一个直径 60mm、约 300g 的圆柱瓶，立着放。请提取出尺寸和重量。"}
        ]
    )
    # 4. 打印结果
    print("\n--- AI 回复 ---")
    print(response.choices[0].message.content)
    print("----------------")

except Exception as e:
    print(f"\n报错了！错误信息：{e}")