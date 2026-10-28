
from datasets import load_from_disk

path = "data/processed/banglanmt_sample_1000"

print("Loading cleaned dataset...")
dataset = load_from_disk(path)

print("\nDataset verification")
print("--------------------")
print("Total rows:", len(dataset))
print("Columns:", dataset.column_names)

# Check empty values
empty_bn = sum(
    1 for row in dataset
    if not isinstance(row["bn"], str) or not row["bn"].strip()
)
empty_en = sum(
    1 for row in dataset
    if not isinstance(row["en"], str) or not row["en"].strip()
)

print("Empty Bengali translations:", empty_bn)
print("Empty English translations:", empty_en)

print("\nFirst 5 translation pairs:")
for i in range(min(5, len(dataset))):
    print(f"\nPair {i + 1}")
    print("Bengali:", dataset[i]["bn"])
    print("English:", dataset[i]["en"])
