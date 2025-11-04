import matplotlib.pyplot as plt

def show_pie_chart(df):
    avg_usage = df[['Instagram', 'YouTube', 'WhatsApp', 'Facebook']].mean()
    plt.figure(figsize=(6,6))
    plt.pie(avg_usage, labels=avg_usage.index, autopct='%1.1f%%')
    plt.title("Percentage of Time on Each App")
    plt.show()

def show_line_graph(df):
    plt.figure(figsize=(8,5))
    plt.plot(df['Day'], df['Total_Social_Time'], label='Total Social Time', marker='o')
    plt.plot(df['Day'], df['Productivity_Hours'], label='Productivity Hours', marker='s')
    plt.title("Usage vs Productivity")
    plt.xlabel("Day")
    plt.ylabel("Hours")
    plt.legend()
    plt.show()

def show_gauge(level):
    colors = {'Low':'green','Moderate':'orange','High':'red'}
    plt.figure(figsize=(5,1))
    plt.barh(['Addiction Level'], [1], color=colors[level])
    plt.text(0.3, 0, level, fontsize=12, color='white')
    plt.title("Addiction Level Gauge")
    plt.show()
