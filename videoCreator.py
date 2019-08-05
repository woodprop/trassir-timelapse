import os
from datetime import datetime

date = datetime.strftime(datetime.now(), "%d-%m-%Y")

def move_and_rename(source, destination, label):
    flist = os.listdir(source)
    i = 1
    for file in flist:
        num = str(i)
        while len(num) < 7:
            num = '0' + num

        if os.path.isdir(source + file):
            continue
        if file.startswith(label):
            os.rename(source + file, destination + num + '.jpg')

            i += 1


def create_video(source, destination):
    # Путь к FFMPEG
    script_path = 'C:/FFMPEG/bin/'

    img_template = source + '%07d.jpg'

    output_file = destination + date + '.mp4'
    script_cmd = '-framerate 10 -i ' + img_template + ' -c:v libx264 -r 30 -pix_fmt yuv420p ' + output_file
    command = script_path + 'ffmpeg ' + script_cmd

    os.system(command)

    # -------------- Удаляем исходные файлы
    for f in os.listdir(source):
        os.remove(source + f)
    # -------------------------------------



move_and_rename('D:/Screenshots/', 'D:/Screenshots/BUTAFOR/', 'Бутафорский')
move_and_rename('D:/Screenshots/', 'D:/Screenshots/PENOREZ/', 'Пенорезка')
move_and_rename('D:/Screenshots/', 'D:/Screenshots/SVAR/', 'Сварной')
move_and_rename('D:/Screenshots/', 'D:/Screenshots/CENTER/', 'Центр')

print('Files was renamed')

create_video('D:/Screenshots/SVAR/', 'D:/VIDEO_TimeLapse/SVAR/')
create_video('D:/Screenshots/BUTAFOR/', 'D:/VIDEO_TimeLapse/BUTAFOR/')
create_video('D:/Screenshots/CENTER/', 'D:/VIDEO_TimeLapse/CENTER/')
create_video('D:/Screenshots/PENOREZ/', 'D:/VIDEO_TimeLapse/PENOREZ/')

print('Video file created! Press Enter to exit')
#input()
