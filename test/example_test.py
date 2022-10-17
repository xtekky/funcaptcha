from src.__init__ import Funcaptcha

funcap = Funcaptcha(
    api_key="E5554D43-23CC-1982-971D-6A2262A2CA24",
    service_url="twitch-api.arkoselabs.com",
    site_url="https://www.twitch.tv",
)

key = funcap.getkey()

print(f"Key: {key}")
