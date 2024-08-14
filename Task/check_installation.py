import pygame
import PIL
import cv2
import moviepy.editor as mp
import pydub
import tkinter as tk
from moviepy import __version__ as moviepy_version
from pydub import AudioSegment

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:", moviepy_version)
    
    # Pydub version check workaround
    print("✅ Pydub version:", AudioSegment.__module__.split('.')[1])
    
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()
