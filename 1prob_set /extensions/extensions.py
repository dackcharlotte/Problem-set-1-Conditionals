file_name = input ("File Name: ")

x = file_name.partition(".")

c = x[2]

c = c.strip()

match c:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf" | "PDF":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case "txt.pdf":
        print("application/pdf")
    case _:
        print("application/octet-stream")




