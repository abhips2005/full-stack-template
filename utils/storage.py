from utils.source import SupabaseClient

def GetURL(id: str, bucket: str):
    return f"{id}"

def SaveToBucket(buffer: bytes, id: str, bucket: str):
    response = SupabaseClient.storage.from_(bucket).upload(
        file=buffer,
        path=f"{id}",
        file_options={"cache-control": "3600", "upsert": "false"},
    )
    return response

def CreateSignedURL(id: str, bucket: str, expirySeconds: int = 180):
    response = SupabaseClient.storage.from_(bucket).create_signed_url(
        GetURL(id), expirySeconds
    )
    return response['signedURL']

def ListBucket(bucket: str):
    response = SupabaseClient.storage.from_(bucket).list()
    return response
