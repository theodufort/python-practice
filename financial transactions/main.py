import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas dataframe
df = pd.read_csv("data.csv")

# Create a new figure and axis object
fig, ax = plt.subplots()

# Plot the data using the line plot function
ax.plot(df["Date"], df["Open"])
ax.plot(df["Date"], df["High"])
ax.plot(df["Date"], df["Low"])
ax.plot(df["Date"], df["Close"])
ax.plot(df["Date"], df["Adj Close"])
ax.plot(df["Date"], df["Volume"])

# Set the x-axis label
plt.xlabel("Date")

# Set the y-axis labels for each plot
plt.ylabel("Open", color="blue")
plt.ylabel("High", color="red")
plt.ylabel("Low", color="green")
plt.ylabel("Close", color="orange")
plt.ylabel("Adj Close", color="purple")
plt.ylabel("Volume", color="yellow")

# Show the plot
plt.show()