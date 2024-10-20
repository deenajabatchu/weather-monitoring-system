import matplotlib.pyplot as plt

def plot_temperature_summary(daily_data):
    dates = list(daily_data.keys())
    avg_temps = [sum(temp for _, temp in daily_data[date]) / len(daily_data[date]) for date in dates]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, marker='o')
    plt.title('Average Daily Temperature')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()