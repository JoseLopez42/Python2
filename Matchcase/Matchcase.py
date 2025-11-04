method = "POST"

match method:
    case "GET":
        print("Fetching Resource...")
    case "POST":
        print("Creating Resource...")
    case "PUT":
        print("Updating Resource...")
    case "DELETE":
        print("Deleting Resource...")
    case _:
        print("Unsupported HTTP method.")
