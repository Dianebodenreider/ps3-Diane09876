def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers (floats).
    """
    numbers = []
    while True:
        raw = input("Enter a number (or 'done'): ").strip()
        if raw.lower() == "done":
            break
        try:
            num = float(raw)
            numbers.append(num)
        except ValueError:
            print(" Invalid input. Please enter a numeric value or 'done'.")
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers (only for integer values)
    - odd_count: count of odd numbers (only for integer values)
    """
    if not numbers:
        return None

    count = len(numbers)
    total = sum(numbers)
    avg = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    # Count even/odd only for values that are integers (e.g., 2.0 counts as 2)
    ints = [int(x) for x in numbers if float(x).is_integer()]
    even_count = sum(1 for n in ints if n % 2 == 0)
    odd_count = sum(1 for n in ints if n % 2 != 0)

    return {
        "count": count,
        "sum": total,
        "average": avg,
        "minimum": minimum,
        "maximum": maximum,
        "even_count": even_count,
        "odd_count": odd_count,
    }


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    if analysis is None:
        print("No numbers to analyze.")
        return

    print("\nNumber Analysis")
    print("-" * 30)
    print(f"Count     : {analysis['count']}")
    print(f"Sum       : {analysis['sum']:.2f}")
    print(f"Average   : {analysis['average']:.2f}")
    print(f"Minimum   : {analysis['minimum']:.2f}")
    print(f"Maximum   : {analysis['maximum']:.2f}")
    print(f"Even nums : {analysis['even_count']}")
    print(f"Odd nums  : {analysis['odd_count']}")


def main():
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    numbers = get_numbers_from_user()
    if not numbers:
        print("No numbers entered!")
        return
    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    main()
