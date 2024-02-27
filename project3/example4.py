
import re
import re




with open(r"c:\shared\apache_logs.txt","r") as myFile:
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
# Open a file in append mode ('a')
# If the file doesn't exist, it will be created; if it exists, its content will be appended
    with open('output.txt', 'a') as file:
    # Write content to the file
        file.write(f"IP: {ip}\n")
        file.write(f"Number of occurrences of '404': {counts['404']}\n")
        file.write(f"Number of occurrences of '500': {counts['500']}\n")

print(f"IP: {ip}")
print(f"Number of occurrences of '404': {counts['404']}")
print(f"Number of occurrences of '500': {counts['500']}")
print("See output.txt for the results.")