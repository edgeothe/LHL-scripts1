

count_404 = 0
count_500 = 0

with open(r"c:\users\Mr. Big\Desktop\apache_logs.txt","r") as myFile:
    for line in myFile:
    # Check for 404 errors
        if "404" in line:
            count_404 += 1
    # Check for 500 errors
        if "500" in line:
            count_500 += 1
    # Extract DATETIME information in [ ]
        if "[" in line and "]" in line:
            datetime_info = line.split("[")[1].split("]")[0]

    # Assuming you want to check if the time is between 00:00 and 14:00
            if "00:00" <= datetime_info.split()[1] <= "14:00":
            # Write DATETIME information to the new file
                newFile.write(f"DATETIME: {datetime_info}\n")
# Print the counts of 404 and 500 errors
print("Number of occurrences of '404':", count_404)
print("Number of occurrences of '500':", count_500)
# Open the new file for writing
with open("results.txt", "w") as newFile:
    # Write the counts of 404 and 500 errors to the new file
    newFile.write(f"Number of occurrences of '404': {count_404}\n")
    newFile.write(f"Number of occurrences of '500': {count_500}\n")