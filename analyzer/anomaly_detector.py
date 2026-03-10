def detect_anomalies(df):
    suspicious_keywords = ["failed", "unauthorized", "error", "attack"]

    anomalies = df[df["message"].str.lower().str.contains('|'.join(suspicious_keywords))]
    
    return anomalies