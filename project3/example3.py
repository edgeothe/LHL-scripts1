
import re
from collections import Counter

status_count = {"404": 0, "500": 0}
ip_addresses = []

# with blob.open("r") as logFile:
with open(r"c:\shared\apache_logs.txt","r") as myFile:

    for line in myFile:
        # Use a regular expression pattern to match status codes
        match = re.search(r'\s(\d{3})\s', line)
        if match:
            status = match.group(1)
            if status in status_count:
                status_count[status] += 1
                # Extract the IP address using a separate pattern
                ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    ip = ip_match.group(1)
                    ip_addresses.append(ip)
print("Number of occurrences of '404':", status_count["404"])

print("Number of occurrences of '500':", status_count["500"])

ip_counts = Counter(ip_addresses)
sorted_ips = sorted(ip_counts, key=ip_counts.get, reverse=True)

print("Sorted IP addresses (most common to least):")
with open('output2.txt', 'a') as file:
    for ip in sorted_ips:
        file.write(f"{ip}: {ip_counts[ip]}\n")
        print(ip, ":", ip_counts[ip])
count_404 = status_count["404"]
count_500 = status_count["500"]