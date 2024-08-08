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

def tree(location=(0,height/2,0)):
    v = location[2]+19
    statue = Rectangle((200,200),(location[0],location[1]+v*-1),(250,0,0),"16_p_tileset.png")
    statue.set_image(my_sprite_sheet.image_at((16*51,16*6,32,48)),True)
    statue.z_position = location[2]
    statue.set_size((75,100))
    return statue

pressed =False
my_sprite_sheet = SpriteSheet("16_p_tileset.png")
my_walks = SpriteSheet("Basic Charakter Spritesheet.png")
walk_idle = [1]
for i in range(3):
    walk_idle.append(my_walks.image_at((50,50*(i+1),40,40)))
walk_back = [1]
for i in range(3):
    walk_back.append(my_walks.image_at((50*(i+1),50,40,40)))
walk_front = [1]
for i in range(3):
    walk_front.append(my_walks.image_at((50*(i+1),0,40,40)))
walk_left = [1]
for i in range(3):
    walk_left.append(my_walks.image_at((50*(i+1),100,40,40)))
walk_right = [1]
for i in range(3):
    walk_right.append(my_walks.image_at((50*(i+1),150,40,40)))

my_walk = walk_idle
p = Rectangle((width/5,height/15),(width/2,height/2),(250,0,0),"Basic Charakter Spritesheet.png")
p.set_image(walk_front[1],True)
p.set_size((100,100))
p.z_position = 0
my_sprites = {}
g1 = statue((width/2,height/2,200))
g3 = tree((width/2-100,height/2,150))
g2 = statue((width/2,height/2,100))
my_sprites["fg"] = g1
my_sprites["fg1"] = g2
my_sprites["fg2"] = g3
my_sprites["p"] = p
out_of_charakter = False
#you have to summand y+(z+z:4)*-1
printing_row = []

def make_row(key):
    c = 0
    d = True
    while d:
        if my_sprites[key].z_position >= my_sprites[printing_row[c]].z_position:
            printing_row.insert(c,key)
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
counter = 0     

while True:
    if p.return_perfect_colission(my_sprites["fg2"]):
        p.kill()
    if counter <= 4:
        counter += 1
    else:
        p.set_image(my_walk[my_walk[0]],True)
        if my_walk[0] <= 2:
            my_walk[0] += 1
        else:
            my_walk[0] = 1
        p.set_size((100,100))
        counter = 0

    clock.tick(30)
    if pressed != False:
        if pressed == "up":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0,0.7)
                    if out_of_charakter == True:
                        my_sprites[key].change_position(0,0.7)
            if out_of_charakter == True:
                my_sprites["p"].change_position(0,1.4)
            else:
                my_sprites["p"].z_position += 0.7
            del printing_row[printing_row.index("p")]
            make_row("p")

        if pressed == "down":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0,-0.7)
                    if out_of_charakter == True:
                        my_sprites[key].change_position(0,-0.7)
            if out_of_charakter == True:
                my_sprites["p"].change_position(0,-1.4)
            else:
                my_sprites["p"].z_position -= 0.7
            del printing_row[printing_row.index("p")]
            make_row("p")

        if pressed == "right":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(-0.7,0)
                    if out_of_charakter == True:
                        my_sprites[key].change_position(-0.7,0)
            if out_of_charakter == True:
                my_sprites["p"].change_position(-1.4,0)

        if pressed == "left":
            for key in printing_row:
                if not key == "p":
                    my_sprites[key].change_position(0.7,0)
                    if out_of_charakter == True:
                        my_sprites[key].change_position(0.7,0)
            if out_of_charakter == True:
                my_sprites["p"].change_position(1.4,0)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_walk = walk_back
                pressed = "up"
            elif event.key == pygame.K_DOWN:
                my_walk = walk_front
                pressed = "down"
            elif event.key == pygame.K_LEFT:
                my_walk = walk_left
                pressed = "left"
            elif event.key == pygame.K_RIGHT:
                my_walk = walk_right
                pressed = "right"
            elif event.key == pygame.K_SPACE:
                if out_of_charakter == True:
                    out_of_charakter = False
                else:
                    out_of_charakter = True

        if event.type == pygame.KEYUP:
            my_walk = walk_idle
            pressed = False

    screen.fill((250,250,250))
    for key in printing_row:
        my_sprites[key].update(screen)
    pygame.display.update()