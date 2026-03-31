import pandas as pd
import numpy as np
import os

def generate_data():
    np.random.seed(42)

    txn_ids = list(range(1, 21))

    transactions = pd.DataFrame({
        "transaction_id": txn_ids,
        "amount": np.random.randint(100, 1000, size=20),
        "date": pd.to_datetime("2024-03-01") + pd.to_timedelta(np.random.randint(0, 30, 20), unit="D")
    })

    settlements = transactions.copy()

    # ✅ Fix dtype issue
    settlements["amount"] = settlements["amount"].astype(float)

    # Add delay
    settlements["settlement_date"] = settlements["date"] + pd.to_timedelta(np.random.randint(1, 3, 20), unit="D")

    # Errors
    settlements.loc[0, "settlement_date"] = pd.to_datetime("2024-04-02")
    settlements.loc[1, "amount"] += 0.5

    # Duplicate
    settlements = pd.concat([settlements, settlements.iloc[[2]]])

    # Refund without original
    settlements = pd.concat([
        settlements,
        pd.DataFrame({
            "transaction_id": [999],
            "amount": [-200.0],
            "date": [pd.NaT],
            "settlement_date": [pd.to_datetime("2024-03-20")]
        })
    ])

    return transactions, settlements


if __name__ == "__main__":
    txn, sett = generate_data()

    # ✅ Fix folder issue
    os.makedirs("data", exist_ok=True)

    txn.to_csv("data/transactions.csv", index=False)
    sett.to_csv("data/settlements.csv", index=False)

    print("✅ Data generated successfully!")