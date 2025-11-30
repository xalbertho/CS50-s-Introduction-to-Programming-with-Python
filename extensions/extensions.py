text=input("File name: ").strip().lower()

pos=text.find('.')
text=text[pos+1:]
#print(text.find('.'))
if '.' in text:
    pos2=text.find('.')
    text=text[pos2+1:]
#print(text)


match text:
    case "gif":
        print("image/gif")
    case ("jpg" | "jpeg"):
        print("image/jpeg")
    case ("png"):
        print("image/png")
    case("pdf"):
        print("application/pdf")
    case("txt"):
        print("text/plain")
    case ("zip"):
        print("application/zip") 
    case default:
        print("application/octet-stream")
