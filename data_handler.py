import numpy as np
import random
import os

def create_folders(base_path, genres, folder_tree):

    for folder in folder_tree:
        for genre in genres:
            path = base_path + folder + '/' + genre
            if not os.path.isdir(path):
                os.system(f'mkdir {path}')

def move_files(base_path, generes):
    for folder in os.scandir(base_path):
        if folder.name in generes:
            # print(folder.name)
            for file in os.listdir(folder):
                origin = base_path + folder.name + '/' + file
                if file.endswith('.wav'):
                    rnd = random.random()
                    if rnd < 0.7:
                        dest = base_path + 'train/' + folder.name
                        os.system(f'cp {origin} {dest}')
                    elif 0.7 <= rnd < 0.9:
                        dest = base_path + 'validation/' + folder.name
                        os.system(f'cp {origin} {dest}')
                    else:
                        dest = base_path + 'test/' + folder.name
                        os.system(f'cp {origin} {dest}')




