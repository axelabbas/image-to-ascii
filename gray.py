from PIL import Image, ImageDraw, ImageFont
import cv2, numpy

def resize(image, new_width = 100):
    old_width, old_height = image.size
    new_height =  new_width * old_height / old_width
    return image.resize((int(new_width), int(new_height)))


def to_greyscale(image):
    return image.convert("L")

ASCII_CHARS = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^    ")
ASCII_CHARS.reverse()

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str

def PILimgToAsciiText(image):
    image = resize(image)
    greyscale_image = to_greyscale(image)
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    return {"ascii":ascii_img, "h": greyscale_image.height, "w": greyscale_image.width}

def AsciiTextToImg(ascii, h, w, bg="black", textRgb=(255,255,255)):
    scale = 25
    img = Image.new("RGB", (h * scale, w * scale), color=bg)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("C:\\Users\\ns\\Downloads\\Compressed\\Courier_Prime\\CourierPrime-Regular.ttf", scale)
    rows = ascii.split("\n")
    for indexRows, row in enumerate(rows):
        for indexCols, col in enumerate(row):
            d.text((indexCols * scale, indexRows * scale), col, fill=textRgb, font=fnt)
    return img

def vidToFrames(video):
    capture = cv2.VideoCapture(video)
    frames = []
    frameNr = 0 
    while True:
        success,frame = capture.read()
        if success:
            frames.append(frame)
        else:
            break
        frameNr = frameNr + 1
    capture.release()
    return frames

def videoToAsciiVideo(inputPath, outputPath):
    frames = vidToFrames(inputPath)
    asciiImages = []
    for index, frame in enumerate(frames):
        PilImg = Image.fromarray(frame)
        Ascii = PILimgToAsciiText(PilImg)
        AsciiText, w, h = Ascii["ascii"],Ascii["w"],Ascii["h"]
        AsciiImg = AsciiTextToImg(AsciiText, w, h)
        opencvImage = cv2.cvtColor(numpy.array(AsciiImg), cv2.COLOR_RGB2BGR)
        asciiImages.append(opencvImage)
    
    height, width, layers = asciiImages[0].shape
    video = cv2.VideoWriter(outputPath, 0 , 30, (width,height))

    for image in asciiImages:
        video.write(image)
    
    cv2.destroyAllWindows()
    video.release()
videoToAsciiVideo("inputs/killua.mp4","outputs/22.mp4")