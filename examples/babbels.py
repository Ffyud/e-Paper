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

    # Drawing on the image
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    
    logging.info("1.Drawing on the image...")
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    
    # draw.rectangle([(0,0),(50,50)],outline = 0)
    # draw.rectangle([(55,0),(100,50)],fill = 0)
    # draw.line([(0,0),(50,50)], fill = 0,width = 1)
    # draw.line([(0,50),(50,0)], fill = 0,width = 1)
    # draw.chord((10, 60, 50, 100), 0, 360, fill = 0)
    # draw.ellipse((55, 60, 95, 100), outline = 0)
    # draw.pieslice((55, 60, 95, 100), 90, 180, outline = 0)
    # draw.pieslice((55, 60, 95, 100), 270, 360, fill = 0)
    # draw.polygon([(110,0),(110,50),(150,25)],outline = 0)
    # draw.polygon([(190,0),(190,50),(150,25)],fill = 0)
    draw.text((120, 60), 'Hallo Babbels!', font = font24, fill = 0)
    epd.display(epd.getbuffer(image))
    time.sleep(2)
        
    
    logging.info("Goto Sleep...")
    epd.sleep()
    time.sleep(3)
    epd.Dev_exit()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
