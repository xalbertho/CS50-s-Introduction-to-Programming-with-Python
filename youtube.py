import argparse
from yt_dlp import YoutubeDL

def download(
    url: str,
    outdir: str,
    audio_only: bool,
    subtitles: bool,
    browser: str | None,
    cookies_file: str | None,
):
    ydl_opts = {
        # Máximo 720p (y mezcla con ffmpeg si viene separado)
        "format": "bestaudio/best" if audio_only else "bv*[height<=720]+ba/b[height<=720]",
        "merge_output_format": "mp4",
        "outtmpl": f"{outdir}/%(playlist_title)s/%(playlist_index)03d - %(title)s.%(ext)s",

        # Playlist / reanudar / no repetir
        "noplaylist": False,
        "ignoreerrors": True,
        "retries": 10,
        "fragment_retries": 10,
        "continuedl": True,
        "overwrites": False,
        "download_archive": f"{outdir}/.descargados.txt",

        # Mejor en USB: temporales en disco interno
        "paths": {
            "home": outdir,
            "temp": "/tmp/yt-tmp"
        },

        # Como no tienes deno, evitamos el warning (puede limitar formatos, pero es mejor que nada)
        "extractor_args": {
            "youtube": {
                "skip": ["js"]
            }
        },

        "quiet": False,
        "noprogress": False,
        "consoletitle": True,
    }

    # --- Subtítulos ---
    if subtitles:
        ydl_opts.update({
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": ["es", "es-419", "en"],
            "subtitlesformat": "srt",
            # Si quieres incrustarlos dentro del mp4 (seleccionables), descomenta:
            # "embedsubtitles": True,
        })

    # --- Solo audio ---
    if audio_only:
        ydl_opts.update({
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        })

    # --- Cookies: esto arregla el "Sign in to confirm you're not a bot" ---
    # Opción 1: desde navegador
    if browser:
        # valores típicos: chromium, chrome, brave, firefox
        ydl_opts["cookiesfrombrowser"] = (browser,)

    # Opción 2: archivo cookies.txt (si lo exportas)
    if cookies_file:
        ydl_opts["cookiefile"] = cookies_file

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    p = argparse.ArgumentParser(description="Descarga videos o playlists (solo si tienes derecho/permiso).")
    p.add_argument("url", help="URL del video o playlist")

    p.add_argument(
        "-o", "--outdir",
        default="/run/media/alberto/962809992809798F/cs50python",
        help="Carpeta de salida"
    )

    p.add_argument("--audio", action="store_true", help="Descargar solo audio (MP3)")
    p.add_argument("--subs", action="store_true", help="Descargar subtítulos (es/es-419/en)")

    # IMPORTANTE para el bloqueo anti-bot:
    p.add_argument(
        "--browser",
        default="chromium",
        help="Navegador para leer cookies: chromium, chrome, brave, firefox (default: chromium)"
    )
    p.add_argument(
        "--cookies-file",
        default=None,
        help="Ruta a cookies.txt (si prefieres exportarlas manualmente)."
    )

    args = p.parse_args()

    download(args.url, args.outdir, args.audio, args.subs, args.browser, args.cookies_file)

if __name__ == "__main__":
    main()

