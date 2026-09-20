import platform
import sys
import subprocess
from datetime import datetime

print(platform.node())
print(sys.version)
print(datetime.now())

branch = subprocess.run(
    ["git", "branch", "--show-current"],
    capture_output=True,
    text=True
)

print(branch.stdout.strip())
status = subprocess.run(
    ["git", "status", "--porcelain"],
    capture_output=True,
    text=True
)

if status.stdout.strip():
    print("⚠️ Cambios pendientes")
else:
    print("✅ Repositorio limpio")
