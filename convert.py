import img2pdf
import os
from fpdf import FPDF
import glob
from PIL import Image
import random

# STEP 2
# file path you want to extract images from







def convert(ROI_number):
    imagelist = glob.glob('temp/*')
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    print("ROI",ROI_number)
    pdf.set_auto_page_break(0)
    # imagelist is the list with all image filenames
    for imageFile in imagelist:
        cover = Image.open(imageFile)
        width, height = cover.size

        # convert pixel in mm with 1px=0.264583 mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        # given we are working with A4 format size 
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

        # get page orientation from image size 
        orientation = 'P' if width < height else 'L'

        #  make sure image size is not greater than the pdf format size
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

        pdf.add_page(orientation=orientation)

        pdf.image(imageFile, 0, 0, width, height)
    pdf.output("result/converted_pdf.pdf", "F")
    


 

#also works kinda
'''

def convert():
    imagelist = glob.glob('temp/*')
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.set_auto_page_break(0)
    # imagelist is the list with all image filenames
    for image in imagelist:
        pdf.add_page()
        pdf.image(image,0,0,210,297)
    pdf.output("yourfile.pdf", "F")


'''
