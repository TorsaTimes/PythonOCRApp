import cv2
import pytesseract
# import module
from pdf2image import convert_from_path
import os.path
from os import path

list_of_filename = []

def check_file_ex(f):

      # Split the extension from the path and normalise it to lowercase.
      ext = os.path.splitext(f)[-1].lower()

      # Now we can simply use == to check for equality, no need for wildcards.
      if ext == ".pdf":
          print("is an pdf!")
          return "PDF"
      elif ext == ".png":
          print("is a png file!")
          return "PNG"
      elif ext == ".jpg":
        print("is a png file!")
        return "JPG"
      else:
          print("is an unknown file format.")

def extract_file(f):
  var = check_file_ex(f)
  pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
  
  if var == "PDF":
    # Store Pdf with convert_from_path function
    images = convert_from_path(f)
    counter = 0
    for i in range(len(images)):
      
          # Save pages as images in the pdf
        images[i].save('page'+ str(i) +'.png', 'PNG')
        counter = i
        
    print(" PNG generated")
    counter = counter + 1
    for x in range(0,counter):
      filename_var = "page" + str(x) + ".png"
      list_of_filename.append(filename_var)
      if path.exists(filename_var):
        extract(filename_var)
      else:
        break
  elif var == "PNG":
    extract(f)
  
  remove_files()

def extract(filename):
  img = cv2.imread(filename)
  text = pytesseract.image_to_string(img)
  print(text)
  print("############"+ filename +"###################")

def remove_files():
  for x in list_of_filename:
    os.remove(x)
  list_of_filename.clear()
