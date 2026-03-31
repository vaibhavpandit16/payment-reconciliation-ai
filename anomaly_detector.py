def detect_anomalies(df):
    issues = {}

    # Missing settlements
    issues["missing_settlement"] = df[df["amount_settle"].isna()]

    # Late settlement
   
    late_settlement = df[
    df["settlement_date"].dt.month != df["date_txn"].dt.month
]

    # Amount mismatch
    issues["amount_mismatch"] = df[
        df["amount_txn"] != df["amount_settle"]
    ]

    # Duplicate
    issues["duplicates"] = df[
        df.duplicated(subset="transaction_id", keep=False)
    ]

    # Refund without original
    issues["invalid_refunds"] = df[
        (df["amount_settle"] < 0) & (df["amount_txn"].isna())
    ]

    return issues