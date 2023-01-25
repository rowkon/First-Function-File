def slugify(text):
    url = text.strip().lower().replace(" ", "-")
    while "--" in url:
        url = url.replace("--", "-")
    return url



# Title =  input("Enter Your Title Text: ")
# print(slugify(Title))