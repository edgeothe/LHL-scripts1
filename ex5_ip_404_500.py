

parsed_data = []
with open(r"c:\users\Mr. Big\Desktop\apache_logs.txt","r") as myFile:
    # Read the file content
    file_content = myFile.read()

    prev_time = ""
    data = {}
for line_number, line in enumerate(file_content.splitlines(), start=1):
    try:
        time = line.split("[")[1].split("]")[0].split(" ")[0]
        status_code = line.split('"')[2].split(" ")[1]

        if prev_time != "":
            if time == prev_time:
                data[time]["count"] = data[time]["count"] + 1
                if status_code in data[time]:
                    data[time][status_code] = data[time][status_code] + 1
                else:
                    data[time][status_code] = 1
            else:
                prev_time = time
                parsed_data.append(data)
                data = {}
                data[time] = {"count": 1, status_code: 1}

        else:
            prev_time = time
            data[time] = {"count": 1, status_code: 1}
    except Exception as e:
        print(f"Error processing line {line_number}: {line}")
        print(f"Error details: {e}")
for i in parsed_data:
    print(i)
    with open('results2.txt', 'a') as file:
        # Write content to the file
        file.write(str(i) + '\n')
