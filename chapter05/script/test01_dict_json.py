import json

# 定义字典

data1 = {
    "name": "字典名",
    "age": 38
}

# 调用dumps将data转换为json
print(type(data1))
d1 = json.dumps(data1, ensure_ascii=False)
print(type(d1))
print(d1)

# 定义字符串

data2 = '{"name": "名称", "age": 38 }'

# 调用loads将data2转换为字典

print(type(data2))
d2 = json.loads(data2)
print(type(d2))
print(d2)

