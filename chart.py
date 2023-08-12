import matplotlib.pyplot as plt
import seaborn as sns

weeks = ['Week 32', 'Week 33', 'Week 34', 'Week 35', 'Week 36']
values_a = [6, 7, 7.5, 8, 7.7]
values_b = [1000, 1100, 1050, 1200, 1100]

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

sns.lineplot(x=weeks, y=values_a, label='DeGod(ETH)', marker='o')
sns.lineplot(x=weeks, y=values_b, label='Overall', marker='s')

plt.xlabel('Week')
plt.ylabel('Value')
plt.title('Weekly Chart with Legends')
plt.legend()

plt.savefig('seaborn_weekly_chart.png')
