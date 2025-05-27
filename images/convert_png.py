from PIL import Image

def int_to_hex_char(i):
    
    return "%X" % min(15,int(i*16/255))
    
def read_png_rgb(file_path):
    try:
        img = Image.open(file_path)
        
        img = img.convert('RGB')
        
        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                
                #print(f"Pixel at ({x}, {y}): R={r}, G={g}, B={b}")
                
                print(''.join([int_to_hex_char(i) for i in (r,g,b)]), end=" ")
            print()
                    
    except Exception as e:
        print(e)

read_png_rgb('man_on_floor.png')
