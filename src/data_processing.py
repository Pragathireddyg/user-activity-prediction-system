import pandas as pd
import numpy as np

def generate_data(n=1000):
    np.random.seed(42)

    data = pd.DataFrame({
        "user_id": np.arange(n),
        "posts": np.random.randint(0, 20, n),
        "reactions": np.random.randint(0, 100, n),
        "days_active": np.random.randint(1, 30, n),
    })

    data["active_next_week"] = (
        (data["posts"] + data["reactions"]) > 50
    ).astype(int)

    return data


if __name__ == "__main__":
    df = generate_data()
    print(df.head())
    df.to_csv("data/user_data.csv", index=False)