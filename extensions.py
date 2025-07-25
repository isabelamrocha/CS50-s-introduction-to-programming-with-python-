#prompt the user for the name of a file
file = input("File name: ").lower().strip()
#check what type of file it is and output the media type
if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith("jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
