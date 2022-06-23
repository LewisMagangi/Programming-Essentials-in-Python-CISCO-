hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

print(((hour + (dura // 60) + (((dura % 60) + mins) // 60)) % 24), ":", ((dura + mins) % 60))# Write your code here.
