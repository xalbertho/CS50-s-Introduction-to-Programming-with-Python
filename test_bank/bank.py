def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting: str) -> int:
    s = greeting.strip().lower()
    if s.startswith("hello"):
        return 0
    if s.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
