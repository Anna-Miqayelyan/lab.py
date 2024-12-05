from collections import Counter

log_file = 'file.log'  
output_file = 'log_summary.txt'

total_requests = 0
status_code_counts = Counter()
ip_addresses = Counter()

with open(log_file, 'r') as f:
    for line in f:
        total_requests += 1

        parts = line.split()
        if len(parts) >= 9: 

            ip = parts[0]
            status_code = parts[-2]  
            if status_code in {'200', '404', '500'}:
                status_code_counts[status_code] += 1

            ip_addresses[ip] += 1

most_common_ips = ip_addresses.most_common(3)

summary = [
    f"Total: {total_requests}",
    "Requests:",
]
summary.extend([f"{code}: {count}" for code, count in status_code_counts.items()])
summary.append("3 IP :")
summary.extend([f"{ip}: {count}" for ip, count in most_common_ips])

with open(output_file, 'w') as f:
    f.write("\n".join(summary))

print(f"Log summary: {output_file}")
