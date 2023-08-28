
def main():
    user_time = input("What time is it: ")
    n = convert(user_time)
    if 7 <= n <= 8:
        print("breakfast time")
    elif 12 <= n <= 13:
        print("lunch time")
    elif 18 <= n <= 19:
        print("dinner time")

# convert time to decimal scale
def convert(time):
    hours, minutes = time.split(":")
    return float(int(hours) + int(minutes) / 60)


if __name__ == "__main__":
    main()