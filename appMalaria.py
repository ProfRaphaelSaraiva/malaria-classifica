import streamlit as st
import gdown
import tensorflow as tf
import io
import PIL import image
import numpy as np

@st.cache_resource
def carrega_modelo():
  url=

gdown.download(url, 'modelo_quantizado16bits.tflite')
interpreter = tf.lite.Interpreter(model_path='modelo_quantizado16bits.tflite')
interpreter.allocate_tensors()

return interpreter

def carrega_imagem():
  upload_file = st.file_uploader('Arraste e solte a imagem aqui ou clique para selecionar uma', type=['png,'jpg','jpeg'])

  if upload_file is not Nome:
    image_data = uploaded_file.read()
    imagem = Image.open(io.BytestIO(image_data))

    st.image(image)
    st.success('Imagem foi carregada com sucesso')

    image = np.array(image, dtype= np.float32)
    image = image/255.0
    image = np.expand_dims(image, axis=0)

    return  image

def main():

  st.set_page_config(
    page_title="Classifica  Malária - Rapha.Tech",
    page_icon="🩸",
    
  )

  st.write("#Classifica Malária ! 🩸 - Rapha.Tech")
  #carregar o modelo
  interpreter = carrega_modelo()

  #carregar a imagem
image = carrega_imagem()
  #classifica


  if __name__== "__main__":
    main()
