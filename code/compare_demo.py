import matplotlib.pyplot as plt

# 模拟不同参数下的表现（数字)
labels = ['Random', 'Kp=5.0, Kd=1.0', 'Kp=1.0, Kd=0.1', 'Perfect PD (Kp=1.0, Kd=1.0)']
steps = [28, 55, 68, 200] # 把这里的数字换成你刚才实际跑出来的结果

# 画柱状图
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, steps, color=['red', 'orange', 'blue', 'green'])
plt.ylabel('Steps Survived')
plt.title('CartPole Performance Comparison (PD Control)')
plt.ylim(0, 220)

# 在柱子上标数字
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom')

# 保存图片到本地
plt.savefig('code/cartpole_pd_performance.png')
print("📊 图表已保存至 code/cartpole_pd_performance.png")