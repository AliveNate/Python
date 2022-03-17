



newline = "\n-----------------"



print(newline)
print("Remember that all keys in a dictionary have to be unique, no duplicate keys.")

monthCoverstions = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "Jul",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}


print(newline)
print(monthCoverstions)

print(newline)
print(monthCoverstions["Nov"])

print(newline)
print(monthCoverstions.get("Dec"))

print(newline)
print(monthCoverstions.get("XXX")) # Wrong key
print(monthCoverstions.get("XXX", "Not a valid key")) # Wrong key, with safety
