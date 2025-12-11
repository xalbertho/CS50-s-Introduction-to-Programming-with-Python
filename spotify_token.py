#!/usr/bin/env python3
import base64
import requests

def main():
    client_id = input("Client ID: ").strip()
    client_secret = input("Client Secret: ").strip()

    # Debe coincidir EXACTAMENTE con el redirect URI del dashboard
    redirect_uri = "http://127.0.0.1:8000/callback"

    print("Code (todo lo que va después de 'code='):")
    code = input().strip()

    # Construir header Authorization: Basic base64(id:secret)
    raw = f"{client_id}:{client_secret}".encode("utf-8")
    encoded = base64.b64encode(raw).decode("utf-8")

    headers = {
        "Authorization": f"Basic {encoded}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
    }

    resp = requests.post("https://accounts.spotify.com/api/token",
                         headers=headers,
                         data=data)

    print("Status code:", resp.status_code)
    print("Respuesta de Spotify:")
    print(resp.text)


if __name__ == "__main__":
    main()
