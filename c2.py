from flask import Flask
from flask import Flask, flash, request,render_template,redirect

from werkzeug.utils import secure_filename
from functions import *
import cv2
import pytesseract
from PyPDF2 import PdfReader
f=[]
b=[]
app = Flask(__name__,template_folder='templates')
@app.route('/',methods =["GET", "POST"])
def home():
    pred=""
    img=""
    if request.method == "POST":
       print("vfbfb")
       tweet_input = request.form.get("txt")
       file = request.files["file"]
       if file.filename!="":
           
            print(file.filename)
            file.save(secure_filename(file.filename))
           # read image
            text=""
            if "jpeg" in file.filename or "jpg" in file.filename or "png" in file.filename:
                img = cv2.imread(file.filename)

                # configurations
                config = ('-l eng --oem 1 --psm 3')

                # pytessercat
                pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
                text = pytesseract.image_to_string(img, config=config)
            elif "txt" in file.filename:
                with open(file.filename,"r") as f:
                    text=f.read()
            elif "pdf" in file.filename:
                reader = PdfReader(file.filename)
                page = reader.pages[0]
                text = page.extract_text()
            prediction = custom_input_prediction(text)
            print(prediction)
            if prediction == "cyberbullying":
                img="static/cyberbullying.jpeg"
            elif prediction == "not cyberbullying":
                img="static/not_cyberbullying.png"
             
            
       if  tweet_input!="": 
                prediction = custom_input_prediction(tweet_input)
                print(prediction)
                if prediction == "cyberbullying":
                    img="static/cyberbullying.jpeg"
                elif prediction == "not cyberbullying":
                    img="static/not_cyberbullying.png"
    print(pred)
    return render_template('c.html',pred=pred,imag=img)


if __name__ == "__main__":
    app.run(debug=True,port=2000)
