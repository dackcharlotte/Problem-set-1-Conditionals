def main ():
    time = input("what's the time ")
    n = convert(time)
    if n >= 7.00 and n <=8.00:
        print("Breakfast time")
    elif n >= 12.00 and n <= 13.00:
        print("Lunch time")
    elif n >= 18.00 and n <= 19.00:
        print("Dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    n = float(hours) + float(minutes)/60
    return n

if __name__ == "__main__":
    main()
