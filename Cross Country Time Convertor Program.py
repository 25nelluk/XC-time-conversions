import sys

def convert_to_seconds(time: str) -> int:
    """Converts a time in XX:XX.XX format into seconds

    time: str - The time represented as a string
    min_to_s: list - Helps convert a minutes place into its seconds counterpart (Ex. 10min = 600s)
    total_s: int - Captures the total number of seconds
    colon: int - Ensures an accurate conversion with list min_to_s whether time is above or below 10 minutes

    RETURNS: int (sec) (rounded to the nearest hundredths place)"""

    min_to_s: list = [600, 60, 10, 1, 0.1, 0.01]
    total_s: int = 0
    colon = time.index(":") % 2

    time = time.replace(":", "")
    time = time.replace(".", "")

    for i, v in enumerate(time):
        total_s += int(v) * min_to_s[i + colon]

    return round(total_s, 2)


def convert_to_minutes(s: float) -> str:
    
    minutes = int(s / 60)
    seconds = round(s - (minutes * 60), 2)
    if seconds < 10:
        return f"{minutes}:0{seconds:.2f}"
    return f"{minutes}:{seconds:.2f}"


def find_pace() -> str:
    dist: float = float(input("Enter a distance (miles): "))
    t: str = input("Enter a time: ")
    time: int = convert_to_seconds(t)

    return convert_to_minutes(time / dist)


def find_time() -> str:
    dist: float = float(input("Enter a distance (miles): "))
    p: str = input("Enter a pace: ")
    pace: int = convert_to_seconds(p)

    return convert_to_minutes(dist * pace)


def find_distance() -> int:
    t: str = input("Enter a time: ")
    p: str = input("Enter a pace: ")

    time: int = convert_to_seconds(t)
    pace: int = convert_to_seconds(p)

    return round(time / pace)


def find_average() -> str:
    num_of_times = int(input("How many times would you like to add?: "))
    total_s = 0
    for val in range(1, num_of_times+1):
        time = input(f"Enter time #{val}: ")
        total_s += convert_to_seconds(time)
    return convert_to_minutes(total_s/num_of_times)
    

def find_spread() -> str:
    time1: str = input("Enter time #1: ")
    time2: str = input("Enter time #2: ")

    t1: int = convert_to_seconds(time1)
    t2: int = convert_to_seconds(time2)

    if t1 > t2:
        return convert_to_minutes(t1-t2)
    else:
        return convert_to_minutes(t2-t1)


def get_commands() -> None:
    commands: dict = {
        "Find pace ('pace'):": "Finds the pace by inputting a distance and time",
        "Find time ('time'):": "Finds the time by inputting a pace and distance",
        "Find distance ('distance'):": "Finds the distance by inputting the pace and time",
        "Find average ('average'):": "Finds the average of a certain amount of times",
        "Find spread ('spread'):": "Finds the spread of two times",
        "View commands ('commands'):": "View all of the commands you can run",
    }

    print("-------------------------------------------------------------")
    for i, v, in commands.items():
        print(i, v)
    print("-------------------------------------------------------------")

def main() -> None:

    while True:
        print("Type 'commands' for more commands")
        user_input: str = input("What would you like to find?: ").lower()

        match user_input:
            case "pace":
                print(f"The pace is {find_pace()}")
            case "time":
                print(f"The time is {find_time()}")
            case "distance":
                print(f"The distance is {find_distance()}")
            case "average":
                print(f"The average time is {find_average()}")
            case "spread":
                print(f"The spread is {find_spread()}")
            case "commands":
                get_commands()
            case _:
                print("Invalid input.")

        status: str = input("Are there any other things you would like to do (y/n)? ").lower()

        match status:
            case "y" | "yes":
                pass
            case "n" | "no":
                sys.exit()
    

if __name__ == "__main__":
    main()
