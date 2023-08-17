import subprocess
import os
import pyautogui as pag
import time
import schedule
import log_utils as ulog
import bot_settings as settings

#screen_width = pag.size().width
#screen_height = pag.size().height

powerbi_exe = r'C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe'

imgs_root = '.\\res\\'

img_atualizar   = imgs_root+'_powerbi_atualizar.png'
img_publicar    = imgs_root+'_powerbi_publicar.png'
img_salvar      = imgs_root+'_powerbi_salvar.png'
img_workspace   = imgs_root+'_powerbi_workspace.png'
img_selecionar  = imgs_root+'_powerbi_selecionar.png'

img_atualizando = imgs_root+'_powerbi_atualizando.png'
img_publicando  = imgs_root+'_powerbi_publicando.png'
img_entendi     = imgs_root+'_powerbi_entendi.png'
img_substituir  = imgs_root+'_powerbi_substituir.png'

locate_grayscale = False
locate_confidence = 0.75


def locate_image(imagepath):
    location = None
    while (location == None):
        try:
            location = pag.locateOnScreen(imagepath, 
                                          grayscale=locate_grayscale, 
                                          confidence=locate_confidence)
        except Exception as e:
            print(e)
    print(imagepath)
    return pag.center(location)

def wait_finish_image(imagepath):
    location = pag.locateOnScreen(imagepath,
                                  grayscale=locate_grayscale, 
                                  confidence=locate_confidence)
    
    print(location)

    while (location != None):
        try:
            location = pag.locateOnScreen(imagepath, 
                                          grayscale=locate_grayscale, 
                                          confidence=locate_confidence)
        except Exception as e:
            print(e)
    
    return location

def move_click(img_pos):
    if img_pos != None:
        pag.moveTo(img_pos)
        time.sleep(0.5)
        pag.leftClick()

def refresh_pbix(filepath):
    full_filepath = os.path.abspath(filepath)
    process = subprocess.Popen([powerbi_exe, full_filepath])

    _refresh = locate_image(img_atualizar)
    move_click(_refresh)
    time.sleep(5)
    wait_finish_image(img_atualizando)
    time.sleep(1)

    _post = locate_image(img_publicar)
    move_click(_post)
    time.sleep(1)

    _save = locate_image(img_salvar)
    move_click(_save)
    time.sleep(1)

    _workspace = locate_image(img_workspace)
    move_click(_workspace)
    time.sleep(1)

    _select = locate_image(img_selecionar)
    move_click(_select)
    time.sleep(1)

    _replace = locate_image(img_substituir)
    move_click(_replace)
    time.sleep(1)

    _understood = locate_image(img_entendi)
    move_click(_understood)
    time.sleep(1)

    process.kill()

    time.sleep(5)

print('PowerBi Autobot by Dragonyk')
ulog.write_info('PowerBi Automation bot started.')

def execute_scripts():
    ulog.write_info('Started running the files.')
    for filepath in settings.file_list:
        refresh_pbix(filepath)

if settings.cycle_timer == True:
    if settings.timer == 'min':
        schedule.every(settings.each_time).minutes.do(execute_scripts)
    else:
        schedule.every(settings.each_time).hours.do(execute_scripts)
else:
    schedule.every().day.at(settings.specified_time).do(execute_scripts)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
