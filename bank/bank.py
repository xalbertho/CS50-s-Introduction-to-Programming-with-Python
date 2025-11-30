
saludo=input("Greeting:\n").strip()

match saludo:
    case "Hello":
        print("$0")
    case "Hello, Newman":
        print("$0")
    case "How you doing?":
        print("$20")
    case ("What's happening?"):
        print("$100")
    case ("What's up?"):
        print("$100")