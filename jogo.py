import pygame


def main():
    # As definicoes dos obejtos(variaveis)
    pygame.init()
    tela = pygame.display.set_mode([600, 450])
    pygame.display.set_caption("Jogo Iniciante")
    relogio = pygame.time.Clock()
    cor_branca = (255, 255, 255)
    cor_azul = (108, 194, 236)
    cor_preta = (7, 7, 7)
    cor_verde = (152, 231, 114)
    cor_vermelha = (237, 28, 36)
    cor_amarela = (219, 235, 18)
    superficie = pygame.Surface((600, 450))
    superficie.fill(cor_preta)

    ret = pygame.Rect(10, 10, 30, 30)
    ret2 = pygame.Rect(0, 70, 540, 7)
    ret3 = pygame.Rect(0, 120, 350, 7)
    ret4 = pygame.Rect(405, 120, 195, 7)
    ret5 = pygame.Rect(60, 170, 555, 7)
    ret6 = pygame.Rect(0, 220, 400, 7)
    ret7 = pygame.Rect(455, 220, 145, 7)
    ret8 = pygame.Rect(60, 270, 555, 7)
    ret9 = pygame.Rect(0, 320, 540, 7)
    sair = False

    pygame.font.init()

    font_padrao = pygame.font.get_default_font()
    fonte_perdeu = pygame.font.SysFont(font_padrao, 30)
    fonte_ganhou = pygame.font.SysFont(font_padrao, 30)

    audio_explosao = pygame.mixer.Sound('C:\\Users\\Denis\\Desktop\\pygame\\Arquivos Pygame\\Fontes\\explodir.ogg')

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
        if ret.colliderect(ret2) or ret.colliderect(ret3) or ret.colliderect(ret4) \
                or ret.colliderect(ret5) or ret.colliderect(ret6) or ret.colliderect(ret7) \
                or ret.colliderect(ret8) or ret.colliderect(ret9):
            text = fonte_perdeu.render('VOCÊ PERDEU!!', 1, (255, 255, 255))
            tela.blit(text, (210, 210))
            pygame.mouse.set_pos(10, 10)
            audio_explosao.play()
            audio_explosao.set_volume(00.1)
            (ret.left, ret.top) = (xant, yant)

        if ret.top > 330:
            text = fonte_ganhou.render('VOCÊ GANHOU!!', 3, (255, 255, 255))
            tela.blit(text, (240, 200))
            text = fonte_perdeu.render('Clique para recomeçar!!', 1, cor_vermelha)
            tela.blit(text, (200, 250))
            ret2.left, ret3.left, ret4.left, ret5.left, ret6.left = 602, 602, 602, 602, 602
            ret7.left, ret8.left, ret9.left = 602, 602, 602

        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_verde, ret2)
        pygame.draw.rect(tela, cor_verde, ret3)
        pygame.draw.rect(tela, cor_verde, ret4)
        pygame.draw.rect(tela, cor_verde, ret5)
        pygame.draw.rect(tela, cor_verde, ret7)
        pygame.draw.rect(tela, cor_verde, ret6)
        pygame.draw.rect(tela, cor_verde, ret8)
        pygame.draw.rect(tela, cor_verde, ret9)
        pygame.display.update()
    pygame.quit()


main()
