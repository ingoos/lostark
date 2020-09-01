import mouse as mo
import keyboard as key
import pyautogui as pg

#마우스 포인트저장 함수
def getMousePoint(n):
    print('F12 키를 눌러 낚시할 포인트를 저장하세요.')
    while True:
        if key.is_pressed('F12') == True:
            print('point ',n,' Catched')
            return mo.get_position()
    
def fishMovePoint(currentcursor):
    x = currentcursor[0]
    y = currentcursor[1]
    pg.move(x,y,0.1)
    pg.press('w')
    # 이미지 체크후 다시 w누르기

if __name__ == "__main__":
    pointLoop = 3
    n = 1
    currentcursor = getMousePoint(n) # 마우스 위치 저장
    fishMovePoint(currentcursor) # 마우스 위치 이동