import sys
import platform

print("=" * 50)
print("ENVIRONMENT VERIFICATION")
print("=" * 50)

# Python version
print(f"✅ Python: {sys.version.split()[0]}")

# OS
print(f"✅ OS: {platform.system()} {platform.release()}")

# Check packages
packages = ['numpy', 'pandas', 'matplotlib', 'seaborn']
for pkg in packages:
    try:
        module = __import__(pkg)
        print(f"✅ {pkg}: {module.__version__}")
    except ImportError:
        print(f"❌ {pkg}: NOT INSTALLED")

# Check virtual environment
import os
if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print(f"✅ Virtual environment: Active")
elif 'CONDA_PREFIX' in os.environ:
    print(f"✅ Conda environment: Active")
else:
    print("⚠️  Virtual environment: NOT active")

print("=" * 50)