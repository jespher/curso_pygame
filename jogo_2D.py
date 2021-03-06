import pygame


def main():
    # As definicoes dos obejtos(variaveis)
    pygame.init()
    tela = pygame.display.set_mode([350, 350])
    pygame.display.set_caption("Iniciando com Pygame")
    relogio = pygame.time.Clock()
    cor_branca = (255, 255, 255)
    cor_azul = (108, 194, 236)
    cor_verde = (152, 231, 114)
    cor_vermelha = (237, 28, 36)
    cor_amarela = (219, 235, 18)
    superficie = pygame.Surface((200, 200))
    superficie.fill(cor_azul)

    superficie2 = pygame.Surface((100, 100))
    superficie2.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)
    ret2 = pygame.Rect(50, 50, 100, 50)
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
                pygame.mouse.set_pos(150, 150)

            # if event.type == pygame.MOUSEMOTION:
            #     ret = ret.move(-10, -10)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ret.move_ip(-10, 0)

                if event.key == pygame.K_RIGHT:
                    ret.move_ip(10, 0)

                if event.key == pygame.K_UP:
                    ret.move_ip(0, -10)

                if event.key == pygame.K_DOWN:
                    ret.move_ip(0, 10)

                if event.key == pygame.K_SPACE:
                    ret.move_ip(10, 10)

                if event.key == pygame.K_BACKSPACE:
                    ret.move_ip(-10, -10)

        relogio.tick(50)
        tela.fill(cor_branca)
        tela.blit(superficie, [50, 50])
        tela.blit(superficie2, [50, 50])

        (xant, yant) = (ret.left, ret.top)
        (ret.left, ret.top) = pygame.mouse.get_pos()
        ret.left -= ret.width / 2
        ret.top -= ret.height / 2
        if ret.colliderect(ret2):
            text = fonte_perdeu.render('COLIDIU!!', 1, (255, 255, 255))
            audio_explosao.play()
            audio_explosao.set_volume(00.1)
            tela.blit(text, (150, 150))
            (ret.left, ret.top) = (xant, yant)

        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_amarela, ret2)
        pygame.display.update()
    pygame.quit()


main()
