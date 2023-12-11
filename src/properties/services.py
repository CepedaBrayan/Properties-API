from sqlalchemy.orm import Session

from src.bucket import MinioFactory

from .crud import create_property_image
from .models import PropertyImage

"""
This function initializes the Minio client and uploads the image to the bucket, after that it creates the PropertyImage object in the database.
"""


def add_property_image(db: Session, property_id: int, file) -> PropertyImage:
    minioClient = MinioFactory()
    image_url = minioClient.upload_image(file, file.filename)
    property_image = create_property_image(
        db=db, property_id=property_id, image_url=image_url
    )

    return property_image
