import pyautogui as pag

def test(function_name, compare_list):
    pag.PAUSE=0.6
    pag.write(function_name, interval=0.1)
    #pag.press('enter')
    positive = []
    for inst_comp in compare_list:
        box = pag.locateOnScreen("screenshots/"+inst_comp+".png")
        if (box != None):
            positive.append(inst_comp)

    if (len(positive) == 0):
        print(function_name+" matched with nothing")
    else:
        print(function_name+" matched with: "),
        for match in positive:
            print(match),
        print("")

    pag.PAUSE=0.05
    
pag.PAUSE=0.05

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

#functions = [ 'x' ]
pag.moveTo(FUNCTION_BOX[0], FUNCTION_BOX[1], duration=0.05)
pag.click()

for function in functions:
    test(function, functions)
    for i in range(len(function)):
        pag.press('backspace')
