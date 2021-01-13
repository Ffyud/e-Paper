#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import json
import time
from waveshare_epd import epd2in13_V2
from datetime import datetime
import random
import logging
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.INFO)

def itereer_over_lijst():
    lijst = geef_een_lijst()
    logging.debug('Van start met een lijst van ' + str(len(lijst)) + ' quotes.')
    y = 0
    sec_wachten = 7200
    max_quotes_per_lijst = 3
    for quote in lijst:
        bouw_afbeelding_met_quote(quote)
        y = y+1
        time.sleep(sec_wachten)
        if(y >= max_quotes_per_lijst):
            logging.debug('Er zijn ' + str(max_quotes_per_lijst) +
                         ' quotes getoond, tijd voor een nieuwe lijst')
            itereer_over_lijst()


def geef_een_lijst():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    lijst_wat_te_tonen = []

    with open('../quotes.json') as jsonFile:
        quotes = json.load(jsonFile)

    for j in quotes:
        start_time = j['time']
        end_time = j['end-time']
        if(current_time > start_time and current_time < end_time):
            # controle op dag-specifieke quotes toevoegen
            quote = j['text']
            lijst_wat_te_tonen.append(quote)

    random.shuffle(lijst_wat_te_tonen)
    return lijst_wat_te_tonen


def bouw_afbeelding_met_quote(quote):
    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    font17 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 17)

    image = Image.new('1', (epd.height, epd.width), 255)  # Frame eerst poetsen
    draw = ImageDraw.Draw(image)
    logging.debug('Afbeelding maken van de gevonden quote.')
    
    # Breek zinnen af zodat het past op scherm
    def wrap_by_word(tekst, linebreakLocatie):
        gespletenTekst = tekst.split()
        resultaat = ''
        for i in range(0, len(gespletenTekst), linebreakLocatie):
            resultaat += ' '.join(gespletenTekst[i:i+linebreakLocatie]) + '\n'
        return resultaat

    # Centrale quote
    draw.multiline_text((10, 10), wrap_by_word(quote, 4), align="left", font=font17, fill=0)

    epd.display(epd.getbuffer(image))
    epd.sleep()

if __name__ == '__main__':
    itereer_over_lijst()
    # epd.Dev_exit()

# try:
#     itereer_over_lijst

# except IOError as e:
#     logging.info(e)

# except KeyboardInterrupt:
#     epd2in13_V2.epdconfig.module_exit()
#     exit()
