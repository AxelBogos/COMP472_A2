import PySimpleGUI as sg
import cv2
import numpy as np
import os

def main():

    imgs={}
    path=r'UI_images'
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            file_in = subdir + os.sep + filename
            if file_in.endswith('.jpg'):
                imgs[int(filename[0])]=cv2.imread(file_in)
   

    sg.theme("LightGreen")


    # Define the window layout
    layout = [
        [sg.Text("OpenCV Demo", size=(60, 1), justification="center")],
        [sg.Image(filename="", key="-IMAGE-")],[sg.Button("OK")]]
    window = sg.Window("OpenCV Integration", layout, location=(800, 400))

    
    path=r'GBF_H1_3x3\Solution_files\0_GBF_H1_3x3_solution.txt'
    puzzles=read_puzzle_solution(path)
    i=0
    change=True
    while True:
        event, values = window.read(timeout=20)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "OK":
            change=True
        if change:
            if len(puzzles)>i:
                frame=create_img(puzzles[i],imgs,(3,3))
                change=False
                i+=1
        
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["-IMAGE-"].update(data=imgbytes)

    window.close()
def create_img(puzzle,images,dims):
    h,w  = images[1].shape[:2]
    H ,W =( h*3+8, w*3+8)
    #create empty matrix
    vis = np.zeros(( H, W,3), np.uint8)

    #combine 2 images
    for row in range(dims[0]):
        for col in range(dims[1]):
            id=row*3+col
            if puzzle[id]==0:
                continue
            
            vis[col*h+2*col+2:(col+1)*h+2*col+2,row*h+2*row+2:(row+1)*h+2*row+2,:3] = images[puzzle[id]]
    return vis
def read_puzzle_solution(path):
    puzzles=[]
    with open(path,'r') as f:
        for line in f:
            puzzle=line.split(' ')[2:]
            if len(puzzle)<3:
                break
            puzzle=[int(i) for i in puzzle ]
            puzzles.append(puzzle)

    return puzzles
main()