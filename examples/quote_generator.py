import json
import time
import random
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def itereer_over_lijst():
    lijst = geef_een_lijst()
    logging.debug('Van start met een lijst van ' + str(len(lijst)) + ' quotes.')
    i = 0
    sec_wachten = 5
    max_quotes_per_lijst = 10
    for quote in lijst:
        bouw_afbeelding_met_quote(quote)
        i = i+1
        time.sleep(sec_wachten)
        if(i >= max_quotes_per_lijst):
            logging.debug('Er zijn ' + str(max_quotes_per_lijst) + ' quotes getoond, tijd voor een nieuwe lijst')
            itereer_over_lijst()

def geef_een_lijst():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    lijst_wat_te_tonen = []

    with open('../quotes.json') as jsonFile:
        quotes = json.load(jsonFile)

    for i in quotes:
        start_time = i['time']
        end_time = i['end-time']
        if(current_time > start_time and current_time < end_time):
            # controle op dag-specifieke quotes toevoegen
            quote = i['text']
            lijst_wat_te_tonen.append(quote)

    random.shuffle(lijst_wat_te_tonen)
    return lijst_wat_te_tonen

def bouw_afbeelding_met_quote(quote):
    return quote
    # drawen op het scherm (voor nu printen)

if __name__ == '__main__':
    itereer_over_lijst()
