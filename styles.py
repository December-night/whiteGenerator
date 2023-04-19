import random


properties = {
    "background-color": [
        "aliceblue",
        "antiquewhite",
        "aqua",
        "crimson",
        "cyan",
        "darkblue",
        "darkcyan",
        "red",
        "green",
        "blue",
    ],

    "Font-family": [
        "Arial",
        "Arial Black",
        "Courier New",
        "Georgia",
        "Lucida Console",
        "Lucida Sans Unicode"],
    "Font-size": [
        str(random.randint(12, 16)) + "px",

    ],
    "Font-size-nav": [
        str(random.randint(20, 24)) + "px",
    ],
    "Font-style": [
        "italic",
        "normal",
        "oblique",
        "inherit"],
    "Display": [
        "block",
        "inline-block",
        "flex",
        "inline-flex",
    ],
    "Text-align": [
        "center",
        "left",
        "right",
        "justify",
        "inherit",
    ],
    "Text-decoration": [
        "none",
        "underline",
    ],
    "Transition": [
        "all 0.5s ease",
        "all 0.5s ease-in",
        "all 0.5s ease-out",
        "all 0.5s ease-in-out",
    ],
    "Width": [
        "85%",
        "50%",
        "75%",
    ],
    "Height": [
        "100%",

        "75%",

        "auto",
    ],
    "Margin": [
        str(random.randint(30, 50)) + "px",
    ],
    "Padding": [
        "0",
        "10px",
        "20px",
        "30px",
    ],
    "Border": [
        str(random.randint(1, 6)) + "px solid",
    ],
    "Border-color": [
        "black",
        "white",
        "red",
        "green",
        "blue",
        "yellow",
    ],
    "Border-radius": [
        str(random.randint(10, 70)) + "px",
    ],
    "Color": [
        "black",
        "white",
        "red",
        "green",
        "blue",
        "yellow",
        "orange",
        "purple",
        "brown",
        "grey",
    ],
    "justify-content": [
        "center",
        "flex-start",
        "flex-end",
        "space-between",
        "space-around",
        "space-evenly",
    ],
    "align-items": [
        "center",
        "flex-start",
        "flex-end",
        "stretch",
        "baseline",
    ],
    "align-content": [
        "center",
        "flex-start",
        "flex-end",
        "space-between",
        "space-around",
        "stretch",
    ],
    "flex-direction": [
        "row",
        "row-reverse",
        "column",
        "column-reverse",
    ],
    "image_size": [
        "512x512",
        "256x256",
    ],
    "Font-weight": [
        "bold",
        "normal",
    ],
    "Box-shadow": [
        "0 0 0 0",
        "0 0 0 1px",
        "0 0 0 2px",
        "0 0 0 3px",
        "0 0 0 4px",],
    "right-border":[
       str(random.randint(1, 5)) + "px solid",
    ],
    "left-border":[
        str(random.randint(1, 5)) + "px solid",
    ]
}
