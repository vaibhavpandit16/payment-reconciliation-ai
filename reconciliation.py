import pandas as pd

def reconcile(transactions, settlements):
    merged = pd.merge(
        transactions,
        settlements,
        on="transaction_id",
        how="outer",
        suffixes=("_txn", "_settle")
    )

    return merged