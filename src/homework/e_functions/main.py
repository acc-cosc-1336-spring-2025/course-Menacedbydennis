def convert_seconds_to_time(seconds):
    hours = seconds // 3600 # Calculate hours
    minutes = (seconds % 3600) // 60 # Calculate minutes
    seconds_remaining = seconds % 60 # Calculate remaining seconds

    time_format = f "{hours : 02} :{minutes : 02} :{seconds_remaining : 02}"
    return time_format

input_seconds = 3800

time = convert_seconds_to_time(input_seconds)
print(time)