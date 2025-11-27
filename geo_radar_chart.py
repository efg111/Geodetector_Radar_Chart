import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# --- 1. 数据准备 ---
# 假设有5个变量 (因子)
labels = np.array(['X1', 'X2', 'X3', 'X4', 'X5'])
num_vars = len(labels)

# 模拟5个年份的单因子解释力(q值)数据 (范围通常在0-1之间)
# 这里的数值是随机生成的，您可以替换为您真实的数据
data = {
    '1982': [0.23, 0.21, 0.46, 0.58, 0.45],
    '1992': [0.25, 0.16, 0.38, 0.56, 0.35],
    '2002': [0.25, 0.24, 0.51, 0.42, 0.41],
    '2012': [0.25, 0.26, 0.48, 0.64, 0.51],
    '2022': [0.45, 0.34, 0.39, 0.58, 0.55]
}

# --- 2. 绘图设置 ---
# 设置全局字体为新罗马 (Times New Roman)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.rcParams['font.size'] = 16

# 计算角度：将圆周分为 num_vars 份
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# 让雷达图闭合：将第一个角度和数据重复拼接到列表末尾
angles += angles[:1]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# --- 3. 绘制雷达图 ---
# 设置颜色列表，用于区分不同年份
colors = ['#d73027', '#fc8d59', '#fee090', '#91bfdb', '#4575b4']  # 红到蓝的渐变色系
years = list(data.keys())

for idx, year in enumerate(years):
    values = data[year]
    # 数据闭合
    values += values[:1]

    # 绘制线条
    ax.plot(angles, values, color=colors[idx], linewidth=1.5, label=year, marker='o', markersize=4)
    # 填充颜色 (设置透明度 alpha)
    ax.fill(angles, values, color=colors[idx], alpha=0.15)

# --- 4. 美化图表细节 ---
# 设置顺时针方向，0度在正上方 (符合图片中的样式)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# 设置标签显示
# 将标签放置在对应的角度上
ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=16, fontweight='bold')

# 设置径向刻度 (y轴)
# 1. 设置网格线位置
ticks = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70]
ax.set_yticks(ticks)
# 2. 隐藏默认的刻度标签
ax.set_yticklabels([])

# 3. 手动添加标签到 X1 轴 (角度为0) 的交点处
for t in ticks:
    # 参数: (角度, 半径, 文本, ...)
    # ha='center', va='center' 确保文字中心与交点重合
    # bbox 添加白色背景，避免网格线穿过文字影响阅读
    ax.text(0, t, f"{t:.2f}", ha='center', va='center', fontsize=14, fontweight='bold', color='black',
            bbox=dict(facecolor='none', edgecolor='none', alpha=0.7, pad=1))

plt.ylim(0, 0.70)  # 设置y轴范围

# 移除极坐标默认的圆形外边框，让它看起来更像多边形（可选，取决于审美）
ax.spines['polar'].set_visible(True)

# 添加图例
# 将图例放在图表旁边，以免遮挡数据
legend_font = FontProperties(family='Times New Roman', size=14, weight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.0), frameon=False, prop=legend_font)

# 添加标题
plt.title("Single-factor Explanation Power (q-value)", y=1.08, fontsize=16, fontweight='bold')

# 保存图片或显示
plt.tight_layout()
# plt.savefig('radar_chart.png', dpi=300, bbox_inches='tight') # 如果需要保存去掉注释
plt.show()