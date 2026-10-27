from datasets import load_dataset

print("=" * 60)
print("LOADING BANGLANMT")
print("=" * 60)

banglanmt = load_dataset(
    "csebuetnlp/BanglaNMT"
)

print("\n✅ BanglaNMT loaded successfully")
print(banglanmt)

for split in banglanmt:
    print(f"\n{split} first example:")
    print(banglanmt[split][0])

print("\nSaving to project...")

banglanmt.save_to_disk(
    "data/raw/banglanmt"
)

print("\n✅ BanglaNMT saved successfully!")
print("Location: data/raw/banglanmt")