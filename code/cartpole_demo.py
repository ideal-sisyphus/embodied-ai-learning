import gymnasium as gym

# 创建 CartPole（倒立摆）环境
env = gym.make("CartPole-v1")
observation, info = env.reset()

print("环境初始化成功，开始 PD 控制测试...")

for step in range(200):  # 把100步改为200步，看看能坚持多久
    # PD控制：根据角度和角速度决定推的方向
    # observation[2] 是角度，observation[3] 是角速度
    if observation[2] + observation[3] > 0:
        action = 1  # 向右推
    else:
        action = 0  # 向左推
    
    # 执行动作，获取新状态
    observation, reward, terminated, truncated, info = env.step(action)
    
    # 检查是否结束
    if terminated or truncated:
        print(f"第 {step} 步：小车倒下或越界，环境重置！")
        observation, info = env.reset()

env.close()
print(f"🎉 演示结束！小车总共坚持了 {step + 1} 步！")  # 添加这行打印总步数
print("🎉 演示结束！你已经成功跑通了 CartPole 环境！")