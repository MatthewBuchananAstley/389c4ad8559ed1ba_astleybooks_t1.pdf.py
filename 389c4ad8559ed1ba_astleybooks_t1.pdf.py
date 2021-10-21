#!/usr/bin/python3
#
# Met dit script kun je eenvoudig een pdf met voorblad genereren op de commandline.
# This script enables you to easily generate a pdf with a front cover.
#
# 2021 Matthew Buchanan Astley 

import os,sys

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()

try:
    outputfile = sys.argv[1]
    textfile = sys.argv[2]
    frontpageImage = sys.argv[3]
except IndexError:
    print("./389c4ad8559ed1ba_astleybooks_t1.pdf.py 'outputfile.pdf' 'textfile' 'frontpage image'") 
    sys.exit()

t1 = textfile.split('.')
t2 = open(textfile, "r")
t3 = t1[0].split('/')

#Title = t1[0]
Title = t3[-1]
#pageinfo = t1[0]
pageinfo = t3[-1]

def EerstePagina(canvas, doc):
    canvas.saveState()
    canvas.setTitle(Title)
    canvas.drawImage(frontpageImage,1,1,width=580,height=860)
    canvas.showPage()

def LaterePaginas(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

def c1():
    doc = SimpleDocTemplate(outputfile)
    Story = []
    style= styles["Normal"]
    for i in t2:
        i = i.replace('<br>','\n')
        Story.append(Paragraph(i, style))
    doc.build(Story, onFirstPage=EerstePagina, onLaterPages=LaterePaginas)  

c1()

