import sys
from pathlib import Path

# ec2_client does `from session import ...`, so aws/ must be importable directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
