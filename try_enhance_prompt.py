import os
import json
import requests
import time

# OpenAI API Key
api_key = "sk-MDKCnF2HVFIntoyPhJf7uyA100SpIpjntW44Np2SH6USMyOh"  # TODO: 替换为你的 API 密钥

# 设置 OpenAI API 请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 增强文本的函数
def enhance_text(text):
    prompt = f"Generate five different sentences that have the same meaning as: {text}. Just return text split with &&. No need Serial number"
    payload = {
        # "model": "gpt-4o",
         "model": "gpt-4",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 300  # 增加 max_tokens 以确保生成足够的内容
    }
    
    max_attempts = 3
    attempt_count = 0
    while attempt_count < max_attempts:
        try:
            response = requests.post("https://api.key77qiqi.cn/v1/chat/completions", headers=headers, json=payload)
            response.raise_for_status()
            generated_text = response.json()["choices"][0]["message"]["content"].strip()
            sentences = generated_text.split('\n')
            return [sentence.strip() for sentence in sentences if sentence.strip()], True
        except Exception as e:
            print(f"Error: {e}")
            attempt_count += 1
            time.sleep(2)
    return text, False  # 如果增强失败，返回原文本

# 示例调用
q = "What is the shape of the flag on top of the engineering vehicle?"
ans = enhance_text(q)
print(q)
print(ans[0][0].split("&&"))