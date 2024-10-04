print("(Some final times/paces may be formatted wrong)")
print("Find: distance, time, or pace")
conv_type = input("1) What would you like to find?: ")

class TimeConvert:

    def __init__(self, x, y):
        self.list = list
        self.x = x
        self.y = y

    def find_distance(self):
        pace_s = TimeConvert.time_to_seconds(p)
        time_s = TimeConvert.time_to_seconds(t)
        convert = int(time_s)/int(pace_s)

        return convert

    def find_time(self):
        pace_s = TimeConvert.time_to_seconds(p)
        convert = float(d) * int(pace_s)
        converted_decimal = round(convert - (int(convert/60)*60), 2) # Converting decimal to time notation
        if converted_decimal == 0.0:
            converted_decimal = "00.0"
        converted_final = f"{int(convert/60)}:{converted_decimal}"

        return converted_final

    def find_pace(self):
        time_s = TimeConvert.time_to_seconds(t)
        convert = int(time_s)/float(d)
        converted_decimal = round(convert - (int(convert/60)*60), 2)  # Converting decimal to time notation
        converted_final = f"{int(convert/60)}:{int(converted_decimal)}"

        return converted_final
    
    def time_to_seconds(time):
        l = [digit for digit in time]
        time_s = 0

        if l[2] == ":":
            time_s += (int(l[0])*600) + (int(l[1])*60) + (int(l[3])*10) + (int(l[4])*1)
        else:
            time_s += (int(l[0])*60) + (int(l[2])*10) + (int(l[3])*1)

        if l[-2] == ".":
            time_s += (int(l[-1])*0.1)
        elif l[-3] == ".":
            time_s += (int(l[-2])*0.1) + (int(l[-1])*0.01)
        return time_s


if conv_type.lower() == "distance":
    p = input("2) Enter a pace (0:01-9:59): ")
    t = input("3) Amount of time (0:00-59:59): ")
    z = TimeConvert(p, t)
    print(f"Distance: {round(z.find_distance(), 2)} miles")

if conv_type.lower() == "time":
    p = input("2) Enter a pace (0:01-9:59): ")
    d = input("3) Distance (0.01 to 9.99): ")
    z = TimeConvert(p, d)
    print(f"Time: {z.find_time()}")

if conv_type.lower() == "pace":
    d = input("2) Distance (0.01-9.99): ")
    t = input("3) Amount of time (0:01-59:59): ")
    z = TimeConvert(d, t)
    print(f"Pace: {z.find_pace()}")