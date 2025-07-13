
import requests
import os

# Define output directory
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Step 1: Search Cryo-EM PDB IDs from RCSB
search_url = "https://search.rcsb.org/rcsbsearch/v2/query"

query = {
  "query": {
    "type": "terminal",
    "service": "text",
    "parameters": {
      "attribute": "exptl.method",
      "operator": "exact_match",
      "value": "ELECTRON MICROSCOPY"
    }
  },
  "return_type": "entry",
  "request_options": {
    "pager": {
      "start": 0,
      "rows": 50
    },
    "scoring_strategy": "combined"
  }
}

response = requests.post(search_url, json=query)
response.raise_for_status()
results = response.json()

pdb_ids = [item["identifier"] for item in results["result_set"]]
print(f"Found {len(pdb_ids)} Cryo-EM PDB IDs")

# Step 2: Download .pdb or .cif for each ID
for pdb_id in pdb_ids:
    url = f"https://files.rcsb.org/download/{pdb_id}.cif"
    out_path = os.path.join(OUTPUT_DIR, f"{pdb_id}.cif")

    try:
        file_resp = requests.get(url)
        file_resp.raise_for_status()
        with open(out_path, "wb") as f:
            f.write(file_resp.content)
        print(f"Downloaded {pdb_id}")
    except Exception as e:
        print(f"Failed to download {pdb_id}: {e}")
