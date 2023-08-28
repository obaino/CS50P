def main():
    name = input("Enter filename: ").lower().strip().rsplit('.', 1)[-1]
    extension(name)

def extension(text):
    match text:
        case "gif":
            print("image/gif")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

# main()

if __name__ == "__main__":
    main()