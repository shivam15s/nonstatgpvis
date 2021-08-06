import os
import re

os.system(
    "jupyter nbconvert index_dev.ipynb  --TemplateExporter.exclude_input=True --to html")
path = 'index_dev.html'
save_path = 'index.html'
with open(path, 'r') as f:
    data = f.read()
data = re.sub('Out\[\d+\]:', '', data)
data = re.sub('<title>.*</title>',
              '<title>Active Learning: A Visual Tour</title>', data)
with open(save_path, 'w') as f:
    f.write(data)
