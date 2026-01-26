def main():

  file = input("File name: ")
  filenew = normalize(file)

  if  filenew.endswith("gif"):
      print("image/gif")

  elif  filenew.endswith("jpg"):
      print("image/jpeg")

  elif  filenew.endswith("jpeg"):
      print("image/jpeg")

  elif  filenew.endswith("png"):
      print("image/png")

  elif  filenew.endswith("pdf"):
      print("application/pdf")

  elif  filenew.endswith("txt"):
      print("text/plain")

  elif  filenew.endswith("zip"):
      print("application/zip")

  else:
      print("application/octet-stream")

def normalize(z):
    return z.replace(" ", "").lower()

main()
