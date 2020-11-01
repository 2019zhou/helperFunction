from __future__ import print_function
import pickle

from pycparser import c_parser

text = r"""
void func{
for(int i = 0;i < N;i++){
		cin >> temp;
		stock.push_back(temp);
	}

	for(int i = 0;i < N;i++){
		cin >> temp;
		prices.push_back(temp);
	}
}       
"""

parser = c_parser.CParser()
ast = parser.parse(text)

# Since AST nodes use __slots__ for faster attribute access and
# space saving, it needs Pickle's protocol version >= 2.
# The default version is 3 for python 3.x and 1 for python 2.7.
# You can always select the highest available protocol with the -1 argument.

with open('ast', 'wb') as f:
    pickle.dump(ast, f, protocol=-1)

# Deserialize.
with open('ast', 'rb') as f:
    ast = pickle.load(f)
    ast.show()