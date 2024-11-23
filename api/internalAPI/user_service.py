import httpx

from api.internalAPI.model.user import User
from config.config import Config

config = Config()


async def get_by_id(user_id: int):
    url = f"{config.USER_SERVICE_BASE_URL}/user/{user_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            result = response.json()
            return User(**result)
        except httpx.HTTPStatusError as e:
            raise Exception(f"User with id {user_id} does not exist - Error: {str(e)}")



