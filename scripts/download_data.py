import kagglehub

# Download latest version
path = kagglehub.dataset_download("bsthere/volkswagen-stock-data-1995-2026")

print("Path to dataset files:", path)