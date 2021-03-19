# Deleting $
greeting = "Welcome!$"
greeting = greeting.strip("$")
print(greeting)

# Adding 0 at start of the string
day = "4"
day = day.zfill(2)
print(day)

# Replace white space by underscore
filename = "monday report.pdf"
filename = filename.replace(" ", "_")
print(filename)

# Count the "Good" iterations without regarding the case 
shakespeare = "Good night, good night! parting is such sweet sorrow, That I shall say good night till it be morrow."
shakespeare = shakespeare.lower()
good_count = shakespeare.count("good")
print(good_count)

# Dynamic string. Create this string : Your monday_report.pdf file is ready
filename = "monday report.pdf"
filename = filename.replace(" ", "_")
message = f"Your {filename} file is ready"
print(message)

# Output the "m"
filename = "monday_report.pdf"
slice = filename[0]
print(slice)

# Output the "mon"
filename = "monday_report.pdf"
slice = filename[:3]
print(slice)

# Output the "pdf"
filename = "monday_report.pdf"
slice = filename[-3:]
print(slice)

# Output the "report"
filename = "monday_report.pdf"
slice = filename[-10:-4]
print(slice)