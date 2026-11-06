import ctypes
from pathlib import Path

ACTION_CODE = 20
UPDATE_FLAG = 1 | 2

def set_wallpaper(image_path: Path) -> bool:
    image_path = image_path.resolve()

    if not image_path.is_file():
        print(f"File not Found")
        return False
    
    result = ctypes.windll.user32.SystemParametersInfoW
    result.argtypes = [
        ctypes.c_uint,
        ctypes.c_uint,
        ctypes.c_wchar_p,
        ctypes.c_uint,
    ]
    result.restype = ctypes.c_int

    return bool (
        result(
            ACTION_CODE,
            0,
            str(image_path),
            UPDATE_FLAG,
        )
    )

if __name__ == "__main__":
    image = Path(__file__).resolve().parent / "test.jpg"
    print(f"Using Image: {image}")

    if set_wallpaper(image):
        print("Wallpaper Updated")
    else:
        print("Wallpaper Failed")
        exit(1)