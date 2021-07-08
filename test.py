import librosa
import librosa.display
import os
import matplotlib.pyplot as plt
import data_handler as dh

audio_path = '../../Datasets/genres/'

genres = [d.name for d in os.scandir(audio_path) if os.path.isdir(d)]

# file = audio_path + '/' + genres[0] + '/' + f'{genres[0]}.00000.wav'

# x , sr = librosa.load(file)

# print(x[:5], sr)

# X = librosa.stft(x)
# Xdb = librosa.amplitude_to_db(abs(X))

# print(Xdb.shape)

# plt.figure(figsize=(14, 5))
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
# plt.colorbar()

# plt.show()
dh.create_folders(audio_path, genres, ['train', 'validation', 'test'])
# dh.move_files(audio_path, genres)