"""

Inteligência Artificial aplicada à Visão Computacional
Capítulo 4: Visão Computacional aplicada ao reconhecimento facial em imagens

Todos os direitos reservados à Facti, 2024

www.qualifacti.com.br

-----------------------------------------------------------------------------------------------------------------------

ETAPA CONCEITUALIZAR

Recado importante
Olá,
Como parte do capítulo de reconhecimento facial, gostaríamos de ressaltar a importância de realizar as atividades de
implementação fornecidas. Estas atividades são cuidadosamente desenhadas para reforçar o conteúdo apresentado. Lembre-se,
a implementação é uma habilidade que se aprimora com a prática. Ao aplicar os conceitos aprendidos, especialmente por meio
da escrita e execução de códigos, você ganhará uma compreensão mais profunda e prática dos modelos. Encorajamos todos a
dedicar tempo a essas atividades. Ao fazer isso, você não apenas reforçará o que foi ensinado, mas também desenvolverá
as habilidades essenciais de resolução de problemas e depuração de código.

Lembrem-se: não basta apenas aprender, é preciso codificar! O caminho para dominar os modelos começa com a experiência prática.

Atenciosamente,
Júlio e Marcelo

-----------------------------------------------------------------------------------------------------------------------

Atividade de experimentação 59
Escreva um programa, em Python, que utilize classificadores haarcascade para detectar relógios em imagens.


ORIENTAÇÕES:

#1 - Antes de iniciar e executar o código, abra a aba Terminal, localizada na parte inferior do PyCharm e execute, na
sequência, os seguintes comandos para instalar os recursos da biblioteca do OpenCV:

pip install opencv-python

pip install opencv-contrib-python

#2 - Lembre-se de trazer a pasta fotos disponibilizada para dentro do PyCharm. Você pode arrastar a pasta para dentro do
projeto, no menu lateral esquerdo.

#3 - Lembre-se de trazer a pasta cascades disponibilizada para dentro do PyCharm. Você pode arrastar a pasta para dentro
do projeto, no menu lateral esquerdo.

-----------------------------------------------------------------------------------------------------------------------
"""

import cv2

classificadorRelogio = cv2.CascadeClassifier('cascades\\relogios.xml') # utiliza um haarcascade treinado para detectar relógios

#imagem = cv2.imread('outros\\relogios1.jpg')  # 1.07 - atente-se para o caminho e extensão da imagem
#imagem = cv2.imread('outros\\relogios2.jpg') # 1.068; 6
#imagem = cv2.imread('outros\\relogios3.jpg') # 1.068
#imagem = cv2.imread('outros\\relogios4.jpg') # 1.05
imagem = cv2.imread('outros\\relogios5.jpg') # 1.05
#imagem = cv2.imread('outros\\relogios6.jpg') # 1.05

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # transforma a imagem colorida em escala de cinza

detectado = classificadorRelogio.detectMultiScale(imagemCinza, scaleFactor=1.05, minNeighbors=6)
# comando para detectar relógios na imagem em escala de cinza. Você pode alterar os parâmetros scaleFactor e minNeighbors
# para melhorar a precisão da detecção (alguns estão indicados como os números na frente da imagem acima)

for (x, y, l, a) in detectado:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2) # comando para desenhar um retângulo na presença de relógio

cv2.imshow(str(len(detectado)) + ' relogio(s) encontrado(s)', imagem) # mostrará a quantidade de relógios no título da janela
cv2.waitKey() # comando que aguarda o fechamento das janelas com as imagens