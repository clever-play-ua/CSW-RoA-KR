"""Clean English 1.03 -> localized campaign in Documents/Warcraft III/Campaigns (no Editor resave needed)."""
import sys
sys.path.insert(0, r"C:\Users\UserM\Documents\GitHub\clever-play-ua.github.io\w3r-l10n-toolkit\python_tools")
from roa_build_1_03 import build_campaign  # noqa: E402

REPO = __file__.rsplit("scripts", 1)[0]

build_campaign('koKR', REPO, 'CSW_Rise_of_the_Alliance_1_03_KR_1_0.w3n', loading_screens={
    'ACT1': REPO + 'LOADING_SCREENS_DDS/RoA_A01_INTRO_KR.dds',
    '01': REPO + 'LOADING_SCREENS_DDS/RoA_A01_M01_KR.dds',
    '02': REPO + 'LOADING_SCREENS_DDS/RoA_A01_M02_KR.dds',
    '03': REPO + 'LOADING_SCREENS_DDS/RoA_A01_M03_KR.dds',
    '04': REPO + 'LOADING_SCREENS_DDS/RoA_A01_M04_KR.dds',
})
