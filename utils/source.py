import os
from typing import Literal, Optional

import vecs
from groq import Groq
from pydantic import AnyUrl, BaseModel
from supabase import Client, create_client
from supabase import PostgrestAPIResponse as APIResponse

# Initialize clients only if environment variables are present
GroqClient = None
if os.getenv("GROQ_API_KEY"):
    GroqClient = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

SupabaseVector = None
if os.getenv("DB_CONNECTION"):
    SupabaseVector = vecs.Client(
        os.getenv("DB_CONNECTION"),
    )

SupabaseClient = None
if os.getenv("SUPABASE_URL") and os.getenv("SUPABASE_KEY"):
    SupabaseClient: Client = create_client(
        os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")
    )

class Config(BaseModel):
    ENV: Literal["production", "development"]
    FRONTEND: AnyUrl = "http://localhost:5173"

config = Config.model_validate({
    "ENV": os.getenv("ENV", "development"), 
    "FRONTEND": os.getenv("FRONTEND", "http://localhost:5173")
}).model_dump()