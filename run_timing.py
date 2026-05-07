def run_timing():
    total_duration = 0
    total_run = 0
    average = 0

    while True:
        duration = input("Enter the Duration You Take to Complete a 10KM Run: ")
        if not duration:
            break

        total_duration += float(duration)
        total_run += 1

    average = total_duration / total_run

    return f"Average Duration is {average} Minutes Over {total_run} Runs"


print(run_timing())
