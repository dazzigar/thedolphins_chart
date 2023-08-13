import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
x = [33, 34, 35, 36]
y = [19500, 18000, 21000, 20500]

# Set up Seaborn style with muted color palette
sns.set(style="white", palette="muted")

# Set custom color palette
custom_palette = ["#FF5733"]
sns.set_palette(custom_palette)

# Create a line plot with filled area
plt.figure(figsize=(8, 6))
sns.lineplot(x=x, y=y, color='green',  marker='o', label='USDC')

# Add text labels to each point
for i, txt in enumerate(y):
    plt.text(x[i], y[i], f'{txt}', ha='center', va='bottom', fontsize=10, weight='bold')

# Fill the area under the line with less opaque color
plt.fill_between(x, y, alpha=0.4, color='green')

# Set x and y value limits
plt.xlim(33, 36)
plt.ylim(15000, 25000)

# Set number of ticks on x and y axes
plt.xticks(range(33, 37))  # Set the range of x ticks (1 to 5 in this case)

plt.xlabel('Weeks of August')
plt.ylabel('Value')
plt.title('Treasury Value')
plt.legend()

# Set custom background color
plt.gca().patch.set_facecolor('#ebf5eb')

# Create the figure object and set its facecolor to white (for inside of the chart)
fig = plt.gcf()
fig.set_facecolor('white')

# plt.show()
plt.savefig('seaborn_weekly_chart.png')
