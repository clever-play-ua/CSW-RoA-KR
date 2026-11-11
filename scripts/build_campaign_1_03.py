"""Thin wrapper: the build now lives in war3-campaign-localization/tools/l10n.py (see FORMAT.md there)."""
import subprocess
import sys

TOOL = r"C:\Users\UserM\Documents\GitHub\war3-campaign-localization\tools\l10n.py"
subprocess.run([sys.executable, TOOL, "build", "CSW-RoA", "KR"], check=True)
