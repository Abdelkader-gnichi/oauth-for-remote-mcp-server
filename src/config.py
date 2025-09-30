from decouple import config


class Settings:
    # ScaleKit Configuration
    SCALEKIT_ENVIRONMENT_URL: str = config("SCALEKIT_ENVIRONMENT_URL", "")
    SCALEKIT_CLIENT_ID: str = config("SCALEKIT_CLIENT_ID", "")
    SCALEKIT_CLIENT_SECRET: str = config("SCALEKIT_CLIENT_SECRET", "")
    SCALEKIT_RESOURCE_METADATA_URL: str = config("SCALEKIT_RESOURCE_METADATA_URL", "")
    SCALEKIT_AUDIENCE_NAME: str = config("SCALEKIT_AUDIENCE_NAME", "")
    METADATA_JSON_RESPONSE: str = config("METADATA_JSON_RESPONSE", "")

    # Tavily API Key
    TAVILY_API_KEY: str = config("TAVILY_API_KEY", "")

    # Server Port
    PORT: int = int(config("PORT", 8000))

    def __post_init__(self):
        if not self.SCALEKIT_CLIENT_ID:
            raise ValueError("SCALEKIT_CLIENT_ID environment variable not set")
        if not self.SCALEKIT_CLIENT_SECRET:
            raise ValueError("SCALEKIT_CLIENT_SECRET environment variable not set")
        if not self.SCALEKIT_ENVIRONMENT_URL:
            raise ValueError("SCALEKIT_ENVIRONMENT_URL environment variable not set")
        if not self.SCALEKIT_RESOURCE_METADATA_URL:
            raise ValueError("SCALEKIT_RESOURCE_METADATA_URL environment variable not set")
        if not self.SCALEKIT_AUDIENCE_NAME:
            raise ValueError("SCALEKIT_AUDIENCE_NAME environment variable not set")
        if not self.TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY environment variable not set")

settings = Settings()
