import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt

# 1. 定义要测试的参数组合 (Kp, Kd)
# 你可以随意修改这些数字，看看不同组合的效果
param_combos = [
    (1.0, 1.0),
    (5.0, 1.0),
    (1.0, 0.1),
    (10.0, 5.0),
    (0.5, 0.5),
    (-1.0, -1.0),  # 故意写反！看它怎么瞬间倒下
    (999.0, 999.0) # 极端参数，看它怎么震荡
]

EPISODES = 10      # 每个参数组合跑 10 局
MAX_STEPS = 500   # 让不好的参数自己暴雷

results = []
env = gym.make("CartPole-v1")

print("开始自动扫参测试...")
for Kp, Kd in param_combos:
    total_steps = 0
    for episode in range(EPISODES):
        observation, info = env.reset()
        step = 0
        for step in range(MAX_STEPS):
            # PD 控制逻辑
            if Kp * observation[2] + Kd * observation[3] > 0:
                action = 1
            else:
                action = 0
            
            observation, reward, terminated, truncated, info = env.step(action)
            
            if terminated or truncated:
                break
        total_steps += (step + 1)
    
    avg_steps = total_steps / EPISODES
    results.append(avg_steps)
    print(f"Kp={Kp}, Kd={Kd} -> 平均坚持步数: {avg_steps:.1f}")

env.close()

# 2. 自动画图
labels = [f"Kp={kp}\nKd={kd}" for kp, kd in param_combos]
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, results, color=['red', 'orange', 'blue', 'green', 'purple'])
plt.ylabel('Average Steps Survived')
plt.title('CartPole PD Control - Automated Parameter Sweep')
plt.ylim(0, MAX_STEPS + 20)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f"{yval:.1f}", ha='center', va='bottom')

plt.savefig('code/cartpole_auto_sweep.png')
print("📊 自动扫参图表已保存至 code/cartpole_auto_sweep.png")