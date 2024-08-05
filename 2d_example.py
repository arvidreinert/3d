from setup import *
from rectangle import Rectangle
#the rectangles position in the middle
my_sprite_sheet = SpriteSheet("16_p_tileset.png")
my_walks = SpriteSheet("Basic Charakter Spritesheet.png")
p = Rectangle((width/5,height/15),(width/2,height/2),(250,0,0),"Basic Charakter Spritesheet.png")
p.set_image(my_walks.image_at((0,50,50,50)),True)
p.set_size((100,100))
p.z_position = 0
c = Rectangle((width/5,height/15),(width/2,height/2),(250,0,0),"16_p_tileset.png")
c.set_image(my_sprite_sheet.image_at((16,16,16,16)),True)
c.set_size((200,200))
c.z_position = 1
my_sprites = {"p":p,"c":c}
printing_row = []

for key in my_sprites:
    c = 0
    d = True
    if printing_row != []:
        while d:
            if my_sprites[key].z_position <= my_sprites[printing_row[c]].z_position:
                printing_row.insert(c,key)
                d = False
            else:
                if c <= len(printing_row)-2:
                    c += 1
                else:
                    d = False

        if my_sprites[key].z_position >= my_sprites[printing_row[len(printing_row)-1]].z_position and key not in printing_row:
                printing_row.append(key)
    else:
        printing_row.append(key)
             
printing_row.reverse()
print(printing_row)        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((250,250,250))
    for key in printing_row:
        my_sprites[key].update(screen)
    pygame.display.update()