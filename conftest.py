import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "native"))
from _profile_loader import init_profile
init_profile()
