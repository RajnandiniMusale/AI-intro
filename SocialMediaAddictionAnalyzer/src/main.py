import pandas as pd
from visualize import show_pie_chart, show_line_graph, show_gauge
from addiction_rules import get_addiction_level

# Step 1: Load data
df = pd.read_csv('../data/usage_data.csv')

# Step 2: Calculate averages
df['Total_Social_Time'] = df[['Instagram', 'YouTube', 'WhatsApp', 'Facebook']].sum(axis=1)
avg_social = df['Total_Social_Time'].mean()
avg_productivity = df['Productivity_Hours'].mean()

# Step 3: Use rule-based AI logic
addiction, message = get_addiction_level(avg_social, avg_productivity)

# Step 4: Display result
print(f"\nAverage Screen Time: {avg_social:.2f} hrs/day")
print(f"Average Productivity: {avg_productivity:.2f} hrs/day")
print(f"Predicted Addiction Level: {addiction}\n")
print(message)

# Step 5: Visualize data
show_pie_chart(df)
show_line_graph(df)
show_gauge(addiction)
