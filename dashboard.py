import platform
import sys
import subprocess
from datetime import datetime
from flask import Flask

app = Flask(__name__)

hostname = platform.node()
python_version = sys.version.split()[0]
hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

branch = subprocess.run(
    ["git", "branch", "--show-current"],
    capture_output=True,
    text=True
).stdout.strip()

status = subprocess.run(
    ["git", "status", "--porcelain"],
    capture_output=True,
    text=True
)

if status.stdout.strip():
    git_status = "⚠️ Cambios pendientes"
else:
    git_status = "✅ Repositorio limpio"


@app.route("/")
def home():
    return f"""
    <h1>⚙️ Edarji Home Lab</h1>

    <h2>{hostname}</h2>

    <p>🐍 Python: {python_version}</p>
    <p>🕐 Hora: {hora}</p>
    <p>🌿 Git branch: {branch}</p>
    <p>{git_status}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
