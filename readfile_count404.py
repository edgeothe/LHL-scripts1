#with the “apache_logs.txt" file, open it for read, “r”, and set its contents as a string to
#the variable “myFile”
count = 0
count2 = 0
with open(r"c:\users\Mr. Big\Desktop\apache_logs.txt","r") as myFile: 
    for line in myFile:
        
        #calculate the number of 404 errors in the file
       
        if "404" in line:
            count += 1
        count2 += 1
print("Number of occurrences of '404':", count)
print("Total no. of lines", count2)