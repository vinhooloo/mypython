import tree_sitter
#from tree_sitter import Language, Parser
from tree_sitter_languages import get_parser
import tree_sitter_python

from hello import hello_world 


# Create a parser
parser = get_parser("python")

# Parse some code
code = bytes("def hello():\n    str = \"foo\" \n print('Hello, world!')", "utf8")
tree = parser.parse(code)

# Explore the syntax tree
root_node = tree.root_node

print("Type of the root node:", root_node.type)
print("Children of the root node:")
#added hello_world for no good reason
hello_world("tree.py");
for child in root_node.children:
    print(f"- {child.type}")
    for nextchild in child.children:
        print(f"- {nextchild.text}")
        if ( nextchild.type == "identifier" ):
            print(f"** {nextchild.text}")
        if ( nextchild.type == "block" ):
            print(f"** {nextchild.text}")