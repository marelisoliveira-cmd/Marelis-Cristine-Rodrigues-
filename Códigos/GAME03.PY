import pygame 
import os 

# iniciar o pygame
pygame.init()

# caminho da pasta de imagens 
BASE_DIR = os.path.join(PASTA_IMAGENS, nome)
PASTA_IMAGENS = os.path.join(os.path.dirname(BASE_DIR),
                    
                             
# Função para carregar imagem
def carregar_imagem(nome, largura, altura):
    caminho = os.path.join(PASTA_IMAGENS, nome)
    imagem = pygame.image.load(caminho).convert_alpha()
    imagem = pygame.transform.scale(imagem,(largura,altura))
    return imagem 

# criar a janela 
LARGURA = 720
ALTURA = 720
tela = pygame.display.set_mode(LARGURA,ALTURA))
pygame.display.set_caption("Game 03 - Personagem")

# Carregar personagem 
personagem = carregar_imagem("personagem.png",85,85)

# Posição inicial do personagem 
x = 80
y = 600 = mais embaixo 

# Logo principal 
rodando = true 
while rodando: 
    for evento in pygame.event.get()
        if evento.type == pygame.QUIT:
            rodando = False

    #Cor de fundo 
    tela.fill((135,206,235))

    #Desenhar personagem
    tela.blit(personagem,(x,y))

    #Atualizar tela
    pygame.display.flip()

#Encerrar
pygame.quit

