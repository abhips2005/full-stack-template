from utils.source import APIResponse, SupabaseClient

class Database:
    def __init__(self, client=SupabaseClient):
        self.client = client

    async def query(self, table: str, query: dict):
        return await self.client.table(table).select("*").execute()

    async def insert(self, table: str, data: dict):
        return await self.client.table(table).insert(data).execute()

    # Add more generic database operations

def SearchSituationDB(ids: list[str], table: str = "events"):
    response = SupabaseClient.table(table).select("*").order("timestamp", desc=True).in_("id", ids).execute()  # type: APIResponse

    print(response)

    return response.data  # type: list[dict]


def SaveSituationDB(
    id: str,
    text: str,
    url: str,
    timestamp: float,
    extraData: dict = None,
    table: str = "events",
):
    response = (
        SupabaseClient.table(table)
        .upsert(
            {
                "id": id,
                "text": text,
                "url": url,
                "timestamp": timestamp,
                "extradata": extraData if extraData else None,
            }
        )
        .execute()
    )

    # print(response.data)

    return id
