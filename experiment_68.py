"""
Inteligência Artificial aplicada à Visão Computacional
Capítulo 7: Visão Computacional aplicada ao rastreamento de objetos

Todos os direitos reservados à Facti, 2024

www.qualifacti.com.br

É importante esclarecer que estas atividades não compõem a avaliação e não haverá correção formal por parte dos instrutores;
o objetivo é a autoaprendizagem e prática.

-----------------------------------------------------------------------------------------------------------------------
ETAPA CONCEITUALIZAR

Recado importante
Olá,
Como parte do capítulo de rastreamento de objetos, gostaríamos de ressaltar a importância de realizar as atividades de
implementação fornecidas. Estas atividades são cuidadosamente desenhadas para reforçar o conteúdo apresentado. Lembre-se,
a implementação é uma habilidade que se aprimora com a prática. Ao aplicar os conceitos aprendidos, especialmente por meio
da escrita e execução de códigos, você ganhará uma compreensão mais profunda e prática dos modelos. Encorajamos todos a
dedicar tempo a essas atividades. Ao fazer isso, você não apenas reforçará o que foi ensinado, mas também desenvolverá
as habilidades essenciais de resolução de problemas e depuração de código.

Lembrem-se: não basta apenas aprender, é preciso codificar! O caminho para dominar os modelos começa com a experiência prática.

Atenciosamente,
Júlio e Marcelo

-----------------------------------------------------------------------------------------------------------------------

Atividade de experimentação 68


ORIENTAÇÕES:

#1 - Antes de iniciar e executar o código, abra a aba Terminal, localizada na parte inferior do PyCharm e execute, na
sequência, os seguintes comandos para instalar os recursos da biblioteca do OpenCV:

pip install opencv-python

pip install opencv-contrib-python

#2 - Lembre-se de trazer a pasta videos disponibilizada para dentro do PyCharm. Você pode arrastar a pasta para dentro do
projeto, no menu lateral esquerdo.

#3 - Para executar o código:
    * Clique em Run;
    * Ao iniciar a janela do vídeo, selecione com o mouse criando um retângulo no objeto de interesse para o rastreamento;
    * Aperte Enter para executar.

-----------------------------------------------------------------------------------------------------------------------

"""

# Importando bibliotecas
import cv2
import sys
from random import randint

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

# Declarando os tipos de algoritmos de rastreamento
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
# Escolhendo o algoritmo 0: BOOSTING, 1: MIL, 2: KCF, 3: TLD, 4: MEDIANFLOW, 5: MOSSE, 6: CSRT
tracker_type = tracker_types[0] # Indique o classificador
print(tracker_type)

if int(minor_ver) < 3:
    tracker = tracker_type
else:
# Verificando qual o algoritmo escolhido
   if tracker_type == 'BOOSTING':
       tracker = cv2.legacy.TrackerBoosting_create()
   if tracker_type == 'MIL':
       tracker = cv2.legacy.TrackerMIL_create()
   if tracker_type == 'KCF':
       tracker = cv2.legacy.TrackerKCF_create()
   if tracker_type == 'TLD':
       tracker = cv2.legacy.TrackerTLD_create()
   if tracker_type == 'MEDIANFLOW':
       tracker = cv2.legacy.TrackerMedianFlow_create()
   if tracker_type == 'MOSSE':
       tracker = cv2.legacy.TrackerMOSSE_create()
   if tracker_type == 'CSRT':
       tracker = cv2.legacy.TrackerCSRT_create()

video = cv2.VideoCapture('./tracking_material/videos/race.mp4') # Localize o caminho do vídeo para análise, na pasta videos.
if not video.isOpened():
    print('Não foi possível carregar o vídeo')
    sys.exit()

ok, frame = video.read() # Habilita a leitura do vídeo
if not ok:
    print('Não foi possível ler o arquivo de vídeo')
    sys.exit()

bbox = cv2.selectROI(frame, False) # Cria o retângulo no objeto de interesse.

ok = tracker.init(frame, bbox) # Habilita o rastreamento do objeto.

colors = (randint(0, 255), randint(0, 255), randint(0, 255)) # Seleciona uma cor aleatória para o retângulo.

# Comandos para rastrear o objeto enquando vídeo estiver ativo.
while True:
    ok, frame = video.read()
    if not ok:
        break

    timer = cv2.getTickCount()
    ok, bbox = tracker.update(frame)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), colors, 2, 1)
    else:
        cv2.putText(frame, 'Falha no rastreamento', (100, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)

    cv2.putText(frame, tracker_type + ' Tracker', (100, 20),
                cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)

    cv2.putText(frame, 'FPS: ' + str(int(fps)), (100, 50),
                cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break