import pygame


def main():
    # As definicoes dos obejtos(variaveis)
    pygame.init()
    tela = pygame.display.set_mode([600, 450])
    pygame.display.set_caption("Jogo Iniciante")
    relogio = pygame.time.Clock()
    cor_branca = (255, 255, 255)
    cor_azul = (108, 194, 236)
    cor_verde = (152, 231, 114)
    cor_vermelha = (237, 28, 36)
    cor_amarela = (219, 235, 18)
    superficie = pygame.Surface((600, 450))
    superficie.fill(cor_azul)

    ret = pygame.Rect(10, 10, 30, 30)
    ret2 = pygame.Rect(10, 40, 555, 7)
    ret3 = pygame.Rect(10, 90, 350, 7)
    ret4 = pygame.Rect(410, 90, 225, 7)
    sair = False

    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 30)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

    audio_explosao = pygame.mixer.Sound('C:\\Users\\jdrasini\\Desktop\\Arquivos Pygame\\Fontes\\explodir.ogg')

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(10, 10)
                main()

        relogio.tick(50)
        tela.fill(cor_branca)
        tela.blit(superficie, [0, 0])

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.height / 2
        if ret.colliderect(ret2) or ret.colliderect(ret3):
            text = fonte_perdeu.render('VOCÊ PERDEU!!', 1, (255, 255, 255))
            tela.blit(text, (210, 210))
            pygame.mouse.set_pos(10, 10)
            audio_explosao.play()
            audio_explosao.set_volume(00.1)
            (ret.left, ret.top) = (xant, yant)

        if ret.top > 400:
            text = fonte_ganhou.render('VOCÊ GANHOU!!', 1, (255, 255, 255))
            tela.blit(text, (210, 210))
            text = fonte_perdeu.render('Clique para recomeçar!!', 1, cor_vermelha)
            tela.blit(text, (150, 250))

        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_amarela, ret2)
        pygame.draw.rect(tela, cor_amarela, ret3)
        pygame.draw.rect(tela, cor_amarela, ret4)
        pygame.display.update()
    pygame.quit()


main()
