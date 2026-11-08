import ctypes
from pathlib import Path

ACTION_CODE = 20
UPDATE_FLAG = 1 | 2

def set_wallpaper(image_path: Path) -> bool: #Function for setting the desktop wallpaper
    image_path = image_path.resolve() #Located the path location of the file

    if not image_path.is_file(): #Checks if the file exists with .is_file method, if file does not exist prints "File not Found"
        print(f"File not Found")
        return False
    
    setwa = ctypes.windll.user32.SystemParametersInfoW #Assigns the wallpaper to the desktop
    setwa.argtypes = [ #I DO NOT KNOW WHAT THIS MEANS T-T
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_wchar_p,
        ctypes.c_uint,
    ]
    setwa.restype = ctypes.c_int

    return bool (
        setwa(
            ACTION_CODE,
            0,
            str(image_path),
            UPDATE_FLAG,
        )
    )

if __name__ == "__main__": #I don't know what this does
    image = Path(__file__).resolve().parent / "test.jpg" #Builds the file path and assigns it to the image variable
    print(f"Using Image: {image}") #Prints a message to indicate the file used

    if set_wallpaper(image): #Conditional statement to know if wallpaper was successfully updated or not
        print("Wallpaper Updated")
    else:
        print(f"Wallpaper Failed {image}")
        exit(1) #If failed stops the script