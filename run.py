from src.main import app
from uvicorn import run
from pathlib import Path
import os

if os.name == "nt":
    run(app, host="0.0.0.0", port=443)
else:
    CERT_FILE = Path(os.getenv("SSL_CERT", "/etc/ssl/cloudflare/origin.pem"))
    KEY_FILE = Path(os.getenv("SSL_KEY", "/etc/ssl/cloudflare/origin.key"))

    for p in (CERT_FILE, KEY_FILE):
        if not p.exists():
            raise FileNotFoundError(f"证书文件不存在: {p}")
    run(app, host="0.0.0.0", port=443,
        ssl_certfile=str(CERT_FILE), ssl_keyfile=str(KEY_FILE))