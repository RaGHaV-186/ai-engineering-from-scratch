from huggingface_hub import hf_hub_download, snapshot_download

# Download a single file
model_path = hf_hub_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    filename="config.json"
)
print(f"Single file cached at: {model_path}")

# Download the full model
model_dir = snapshot_download("sentence-transformers/all-MiniLM-L6-v2")
print(f"Full model cached at:  {model_dir}")