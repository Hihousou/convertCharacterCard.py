from PIL import Image
import base64
import json

def convertCharacterCard(filePath):
    try:
        img = Image.open(filePath)
        if "chara" not in img.info:
            raise KeyError("Image doesn't countain 'chara' metadata")
        
        # Extracting base64 encoded JSON string from metadata
        jsonStr = base64.b64decode(img.info["chara"].strip()).decode("utf-8")
        characterData = json.loads(jsonStr)
        return characterData
    
    except Exception as errorMessage:
        print(f"An error occurred: {errorMessage}")
        return None