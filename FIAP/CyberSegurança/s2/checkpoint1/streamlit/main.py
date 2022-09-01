from distutils.fancy_getopt import fancy_getopt
import streamlit as st
from PIL import Image
from captcha.image import ImageCaptcha 
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import cvlib as cv
import cv2
import sys
from cvlib.object_detection import YOLO




def main ():
    if 'cap' not in st.session_state:
        st.session_state.cap = 0

    if 'cap_img' not in st.session_state:
        st.session_state.cap_img, st.session_state.cap_txt = captcha()


    

    st.title("S443 Investimentos")

    if st.session_state.cap == 0:
        st.subheader("Verification step (1/2)")


        st.image(st.session_state.cap_img)

        
        guess = st.text_input("Favor resolver Captcha para prosseguir: ", value="", max_chars=6, help="Digite os numeros acima")

        col1,col2,e1,e2,e3,e4,e5,e6 = st.columns(8)

        with col1:
            if st.button("Change"):
                capReset()

        with col2:
            sub = st.button("Submit")

        if sub:
            if guess == st.session_state.cap_txt:
                st.success("Success!")
                time.sleep(2)
                st.session_state.cap = 1
                st.experimental_rerun()
            else:
                st.error("Failed!")
                capReset(1)
                

    if st.session_state.cap == 1:
        st.subheader("Verification step (2/2)")

    
        image = st.camera_input("Tire uma foto sua, segurando uma caneta")

        if image is not None:

            bytes_data = image.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)


            faces, confidences = cv.detect_face(cv2_img)
            if confidences == []:
                confidences.append(0)   
            st.text(confidences)

            st.text(facematch(faces,confidences))
            
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(cv2_img, (x, y), (w, h), (255, 0, 0), 2)


            # st.image(cv2_img)


def capReset(i:int=0):
    time.sleep(i)
    del st.session_state.cap_img
    del st.session_state.cap_txt
    st.experimental_rerun()

def facematch(faces:list,confidences:float) -> bool:
    if confidences[0] > 0.5:
        if faces != None:
            return True   
    return False


def captcha():
    number = ['0','1','2','3','4','5','6','7','8','9']
    MAX_CAPTCHA = 6
    WIDTH=1000
    HEIGHT=280
    

    image = ImageCaptcha(height=HEIGHT,width=WIDTH,font_sizes=[200])

    captcha_text = []
    for i in range(MAX_CAPTCHA):
        c = random.choice(number)
        captcha_text.append(c)
    captcha_text = ''.join(captcha_text)

    captcha = image.generate(captcha_text)
    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)

    return captcha_image, captcha_text

if __name__ == '__main__':
    main()