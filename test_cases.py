from data_generator import generate_data
from reconciliation import reconcile
from anomaly_detector import detect_anomalies

txn, sett = generate_data()
merged = reconcile(txn, sett)
issues = detect_anomalies(merged)

assert len(issues["late_settlement"]) > 0
assert len(issues["duplicates"]) > 0
assert len(issues["invalid_refunds"]) > 0

print("All test cases passed ✅")