from unittest import result
import streamlit as st
from PIL import Image
from captcha.image import ImageCaptcha 
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import cvlib as cv
import cv2
from cvlib.object_detection import draw_bbox




def main ():
    if 'cap' not in st.session_state:
        st.session_state.cap = 0

    if 'cap_img' not in st.session_state:
        st.session_state.cap_img, st.session_state.cap_txt = captcha()

    if 'hasimg' not in st.session_state:
        st.session_state.hasimg = 0

    if 'apple' not in st.session_state:
        st.session_state.apple = 0


    

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

    
        image = st.camera_input("Tire uma foto sua, segurando uma maça")

        if st.session_state.apple == 0:
            if st.button('Não tenho uma maça!'):
                st.info('Vá comprar uma e ser saudável!')
                st.session_state.apple = 1
        if image is not None:

            cv2_img = cv2Image(image)
           
            results, st.session_state.output_image = detectObjects(cv2_img)

            st.session_state.hasimg = 1

            if appleMatch(results):
                if personMatch(results):
                    st.success("Success!")
                    time.sleep(2)
                    st.session_state.cap = 2
                    st.experimental_rerun()
                else:
                    st.warning('Pessoa não detectada!')
            else:
                st.warning('Maça não detectada!')

    if st.session_state.cap == 2:
        if st.session_state.hasimg == 1:
            if st.checkbox("See photo result"):
                    st.image(st.session_state.output_image)
        
        if st.button("Try app again "):
            st.session_state.cap = 0
            st.experimental_rerun()

        st.balloons()
        
        gifList = [
            'https://media.giphy.com/media/vLvoizmG4esTveDkGW/giphy.gif',
            'https://media.giphy.com/media/pzrsklEOuucIWSADBA/giphy.gif',
            'https://media.giphy.com/media/3b4JiHClZdMlT8OK7I/giphy.gif',
            'https://media.giphy.com/media/SXZj5WFLxiSdy/giphy.gif'

        ]
        
        for i in gifList:
            st.markdown(f"![Alt Text]({i})")

        
        
def detectObjects(image):
    bbox, label, conf = cv.detect_common_objects(image, confidence=0.5, nms_thresh=0.3, model='yolov3')
    output_image = draw_bbox(image, bbox, label, conf)
        
    results={}
    for i in range(len(label)):
        results[label[i]]=conf[i]   
    return  results, output_image

def cv2Image(image):
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    return cv2_img


def appleMatch(results:dict)->bool:
    for i in results.keys():
        if i == "apple":
            if results[i] > 0.8:
                return True
    return False

def personMatch(results:dict)->bool:
    for i in results.keys():
        if i == "person":
            if results[i] > 0.8:
                return True
    return False

def capReset(i:int=0):
    time.sleep(i)
    del st.session_state.cap_img
    del st.session_state.cap_txt
    st.experimental_rerun()



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