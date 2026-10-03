import gymnasium as gym

# 创建 CartPole（倒立摆）环境
env = gym.make("CartPole-v1")
observation, info = env.reset()

print("环境初始化成功，开始随机动作测试...")

for step in range(100):
    # 随机选择一个动作（0向左推，1向右推）
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        print(f"第 {step} 步：小车倒下或越界，环境重置！")
        observation, info = env.reset()

env.close()
print("🎉 演示结束！你已经成功跑通了 CartPole 环境！")
