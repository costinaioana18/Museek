import pygame as pg
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.COLOR_INACTIVE = pg.Color((177, 114, 97))
        self.COLOR_ACTIVE = pg.Color((255, 162, 193))
        self.FONT = pg.font.Font(None, 32)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.default_text= text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.protected_text=''
        self.active = False

    def handle_event(self, event,protected=False):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
                if self.default_text==self.text:
                    self.text=''
                    self.protected_text=''
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    #print(self.text)
                    return self.text
                    self.text = ''
                    self.protected_text=''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.protected_text = self.protected_text[:-1]
                else:
                    self.text += event.unicode
                    self.protected_text+='*'
                # Re-render the text.
                if protected:
                    self.txt_surface = self.FONT.render(self.protected_text, True, self.color)
                else:
                    self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(400, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+155, self.rect.y+16))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
