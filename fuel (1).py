def main():
    while True:
        fraction = input("Enter the fuel fraction (in X/Y format): ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please try again.")

    gauge_str = gauge(percentage)
    print("Fuel percentage:", gauge_str)


def convert(fraction):
    numerator, denominator = map(int, fraction.split('/'))

    if denominator == 0 or numerator > denominator:
        raise ValueError

    percentage = numerator / denominator * 100

    return round(percentage)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()