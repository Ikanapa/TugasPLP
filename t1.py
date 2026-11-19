import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

potongan = {
    "fungsi": b"def sapa(nama):\n    return nama\n",
    "if_else": b'if umur >= 17:\n    print("dewasa")\nelse:\n    print("anak")\n',
    "kelas": b'class Mahasiswa:\n    def halo(self):\n        return "hai"\n',
    "rusak": b"def sapa(nama)\n    return nama\n",
    "rusak2": b'print("halo"\n',
}

for nama, kode in potongan.items():
    tree = parser.parse(kode)
    print(f"=== {nama} ===")
    print(tree.root_node)
    print()

# Tahap 4
tree = parser.parse(potongan["fungsi"])
fn = tree.root_node.children[0]

print("=== anak function_definition ===")
for c in fn.children:
    print(c.type, "bernama" if c.is_named else "anonim")

print("\n=== anak parameters ===")
params = fn.child_by_field_name("parameters")
for c in params.children:
    print(c.type, "bernama" if c.is_named else "anonim")

print("\n=== anak return_statement ===")
ret = fn.child_by_field_name("body").children[0]
for c in ret.children:
    print(c.type, "bernama" if c.is_named else "anonim")

print("\n=== anak comparison_operator (dari if_else) ===")
tree_if = parser.parse(potongan["if_else"])
cond = tree_if.root_node.children[0].child_by_field_name("condition")
for c in cond.children:
    print(c.type, "bernama" if c.is_named else "anonim")

print("\n=== children vs named_children (function_definition) ===")
print("children      :", [c.type for c in fn.children])
print("named_children:", [c.type for c in fn.named_children])