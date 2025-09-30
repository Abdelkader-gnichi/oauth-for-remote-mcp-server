from decouple import config


class Settings:
    def __init__(self):
        # ScaleKit Configuration
        self.SCALEKIT_ENVIRONMENT_URL: str = config("SCALEKIT_ENVIRONMENT_URL", default="")
        self.SCALEKIT_CLIENT_ID: str = config("SCALEKIT_CLIENT_ID", default="")
        self.SCALEKIT_CLIENT_SECRET: str = config("SCALEKIT_CLIENT_SECRET", default="")
        self.SCALEKIT_RESOURCE_METADATA_URL: str = config("SCALEKIT_RESOURCE_METADATA_URL", default="")
        self.SCALEKIT_AUDIENCE_NAME: str = config("SCALEKIT_AUDIENCE_NAME", default="")
        self.METADATA_JSON_RESPONSE: str = config("METADATA_JSON_RESPONSE", default="")

        # Tavily API Key
        self.TAVILY_API_KEY: str = config("TAVILY_API_KEY", default="")

        # Server Port
        self.PORT: int = config("PORT", cast=int, default=8000)

        # Validate required variables
        self._validate()

    def _validate(self):
        required = {
            "SCALEKIT_CLIENT_ID": self.SCALEKIT_CLIENT_ID,
            "SCALEKIT_CLIENT_SECRET": self.SCALEKIT_CLIENT_SECRET,
            "SCALEKIT_ENVIRONMENT_URL": self.SCALEKIT_ENVIRONMENT_URL,
            "SCALEKIT_RESOURCE_METADATA_URL": self.SCALEKIT_RESOURCE_METADATA_URL,
            "SCALEKIT_AUDIENCE_NAME": self.SCALEKIT_AUDIENCE_NAME,
            "TAVILY_API_KEY": self.TAVILY_API_KEY,
        }
        for key, value in required.items():
            if not value:
                raise ValueError(f"{key} environment variable not set")


settings = Settings()
    