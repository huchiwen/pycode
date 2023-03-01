# 代码是测试zip的用法
scores = [80, 85, 90, 75, 95]
weights = [0.2, 0.2, 0.2, 0.2, 0.2]

zipped = zip(scores,weights)

for k,v in zipped:
  print(k,v)
