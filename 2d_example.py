from setup import *
from rectangle import Rectangle
#the rectangles position in the middle
def statue(location=(0,height/2,0)):
    v = location[2]+10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_sprite_sheet.image_at((16*44,16*18,32,64)),True)
    statue.z_position = location[2]
    statue.set_size((50,100))
    return statue

def house(location=(0,height/2,0)):
    v = location[2]-10
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_sprite_sheet.image_at((16*32,16*18,48,64)),True)
    statue.z_position = location[2]
    statue.set_size((75,100))
    return statue

pressed =False
my_sprite_sheet = SpriteSheet("16_p_tileset.png")
my_walks = SpriteSheet("Basic Charakter Spritesheet.png")
p = Rectangle((width/5,height/15),(width/2,height/2),(250,0,0),"Basic Charakter Spritesheet.png")
p.set_image(my_walks.image_at((0,50,50,50)),True)
p.set_size((100,100))
p.z_position = 0
my_sprites = {}
g1 = statue((width/2,height/2,200))
my_sprites["fg"] = g1
my_sprites["p"] = p
#you have to summand y+(z+z:4)*-1
printing_row = []

def make_row(key):
    c = 0
    d = True
    while d:
        if my_sprites[key].z_position >= my_sprites[printing_row[c]].z_position:
            printing_row.insert(c-1,key)
            d = False
        else:
            if c <= len(printing_row)-2:
                c += 1
            else:
                d = False

    if my_sprites[key].z_position <= my_sprites[printing_row[len(printing_row)-1]].z_position and key not in printing_row:
            printing_row.append(key)

for key in my_sprites:
    if printing_row != []:
        make_row(key)
    else:
        printing_row.append(key)
    print(f"loading{key}")
print("sorted reaady")
        
while True:
    if pressed != False:
        if pressed == "up":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0,0.2)
            my_sprites["p"].z_position += 0.2
            del printing_row[printing_row.index("p")]
            make_row("p")

        if pressed == "down":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0,-0.2)
            my_sprites["p"].z_position -= 0.2
            del printing_row[printing_row.index("p")]
            make_row("p")

        if pressed == "right":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(-0.2,0)

        if pressed == "left":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0.2,0)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pressed = "up"
            elif event.key == pygame.K_DOWN:
                pressed = "down"
            elif event.key == pygame.K_LEFT:
                pressed = "left"
            elif event.key == pygame.K_RIGHT:
                pressed = "right"

        if event.type == pygame.KEYUP:
            pressed = False

    screen.fill((250,250,250))
    for key in printing_row:
        my_sprites[key].update(screen)
    pygame.display.update()