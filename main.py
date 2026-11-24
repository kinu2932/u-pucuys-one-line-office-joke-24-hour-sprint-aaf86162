import os

JOKE = "I put 'proficient in Excel' on my résumé — my whole job is now one spreadsheet called FINAL_v27 that nobody dares to open."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
print(JOKE)
