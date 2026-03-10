import re
import pandas as pd

log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'

def parse_logs(file_path):
    data = []

    with open(file_path, "r") as file:
        for line in file:
            match = re.match(log_pattern, line)
            if match:
                timestamp, level, message = match.groups()
                data.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message
                })

    return pd.DataFrame(data)