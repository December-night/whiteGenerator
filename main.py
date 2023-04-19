import shutil
import os
import sys
import time
import base64
import random
import string
import subprocess
from PIL import Image
import requests
import json
from io import BytesIO
import styles
import openai
from styles import properties
import colorsys

#KEY OPEN AI API (DONT SHARE IT)
openai.api_key = "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"


#TEXT GENERATOR
def generate_random_text():
    decision = input("Enter a prompt for the AI model to generate text: ") #PROMPT that the AI will use to generate text
    textSize = random.randint(80, 140) #TEXT SIZE
    response = openai.Completion.create(
        engine="text-davinci-002", #AI MODEL
        prompt=decision, #PROMPT
        max_tokens=textSize, #TEXT SIZE
        n=1, #NUMBER OF TEXTS
        stop=None, #STOP
        temperature=random.uniform(0.5, 1.0) #TEMPERATURE(Dont change it) TEXT ORIGINALITY(UNIQUE TEXT)
    )

    response.choices[0].text = "".join(response.choices[0].text.splitlines()) #REMOVE LINES
    time.sleep(0.5) #TIME TO GENERATE TEXT
    
    return str(response.choices[0].text.strip().encode('utf-8').decode('utf-8')) #RETURN TEXT in UTF-8


#IMAGE GENERATOR
def ImageGen():
    API_KEY = "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" #API KEY (DONT SHARE IT)

    prompt = input("Enter an images prompt: ") #PROMPT THAT THE AI WILL USE TO GENERATE IMAGE

    image_size = random.choice(properties["image_size"]) #IMAGE SIZE

    num_images = 1 #NUMBER OF IMAGES

    data = { #DATA THAT THE AI WILL USE TO GENERATE IMAGE
        "model": "image-alpha-001", #AI MODEL
        "prompt": prompt, #PROMPT
        "size": image_size, #IMAGE SIZE
        "num_images": num_images, #NUMBER OF IMAGES  (DONT CHANGE IT)
    }
    headers = {
        "Content-Type": "application/json", #CONTENT TYPE
        "Authorization": f"Bearer {API_KEY}", #AUTHORIZATION
    }
    response = requests.post(
        "https://api.openai.com/v1/images/generations", data=json.dumps(data), headers=headers) #REQUEST TO API

    # Check the response status code
    if response.status_code != 200: #CHECK IF THE RESPONSE IS 200
        raise Exception(f"Failed to generate image: {response.text}") #IF NOT 200 THEN RAISE ERROR

    # Parse the response JSON
    result = json.loads(response.text)
    # Get the generated image URL
    image_url = result["data"][0]["url"]
    # Download the image from the URL
    response = requests.get(image_url)
    # Load the image into a PIL image object
    img = Image.open(BytesIO(response.content))
    # Save the image to a file

    imageName = prompt + \
        random.choice(string.ascii_uppercase + string.digits) + ".png"

    global image #GLOBAL IMAGE VARIABLE

    image = imageName #IMAGE VARIABLE

    img.save("results/{}/{}".format(FinalPath, imageName)) #SAVE IMAGE TO A FILE
    return imageName, image







colorsMass = { #COLORS MASS (DONT CHANGE IT, ONLY ADD NEW COLORS)
    "first": '81, 163, 163',
    "second": '195, 233, 145',
    "third": '255, 255, 255',
    "fourth": '99, 164, 108',
    "fifth": '232, 233, 235',
    "sixth": '232, 233, 235',
    "seventh": '224, 223, 213',
    "eighth": '244, 253, 175',
}

#Give a random color from the list
def randomColor():
    color = random.choice(list(colorsMass.values()))
    color = tuple(map(int, color.split(',')))
    return color




def generate_color_palette(start_color, num_colors):
   # Вычисляем противоположный цвет
    opposite_color = (
        255 - start_color[0], 255 - start_color[1], 255 - start_color[2])

    # Разбиваем диапазон цветов на num_colors равных интервалов
    color_step = 15 / (num_colors - 1)

    # Создаем массив цветов
    palette = []
    for i in range(num_colors):
        # Вычисляем текущий цвет
        color = (
            round(start_color[0] + i * color_step),
            round(start_color[1] + i * color_step),
            round(start_color[2] + i * color_step)
        )

        # Добавляем текущий цвет в палитру
        palette.append(color)

    # Добавляем противоположный цвет в палитру
    palette.append(opposite_color)

    return palette

colorMAIN = generate_color_palette((randomColor()), 9) #MAIN COLOR


def generateFavicon():
    ImageGen() 
    # Convert the image to a favicon.ico file
    img = Image.open("results/{}/{}".format(FinalPath, image)) # Open the image
    img = img.resize((24, 24), Image.LANCZOS) # Resize the image
    img.save("results/{}/favicon.ico".format(FinalPath), sizes=[(24, 24)]) # Save the image as a favicon.ico file
    return f"""<link rel="icon" href="favicon.ico" type="image/x-icon" />"""


def CssSize():
    # Generate random CSS width and height
    width = random.choice(properties["Width"]) #WIDTH
    height = random.choice(properties["Height"]) #HEIGHT

    return f"""width: {width}; 
    height: {height};
    """



def backgroundCont():
    color = colorMAIN[0]

    return f"""background-color: rgb{color};"""


def SimplyText(colorMAIN):

    color = colorMAIN[0]
    font_size = random.choice(properties["Font-size"]) #FONT SIZE
    font_weight = random.choice(properties["Font-weight"]) #FONT WEIGHT
    font_family = random.choice(properties["Font-family"]) #FONT FAMILY
    text_align = random.choice(properties["Text-align"]) #TEXT ALIGN
    return f"""color: rgb{color};
    font-size: {font_size};
    font-weight: {font_weight};
    font-family: {font_family};
    text-align: {text_align};
    """


def Display():
    display = random.choice(properties["Display"])
    justify = random.choice(properties["justify-content"])
    align = random.choice(properties["align-items"])
    align_content = random.choice(properties["align-content"])

    return f"""display: {display};
    justify-content: {justify};
    align-items: {align};
    align-content: {align_content};
    """


def Nav():
    display = (properties["Display"][3])
    justify = random.choice(properties["justify-content"])
    align = random.choice(properties["align-items"])
    align_content = random.choice(properties["align-content"])

    return f"""display: {display};
    justify-content: {justify};
    align-items: {align};
    align-content: {align_content};
    """


def NavText():

    color = colorMAIN[1]
    font_size = random.choice(properties["Font-size-nav"])
    font_weight = random.choice(properties["Font-weight"])
    font_family = random.choice(properties["Font-family"])
    text_align = random.choice(properties["Text-align"])
    return f"""color: rgb{color};
    font-size: {font_size};
    font-weight: {font_weight};
    font-family: {font_family};
    text-align: {text_align};
    """


def Dflex():
    display = (properties["Display"][2])

    return f"""display: {display} !important;
    """


def FlexDirectionCol():
    direction = properties["flex-direction"][2]

    return f"""flex-direction: {direction};
    """


def JustifyContentCenter():
    justify = properties["justify-content"][0]

    return f"""justify-content: {justify};
    """


def Background(colorMAIN):

    r = colorMAIN[0][0]
    g = colorMAIN[0][1]
    b = colorMAIN[0][2]

    rgb = (r, g, b)
    # Вычисляем противоположный цвет
    r = 255 - rgb[0]
    g = 255 - rgb[1]
    b = 255 - rgb[2]

    background = [(r, g, b)]
    backgroundColor = background[0]
    return f"""background-color: rgb{backgroundColor};
    """


def BackgroundFooter(colorMAIN):

    r = colorMAIN[8][0]
    g = colorMAIN[8][1]
    b = colorMAIN[8][2]

    rgb = (r, g, b)
    # Вычисляем противоположный цвет
    r = 255 - rgb[0]
    g = 255 - rgb[1]
    b = 255 - rgb[2]

    background = [(r, g, b)]
    # convert to string

    backgroundColor = background[0]
    return f"""background-color: rgb{backgroundColor};
        """


def Margin():
    margin = random.choice(properties["Margin"])
    return f"""margin: {margin};
    """


def Border():
    border = random.choice(properties["Border"])
    return f"""border: {border};
    """


def textAlignCenter():
    text_align = properties["Text-align"][0]
    return f"""text-align: {text_align}!important;
    """


def FooterGen():
    color = colorMAIN[3]
    font_size = random.choice(properties["Font-size-footer"])
    font_weight = random.choice(properties["Font-weight"])
    font_family = random.choice(properties["Font-family"])
    text_align = random.choice(properties["Text-align"])
    return f"""color: rgb{color};
    font-size: {font_size};
    font-weight: {font_weight};
    font-family: {font_family};
    text-align: {text_align};
    """


def Container():
    random_text = generate_random_text()
    return f"""<div class="container">
         <div class="text-wrapper">
         <p>{random_text}</p>
         </div>
         </div>
         """


def Text():
    random_text = generate_random_text()
    return f"""{random_text}
         """


def RandomContainer():
    if random.randint(1, 2) == 1:
        random_text = generate_random_text()
        return f"""<div class="container">
         <div class="text-wrapper">
         <p>{random_text}</p>
         </div>
         </div>
         """
    else:
        return ""


def RandomFooterNav():
    if random.randint(1, 2) == 1:
        return f"""
    <ul class="FooterClass">
    <li>About</li>
    <li>Faq</li>
    <li>Home</li>
    </ul>
        
         """
    else:
        return ""


def ImageContainer():
    random_image = ImageGen()
    return f""" <div class="image-wrapper">
    <img class="image1" src="{random_image[0]}" alt="image">
    {RandomContainer()}
    </div>
         """


def ImageContainer2():
    random_image = ImageGen()
    return f""" <div class="image-wrapper1">
    <img class="image1" src="{random_image[0]}" alt="image">
    {RandomContainer()}
    </div>
         """


def RandomImageContainer():
    if random.randint(1, 2) == 1:
        random_image = ImageGen()
        return f""" <div class="image-wrapper" style="flex-direction: column;align-items: center!important;">
    <img class="image1" src="{random_image[0]}" alt="image">
    {RandomContainer()}
    </div>
         """
    else:
        return ""


def RandomImageContainer2():

    return f""" 
        <div class="image-wrapper-fourth">
            <div class="col-6">
                <div class="dop-img-wrap">
                    {ImageContainer2()}
                    {Container()}
                </div>
                <div class="dop-img-wrap">
                    {ImageContainer2()}
                    {Container()}
                </div>
            </div>
            <div class="col-6">
                <div class="dop-img-wrap">
                   {ImageContainer2()}
                   {Container()}
                </div>
                <div class="dop-img-wrap">
                    {ImageContainer2()}
                    {Container()}
                </div>
            </div>
        </div>

    </div>
            """

a = False
b = False


def RightBorder():
   
    if random.randint(1, 2) == 1 or a == True:
        b = True
        rightBor = properties["right-border"][0]
        bottomBor = rightBor 
        borderRad = str(random.randint(5,15)) + "px"
        
        return f"""border-right: {rightBor};
        border-bottom: {bottomBor};
        border-radius: {borderRad};
        
        """, b
    else:
        return ""
    
def LeftBorder():
    if random.randint(1, 2) == 1 or b == True:
        a = True
        leftBor = properties["left-border"][0]
        bottomBor = leftBor 
        borderRad = str(random.randint(5,15)) + "px"
        
        return f"""border-left: {leftBor};
        border-bottom: {bottomBor};
        border-radius: {borderRad};
        """, a

def DownHeaderBg():
    return f"""<div class="down-header">
    <h1>{Text()}</h1>
    </div>"""


def RandomContainer2():

    return f"""  <div class="wrapper-main">
            <div class="main-dop-wrap">
                <div class="col-wrap">
                    <div class="col">
                        <p class="text-wrap">{Text()}</p>
                    </div>
                    <div class="vertical"></div>
                    <div class="col">
                        <p class="text-wrap">{Text()}</p>
                    </div>
                    <div class="vertical"></div>
                    <div class="col">
                        <p class="text-wrap">{Text()}</p>
                    </div>
                    
                </div>
                <div>
                    <button class="button">Learn more</button>
                </div>
            </div>

        </div>"""
        



def RandomImageLeft():

    random_image = ImageGen() #Call function to generate random image
    return f""" <div class="image-wrapper">
        {Container()}
    <img class="image1 right-border" src="{random_image[0]}" alt="image">
    </div>
         """


def RandomImageRight():

    random_image = ImageGen() #Call function to generate random image
    return f""" <div class="image-wrapper">
    <img class="image1" src="{random_image[0]}" alt="image">
     {Container()}
    </div>
         """


#Random Width from properties
def RandomWidth():
    width = random.choice(properties["Width"])
    return f"""width: {width};
    """

#Random Border Color from ColorMain
def BorderColor():
    border_color = colorMAIN[3]
    return f"""border-color: rgb{border_color};
    """


def BorderRadius():
    border_radius = random.choice(properties["Border-radius"])
    return f"""border-radius: {border_radius};
    """


def BackgroundImage():
    print('Please enter a background image:')
    random_image = ImageGen()
    return f"""background-image: url("{random_image[0]}");
    """


def RandomFunction():
    func = []
    size = input("Enter size of site(from 1 to 9): ")
    size = int(size)
    if size <= 0:
        print("Error")
        return
    elif size >= 10:
        print("Error too big size")
        return
    count = 0
    while count < int(size):
        if random.randint(1, 2) == 1:
            func.append(RandomImageRight())
            count += 1
            if count == int(size):
                break
        if random.randint(1, 2) == 1:
            func.append(RandomImageLeft())
            count += 1
            if count == int(size):
                break
        if random.randint(1, 2) == 1:
            func.append(RandomContainer())
            count += 1
            if count == int(size):
                break
        if random.randint(1, 2) == 1:
            func.append(RandomImageContainer2())
            count += 1
            if count == int(size):
                break
            

    func = "".join(func)

    return func


def HtmlGen():
    # Generate random HTML code with random CSS styles

    b = random.randint(1, 2)
    head = f"""<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    {generateFavicon()}
    <link rel="stylesheet" href="style.css">
    <title>{NameFile}</title>
    </head>
    """
    body = f"""<body>
    <header class="header">
      <div class="nav">
            <a href="index.html">Home</a>
            <a href="">About</a>
            <a href="">Contact</a>
        </div>
    </header>
    <div class="main-wrapper">
    {DownHeaderBg()}
    <div class="main">
    
    {RandomFunction()}
    
    
    </div>
    </div>
 
    <footer class="footer">
    <p class="">&copy; 2023 {NameFile}</p>
    {RandomFooterNav()}
    </footer>
    </body>
    """
    html = f"""<html>
    {head}
    {body}
    </html>
    """

    css = open('results/{}/style.css'.format(FinalPath), 'w')
    css.write('body{' + 'height:100%;width:100%;margin:0px;padding:0px;overflow-x:hidden;' + str(Background(colorMAIN)) + '}\n' + '.image1{' + str(Display())  + str(Margin()) + str(Border()) + str(BorderColor()) + str(BorderRadius()) + 'height:430px;' + '}\n' + '.main{' + 'width:75%;align-items:center;' + str(Dflex()) + str(FlexDirectionCol()) + '}\n' + 'h1{' + str(SimplyText(colorMAIN)) + 'font-size:2rem;' + '}\n'
              + 'p{' + str(SimplyText(colorMAIN)) + 'width:100%;' + 'hyphens:auto;' + '}\n' + '.header{' + 'width:100%;height:50px;' + Display() + str(BackgroundFooter(colorMAIN)) + '}\n' +
              '.nav{' + 'height:100%;' + 'width:100%; align-items:center !important;' + Dflex() + Display() + '}\n' +
              '.container{' + Dflex() + JustifyContentCenter() +
              'width:100%' + '}\n' +
              '.nav a{' + NavText() + 'margin-left:15px;' + '}\n' + '.text-wrapper{' + 'width:90%;height:auto;text-decoration:none; '+ RightBorder() + Dflex() + '}\n' + '.image-wrapper{' + 'width:100%;height:auto;align-items: center !important;' + Dflex() + Display() + '}\n' +
              '.footer{' + 'width:100%;height:100px;text-align:center !important;align-items:center !important;' + Dflex() + Display() + str(BackgroundFooter(colorMAIN)) + '}\n' +
              '.FooterClass{' + Dflex() + JustifyContentCenter() + 'margin-right:40px' + '}\n' + '.FooterClass li{' +
              'list-style-type:none;' + 'margin-left:15px;' +
              str(SimplyText(colorMAIN)) + '}\n'
              + '.footer p{' + textAlignCenter() + '}' + '.dop-img-wrap{' + 'width:50%;align-items:center;' + Dflex() + FlexDirectionCol() + '}\n' + '.image-wrapper-fourth{' +
              'justify-content: space-between;' + Dflex() + FlexDirectionCol() + '}\n' +
              '.col-6{' + Dflex() + 'justify-content: space-between;' + '}\n'
              + '.image2{' + 'width:55%;' + Margin() + '}' + '.image-wrapper1{' + Dflex() + FlexDirectionCol() + '}' + '.wrapper-main{' + Dflex() + JustifyContentCenter() + 'width:100%;margin-bottom:50px;' + '}' +
              ' .main-dop-wrap{' + Dflex() + FlexDirectionCol() + 'width:70%;align-items:center;padding:30px;' + str(BackgroundFooter(colorMAIN)) + JustifyContentCenter() + BorderRadius() + '}' +
              '.col-wrap{' + Dflex() + JustifyContentCenter() + 'width:100%;' + '}' + '.text-wrap{' +
              'margin:0px;text-align:center;' + '}\n' +
              '.button:hover{' + backgroundCont() + '}\n'
              + '.button{' + 'width:150px;height:50px;' + BackgroundFooter(colorMAIN) + 'border: 2px solid;\n'  + str(BorderColor()) + SimplyText(
        colorMAIN) + '}' + '.nav a:hover{' + 'padding-bottom:5px;box-shadow: 0 0 10px rgb(255, 255, 255);border-radius:100px;' + 'color:#fff' + '}\n' + '.main-wrapper{' + Dflex() + FlexDirectionCol() + 'align-items:center' + '}\n' + '.down-header{' + 'width:100%;height:500px;background-repeat: no-repeat;background-size: cover;' + Dflex() + JustifyContentCenter() + str(BackgroundImage())  + '}\n')

    css.close()

    if css.close():
        print("CSS file saved successfully")

    for i in range(len(html)):
        html = html.replace('\n', '')
        html = html.replace('  ', '')
        html = html.replace('   ', '')
        html = html.replace('    ', '')
  

    return html


def FinalPath():
    # Generate a random path
    global NameFile
    NameFile = 'index'
    global FinalPath
    randomPath = ''.join(random.choices( # Generate a random path
        string.ascii_uppercase + string.digits, k=10)) 
    FinalPath = NameFile + randomPath # Generate a random path and file name
    os.mkdir('results/{}'.format(FinalPath)) # Create a folder with a random path
    return FinalPath


def FileGen():
    # Generate a random HTML file
    html = HtmlGen() # Generate a random HTML file
    time.sleep(1) # Wait 1 second
    file = open('results/{}/{}.html'.format(FinalPath, NameFile), 'w') # Create a random HTML file
    file.write(html) # Write a random HTML file
    file.close() # Close the file
    if file.close(): # If the file is closed
        print("HTML file saved successfully") # Print a message


def Main():
    # Generate a random HTML file and a random image

    FinalPath()
    FileGen()
    # ImageGen()
    print(NameFile + '.html saved successfully')


if __name__ == "__main__":
    Main()
