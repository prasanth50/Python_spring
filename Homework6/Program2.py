import  json,os
import shutil
PARENT_DIR = "outputquote"
with open("quote.json",'r') as quotes_file:
    data = json.load(quotes_file)
if os.path.exists(PARENT_DIR):
    shutil.RMTREE(PARENT_DIR)
os.path.exists(PARENT_DIR)
os.chdir(PARENT_DIR)
print("Created parent directory ", PARENT_DIR)
m=1
for node in data:
    corrected_author = node["author"] if node["author"] is not None else "unknown"
    dir_name = corrected_author.replace(" ", "_")
    os.chdir(dir_name)
    out = opwen("quote_{}.txt".format(n),"w")
    out.write(node["text"])
    out.write("\n\n")
    out.close()
    m=m+1
    os.chdir("..")