import pygame
import os

pygame. init()

# Caminho das imagens
BASE = os.path.dirname(os.path.abspath( __ file_))
IMG = os.path.join(os.path.dirname(BASE), "imagens")

def carregar_imagem(nome, largura, altura):
    caminho = os.path.join(IMG, nome)
    imagem = pygame. image. load (caminho). convert_alpha()
    return pygame. transform. scale(imagem, (largura, altura))

# Tela
LARGURA = 720
ALTURA = 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Game 08 - Jogo Completo Ajustado")

rel = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 36)

# Tamanhos ajustados
TAM_PERSONAGEM = 120
LARG_OBSTACULO = 90
ALT_OBSTACULO = 100
TAM_OBJETIVO = 120

# Imagens
fundo = carregar_imagem("fundo.png", 720, 720)
personagem = carregar_imagem("personagem.png", TAM_PERSONAGEM, TAM_PERSONAGEM)
obstaculo_img = carregar_imagem("obstaculo1.png", LARG_OBSTACULO, ALT_OBSTACULO)
objetivo_img = carregar_imagem("objetivo.png", TAM_OBJETIVO, TAM_OBJETIVO)

# Chão visual do cenário
chao = 600
# Personagem
x = 70
y = chao - TAM_PERSONAGEM
vel = 5

# Pulo
pulando = False
velocidade_pulo = 0
forca_pulo = -25
gravidade = 0.9

# Obstáculo e objetivo
obstaculo = pygame.Rect(
    360,
    chao - ALT_OBSTACULO,
    LARG_OBSTACULO,
    ALT_OBSTACULO
)

objetivo = pygame.Rect(

590,
chao - TAM_OBJETIVO,
TAM_OBJETIVO,
TAM_OBJETIVO
)

mensagem =""
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

# Movimento para direita
if teclas[pygame.K_RIGHT]:
    x += vel

# Movimento para esquerda
if teclas[pygame.K_LEFT]:
    x -= vel

# Pulo
    if teclas[pygame.K_SPACE] and not pulando:
pulando = True
velocidade_pulo = forca_pulo