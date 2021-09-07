import os
from pprint import pprint

pprint(dict(os.environ))
print()

print(os.getenv('PERLBREW_HOME'), '\n')

