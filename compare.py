import pyautogui as pag

def test(function_name):
    pag.write(function_name, interval=0.05)
    #pag.press('enter')

    try:
        pag.locateOnScreen("screenshots/"+function_name+".png")
        print(function_name+": Image match")
        #pag.screenshot("screenshots/"+function_name+".png", region=(510, 220, 770, 530))
    except:
        print(function_name+": Image not found")

pag.PAUSE=0.01

FUNCTION_BOX = (185, 270)

DELETE_MARKER = (470, 260)

functions = ['x',
             '10x',
             '-10x',
             '10x+5',
             '10x-5',
             '-10x+5',
             '-10x-5',
             'x^2',
             '5+x^2',
             '5-x^2',
             '-5+x^2',
             '-x^2',
             '10+5x+x^2',
             'sinx',
             'cosx',
             '5sinx',
             '5cosx',
             '-5sinx',
             '-5cosx',
             'sinx+cosx',
             '5sinx+5cosx',
             'tanx',
             'tan(x+10)',
             'e^x']

pag.moveTo(FUNCTION_BOX[0], FUNCTION_BOX[1], duration=0.05)
pag.click()

for function in functions:
    test(function)
    for i in range(len(function)):
        pag.press('backspace')
