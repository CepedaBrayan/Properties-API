from datetime import timedelta

from minio import Minio

from .config import settings

"""
    MinioFactory is a class with lazy initialization of minio client
    and methods to upload files to minio bucket
"""


class MinioFactory:
    _client = None

    """
        get_client() returns a minio client
        if client is not initialized, it creates a new client
    """

    @classmethod
    def get_client(cls) -> Minio:
        if cls._client is None:
            cls._client = cls.create_client()
        return cls._client

    """
        create_client() creates a new minio client
    """

    @classmethod
    def create_client(cls) -> Minio:
        try:
            return Minio(
                settings.minio_url,
                settings.minio_access_key,
                settings.minio_secret_key,
                secure=False,
            )
        except Exception as e:
            print("Error creating minio client: ", e)
            raise e

    """
        check_bucket() checks if bucket exists, if not, it creates a new bucket
    """

    def check_bucket(self) -> None:
        client = self.get_client()
        if not client.bucket_exists(settings.minio_bucket_name):
            client.make_bucket(settings.minio_bucket_name)

    """
        upload_image() uploads a file to minio bucket
        returns the url of the file
    """

    def upload_image(self, file, object_name) -> str:
        try:
            client = self.get_client()
            self.check_bucket()
            client.put_object(
                bucket_name=settings.minio_bucket_name,
                object_name=object_name,
                data=file.file,
                length=-1,
                part_size=10 * 1024 * 1024,
            )
            _url = client.get_presigned_url(
                "GET",
                settings.minio_bucket_name,
                object_name,
                expires=timedelta(days=7),
            )

            return _url
        except Exception as e:
            print("Error uploading image: ", e)
            raise e
