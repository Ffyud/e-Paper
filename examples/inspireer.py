#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("testje!")
    
    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    font14 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 14)
    font17 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 17)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    
    image = Image.new('1', (epd.height, epd.width), 255)  # Frame eerst poetsen 
    draw = ImageDraw.Draw(image)
    draw.transpose(Image.ROTATE_180) # Draai om zodat kabel boven zit

    # Breek zinnen af zodat het past op scherm
    def wrap_by_word(tekst, linebreakLocatie):
        gespletenTekst = tekst.split()
        resultaat = ''
        for i in range(0, len(gespletenTekst), linebreakLocatie):
            resultaat += ' '.join(gespletenTekst[i:i+linebreakLocatie]) + '\n'

        return resultaat
    
    # Kader
    draw.rectangle([(0,0),(250,122)],width=5, outline = "#000000")

    # Centrale quote
    mainQuote = 'Goedemorgen, het is donderdag en dus bijna weekend! Tip: stel realistische doelen voor je dag.'
    draw.multiline_text((10, 10), wrap_by_word(mainQuote, 4), align= "left", font = font17, fill = 0)
    
    epd.display(epd.getbuffer(image))
    
    epd.sleep()
    time.sleep(3)
    epd.Dev_exit()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
