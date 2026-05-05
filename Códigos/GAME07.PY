import pygane
import os

pygane.init()

#-Caminho das imagens
BASE - os.path.dirname(os.path.abspath(__ file __))
IMG - os.path. join(os.path. dirnane (BASE), "imagens")

def carregar_imagen(nome, largura, altura):
    caminho - os.path.join(IMG, nome)
    imagen - pygame.image.load(caminho).convert_alpha()
    return pygane. transforn.scale(imnagem, (largura, altura))

# Tela
LARGURA - 728
ALTURA - 720
tela - pygame.display.set_node( (LARGURA, ALTURA))
pygame.display.set_caption("Game 07 - Pulo")

rel - pygane.tine.Clock()

# Imagens
personagem - carregar_imagen("personagem.png", 85, 85)
obstaculo - carregar_imagen("obstaculo1.png", 80, 80)
objetivo - carregar_imagem("objetivo.png", 75, 75)

# Chão
chao - 700

# Personagen
x = 88
y = chao - 85
vel = 5

# Pulo
pulando - False
velocidade_pulo = 0
forca_pulo = -20
gravidade - 0.9

# Objetos
obstaculo_x = 390
obstaculo_y = chao - 88

objetivo_x = 620
abjetivo_y = chao - 75

rodando - True
while rodando:
    for evento in pygame.event.get():
        if evento. type -- pygame.QUIT:
            rodando - False

teclas = pygame.key.get_pressed()

if teclas[pygane.K_RIGHT]:
    x += vel

if teclas[pygane.K_LEFT]:
    x -- vel

if teclas[pygane.K_SPACE] and not pulando:
pulando - True
velocidade_pulo - forca_pulo

if pulando:

y +- velocidade_pulo
velacidade_pulo +- gravidade

if y >- chao - 85:
    y = chao - 85
    pulando - False

tela.fill((135, 206, 235))

tela.blit(personagem, (x, y))
tela.blit(obstaculo, (obstaculo_x, obstaculo_y))
tela.blit(objetivo, (objetivo_x, objetivo_y))

pygane.display.flip()