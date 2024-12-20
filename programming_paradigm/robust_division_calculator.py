def safe_divide(numerator, denominator):
    try:
        return numerator/denominator
    except ZeroDivisionError:
        print("error")
    except ValueError:
        print("error")