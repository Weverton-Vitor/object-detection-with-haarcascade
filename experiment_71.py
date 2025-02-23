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
ORIENTAÇÕES:

#1 - Antes de iniciar e executar o código, abra a aba Terminal, localizada na parte inferior do PyCharm e execute, na
sequência, os seguintes comandos para instalar os recursos da biblioteca do OpenCV:

pip install opencv-python

pip install opencv-contrib-python

#2 - Para executar o código:
    * Clique em Run;
    * Visualize o rastreamento;
    * Pressione ESC para encerrar a qualquer momento.

-----------------------------------------------------------------------------------------------------------------------

Atividade de experimentação 71

"""

# Importando bibliotecas
import cv2
import numpy as np

# Carrega um vídeo para análise do arquivo especificado
cap = cv2.VideoCapture("./tracking_material/videos/walking.avi")

# Configura os parâmetros para o detector de cantos Shi-Tomasi
parameters_shitomasi = dict(maxCorners=100,
                            qualityLevel=0.3,
                            minDistance=7)
# Configura os parâmetros para o algoritmo de Lucas-Kanade para o fluxo óptico
parameters_lucas_kanade = dict(winSize=(15, 15),
                               maxLevel=2,
                               criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
# Gera cores aleatórias para representar os pontos de interesse
colors = np.random.randint(0, 255, (100, 3))

# Lê o primeiro frame do vídeo
ret, frame = cap.read()

# Converte o primeiro frame para escala de cinza
frame_gray_init = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detecta os pontos de interesse no primeiro frame usando o detector de cantos Shi-Tomasi
edges = cv2.goodFeaturesToTrack(frame_gray_init, mask=None, **parameters_shitomasi)

# Cria uma máscara com as mesmas dimensões e tipo do frame para desenhar o trajeto dos pontos
mask = np.zeros_like(frame)

# Loop para processar cada frame do vídeo
while True:
    ret, frame = cap.read() # Lê o frame atual do vídeo
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converte o frame atual para escala de cinza
    # Calcula o fluxo óptico de Lucas-Kanade para os pontos de interesse detectados anteriormente
    new_edges, status, errors = cv2.calcOpticalFlowPyrLK(frame_gray_init,
                                                         frame_gray,
                                                         edges,
                                                         None,
                                                         **parameters_lucas_kanade)
    # Filtra os novos pontos de interesse com base no status
    news = new_edges[status == 1]
    olds = edges[status == 1]

    # Itera sobre os pontos antigos e novos para atualizar o trajeto
    for i, (new, old) in enumerate(zip(news, olds)):
        a, b = new.ravel().astype(int)
        c, d = old.ravel().astype(int)

        # Desenha uma linha na máscara para indicar o trajeto do ponto
        mask = cv2.line(mask, (a, b), (c, d), colors[i].tolist(), 2)
        # Desenha um círculo no frame para marcar o ponto de interesse
        frame = cv2.circle(frame, (a, b), 5, colors[i].tolist(), -1)

    img = cv2.add(frame, mask) # Combina o frame e a máscara

    # Exibe o resultado do fluxo óptico esparsa em uma janela
    cv2.imshow('Sparce Optical flow', img)
    if cv2.waitKey(1) == 13:     # Aguarda por uma tecla ser pressionada; se a tecla 'Enter' for pressionada, interrompe o loop
        break

    # Atualiza o frame inicial para o frame atual para a próxima iteração
    frame_gray_init = frame_gray.copy()
    # Atualiza os pontos de interesse para os novos pontos
    edges = news.reshape(-1, 1, 2)

# Fecha todas as janelas abertas e libera a captura de vídeo
cv2.destroyAllWindows()
cap.release()