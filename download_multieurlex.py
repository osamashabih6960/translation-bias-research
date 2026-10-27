from huggingface_hub import hf_hub_download
import tarfile
import os

print("=" * 60)
print("DOWNLOADING MULTIEURLEX")
print("=" * 60)

REPO_ID = "coastalcph/multi_eurlex"
FILENAME = "data/multi_eurlex.tar.gz"

# Download archive
archive_path = hf_hub_download(
    repo_id=REPO_ID,
    filename=FILENAME,
    repo_type="dataset"
)

print("\n✅ MultiEURLEX archive downloaded")
print("Cache location:", archive_path)

# Project destination
extract_path = "data/raw/multieurlex"
os.makedirs(extract_path, exist_ok=True)

print("\nExtracting MultiEURLEX...")

with tarfile.open(archive_path, "r:gz") as tar:
    tar.extractall(path=extract_path)

print("\n" + "=" * 60)
print("✅ MULTIEURLEX EXTRACTED SUCCESSFULLY")
print("=" * 60)
print("Location:", extract_path)