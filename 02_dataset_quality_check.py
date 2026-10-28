
from datasets import load_from_disk
from pathlib import Path

DATA_DIR = Path("data/raw")

def check_dataset(name, dataset_path, source_col, target_col):
    print(f"\n{'=' * 60}")
    print(f"Dataset: {name}")
    print("=" * 60)

    if not dataset_path.exists():
        print(f"❌ Dataset not found: {dataset_path}")
        return

    dataset = load_from_disk(str(dataset_path))

    split_name = "train" if "train" in dataset else list(dataset.keys())[0]
    data = dataset[split_name]

    print(f"Split checked: {split_name}")
    print(f"Total rows: {len(data):,}")
    print(f"Columns: {data.column_names}")

    required = [source_col, target_col]
    if not all(col in data.column_names for col in required):
        print(f"⚠️ Expected columns not found: {required}")
        return

    sample_size = min(1000, len(data))
    sample = data.select(range(sample_size))

    empty_source = 0
    empty_target = 0
    duplicate_pairs = set()
    empty_pairs = 0

    for row in sample:
        source = row[source_col]
        target = row[target_col]

        if not isinstance(source, str) or not source.strip():
            empty_source += 1

        if not isinstance(target, str) or not target.strip():
            empty_target += 1

        pair = (source, target)
        if pair in duplicate_pairs:
            empty_pairs += 1
        duplicate_pairs.add(pair)

    print(f"Rows sampled: {sample_size:,}")
    print(f"Empty source texts: {empty_source}")
    print(f"Empty target texts: {empty_target}")
    print(f"Repeated pairs in sample: {empty_pairs}")
    print("✅ Quality check completed for sample.")


check_dataset(
    "BanglaNMT",
    DATA_DIR / "banglanmt",
    "bn",
    "en"
)
