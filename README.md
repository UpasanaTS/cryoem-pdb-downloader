
# Cryo-EM PDB Downloader

A simple Python tool to download PDB structures solved using Cryo-Electron Microscopy (Cryo-EM) from the RCSB database.

## How It Works

1. Uses RCSB's API to find structures with experimental method = "ELECTRON MICROSCOPY"
2. Downloads `.cif` files for each matching PDB ID into the `data/` directory

## Usage

```bash
python download_cryoem_structures.py
```

## Requirements

- Python 3.x
- requests (install with `pip install requests`)
