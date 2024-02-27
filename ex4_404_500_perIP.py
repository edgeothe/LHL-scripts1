
import re




with open(r"c:\users\Mr. Big\Desktop\apache_logs.txt","r") as myFile:
    # Read the file content
    file_content = myFile.read()

# Initialize a dictionary to store counts for each IP
ip_counts = {}


# Process the file content
for line in file_content.splitlines():
    # Use a regular expression pattern to match status codes
    match = re.search(r'\s(\d{3})\s', line)
    if match:
        status = match.group(1)
        if status in ("404", "500"):
            # Extract the IP address using a separate pattern
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                if ip not in ip_counts:
                    ip_counts[ip] = {"404": 0, "500": 0}
                ip_counts[ip][status] += 1
1
# Sort IPs alphabetically
sorted_ips = sorted(ip_counts.keys())
# Print counts for each IP
for ip in sorted_ips:
    counts = ip_counts[ip]
    print("IP:", ip)
    print("Number of occurrences of '404':", counts["404"])
    print("Number of occurrences of '500':", counts["500"])
    print()
