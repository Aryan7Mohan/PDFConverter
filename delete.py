import img2pdf
import os
from fpdf import FPDF
import glob
from PIL import Image

def delete():
 
    dir = 'temp/'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)
