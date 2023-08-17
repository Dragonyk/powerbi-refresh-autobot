import logging
from datetime import datetime

logging.basicConfig(filename="report.log",level=logging.INFO)

def write_info(txt):
    current_dt = datetime.now().strftime('%d/%m/%Y %H:%M')
    logging.info('['+current_dt+'] '+txt)