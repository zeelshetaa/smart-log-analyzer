def generate_summary(df, anomalies):
    summary = {
        "total_logs": len(df),
        "info_logs": len(df[df["level"] == "INFO"]),
        "warning_logs": len(df[df["level"] == "WARNING"]),
        "error_logs": len(df[df["level"] == "ERROR"]),
        "anomalies_detected": len(anomalies)
    }

    return summary
