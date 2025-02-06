from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

# Define the router
router = APIRouter()

@router.post('')
async def run(data: ImageData):
    try:
        # Decode the Base64 image
        image_data = base64.b64decode(data.image.split(",")[1])  # Assumes format: data:image/png;base64,<data>
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)
        
        # Analyze the image
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
        return {"message": "Image processed", "data": responses, "status": "success"}
    except Exception as e:
        print(f"Error: {e}")
        return {"message": str(e), "status": "error"}
