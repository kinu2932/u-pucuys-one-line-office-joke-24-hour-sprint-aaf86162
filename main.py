import os

JOKE = "My visitor badge says GUEST \u2014 the only honest job title here, and it expires at 6 p.m."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
print(JOKE)
