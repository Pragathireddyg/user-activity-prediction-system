import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/user_data.csv")

# Basic info
print("Data Shape:", df.shape)
print(df.describe())

# Plot 1: Posts distribution
plt.hist(df["posts"])
plt.title("Posts Distribution")
plt.xlabel("Posts")
plt.ylabel("Count")
plt.show()

# Plot 2: Reactions distribution
plt.hist(df["reactions"])
plt.title("Reactions Distribution")
plt.xlabel("Reactions")
plt.ylabel("Count")
plt.show()