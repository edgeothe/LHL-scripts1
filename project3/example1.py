count_404 = 0
count_500 = 0
#file_path = "C:\Shared\apache_logs.txt"
with open(r"c:\shared\apache_logs.txt", "r") as logFile:
     for line in logFile:
        if "404" in line:
            count_404 += 1
        if "500" in line:
            count_500 += 1
print("number of '404':", count_404)
print("Number of '500':", count_500)