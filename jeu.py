import pyxel
pyxel.init(128, 128, title="NDC 2024")

def update():
    if pyxel.btn(pyxel.KEY_SPACE):
        print("connardouhiughiuh")
        print("test")

def draw():
    pyxel.rect(0,0,3,3,8)



pyxel.run(update,draw)
