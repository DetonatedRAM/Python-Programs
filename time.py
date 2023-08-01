current_time_Str = input("What is the current time (in hours 0-23)?")
wait_time_Str = input("How many hours do you want to wait")

currentTimeInt = int(current_time_Str)
waitTimeInt = int(wait_time_Str)

finalTime_Int = currentTimeInt + waitTimeInt
print(finalTime_Int)
