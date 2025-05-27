import pyscreenshot as ps
img= ps.grab(bbox = (10,10,400,400))
img.show()
img.save("screenshot.png") 