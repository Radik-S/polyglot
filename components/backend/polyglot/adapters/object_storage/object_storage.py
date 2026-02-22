import boto3

from polyglot.application.interfaces import IObjectStorage


class ObjectStorage(IObjectStorage):

    def __init__(self, s3_client: boto3.client, bucket_name: str,
                 expires_in: int):
        self.s3_client = s3_client
        self.bucket_name = bucket_name
        self.expires_in = expires_in

    def generate_presigned_url(self, object_key: str,
                               content_type: str) -> str:
        """Генерирует ссылку для загрузки файла"""
        presigned_url = self.s3_client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": self.bucket_name,
                "Key": object_key,
                "ContentType": content_type,
            },
            ExpiresIn=self.expires_in,
        )
        return presigned_url
