import sys

from __init__ import create_app

app = create_app()
print(app.instance_path)

print(sys.prefix)