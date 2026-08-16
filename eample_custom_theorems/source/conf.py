project = 'My Project'
copyright = '2025, Author'
author = 'Author'
release = '1.0'

extensions = ['myst_parser',
              "sphinx_proof",
              "sphinxcontrib.bibtex"
              ]

bibtex_bibfiles = ['FANCyProject.bib']
bibtex_default_style = 'unsrt'

templates_path = ['_templates']
exclude_patterns = []

tikz_proc_suite = 'GhostScript'

mathjax3_config = {
    "tex": {
        "macros": {
            "ltortoise": "\\unicode{x3014}",
            "rtortoise": "\\unicode{x3015}",
            "ltsbrak": ["\\mathopen{\\ltortoise\\mspace{1mu}}", 0],
            "rtsbrak": ["\\mathopen{\\mspace{1mu}\\rtortoise}", 0],
            "mathbbm": ["\\mathbb{#1}", 1],
            "widebar": ["\\overline{#1}", 1],
            "C": "\\mathbb{C}",
        }
    }
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import sphinx_proof.directive
import sphinx_proof.nodes
import sphinx_proof.domain
import sphinx_proof.proof_type

from docutils import nodes


# --- paragraph ---

class paragraph_node(nodes.Admonition, nodes.Element):
    pass

class ParagraphDirective(sphinx_proof.directive.ElementDirective):
    name = "paragraph"

class Remarks_node(nodes.Admonition, nodes.Element):
    pass

class RemarksDirective(sphinx_proof.directive.ElementDirective):
    name = "remarks"

class TheoremAndDefinitionDirective(sphinx_proof.directive.ElementDirective):  
    name = "theorem_and_definition"
    
# Patch all 4 locations so sphinx-proof fully recognises each custom type.
# Node classes live in proof_ext.py (a real importable module) so pickle can
# find them. ProofDomain.directives is built once at class-import time from
# PROOF_TYPES, so it must be patched explicitly.
_CUSTOM_TYPES = {
    "paragraph": (paragraph_node, ParagraphDirective),
    "remarks": (Remarks_node, RemarksDirective),
    "theorem_and_definition": (sphinx_proof.nodes.Node, TheoremAndDefinitionDirective),
    # "exercise": (exercise_node, ExerciseDirective),
}
for __name, (_node_cls, _directive_cls) in _CUSTOM_TYPES.items():
    _name = __name.lower()
    sphinx_proof.nodes.NODE_TYPES[_name] = _node_cls
    sphinx_proof.proof_type.PROOF_TYPES[_name] = _directive_cls
    sphinx_proof.directive.DEFAULT_REALTYP_TO_COUNTERTYP[_name] = _name
    sphinx_proof.domain.ProofDomain.directives[_name] = _directive_cls

#prf_types = ["axiom", "theorem", "lemma", "algorithm", "definition", "remark", "conjecture", "corollary", "criterion", "example", "property", "observation", "proposition", "assumption", "notation"]

prf_realtyp_to_countertyp = {
    "paragraph": "theorem",
    "remarks": "theorem",
    "axiom": "theorem",
    "theorem": "theorem",
    "lemma": "theorem",
    "algorithm": "theorem",
    "definition": "theorem",
    "remark": "theorem",
    "conjecture": "theorem",
    "corollary": "theorem",
    "criterion": "theorem",
    "example": "theorem",
    "property": "theorem",
    "observation": "theorem",
    "proposition": "theorem",
    "assumption": "theorem",
    "notation": "theorem",
    "theorem_and_definition": "theorem",
}

title_map = {
    "paragraph": "Paragraph",
    "remarks": "Remarks",
    "axiom": "Axiom",
    "theorem": "Theorem",
    "lemma": "Lemma",
    "algorithm": "Algorithm",
    "definition": "Definition",
    "remark": "Remark",
    "conjecture": "Conjecture",
    "corollary": "Corollary",
    "criterion": "Criterion",
    "example": "Example",
    "property": "Property",
    "observation": "Observation",
    "proposition": "Proposition",
    "assumption": "Assumption",
    "notation": "Notation",
    "theorem_and_definition": "Theorem and Definition",
}
if not hasattr(sphinx_proof.nodes, '_pytexmd_original_depart_enumerable_node'):
    sphinx_proof.nodes._pytexmd_original_depart_enumerable_node = sphinx_proof.nodes.depart_enumerable_node
    sphinx_proof.nodes._pytexmd_original_depart_unenumerable_node = sphinx_proof.nodes.depart_unenumerable_node
_original_depart_enumerable_node = sphinx_proof.nodes._pytexmd_original_depart_enumerable_node
_original_depart_unenumerable_node = sphinx_proof.nodes._pytexmd_original_depart_unenumerable_node

def _depart_enumerable_node(self, node: sphinx_proof.nodes.Node) -> None:
    countertyp = node.attributes.get("countertype", "")
    realtyp = node.attributes.get("realtype", "")
    display_name = title_map.get(realtyp, realtyp.title())
    _original_depart_enumerable_node(self, node)
    default_name = realtyp.title()
    if display_name == default_name:
        return
    number = sphinx_proof.nodes.get_node_number(self, node, countertyp)
    if isinstance(self, sphinx_proof.nodes.LaTeXTranslator):
        old_title = f"{default_name} {number}"
        new_title = f"{display_name} {number}"
    else:
        old_title = f"{sphinx_proof.nodes._(default_name)} {number} "
        new_title = f"{sphinx_proof.nodes._(display_name)} {number} "
    idx = sphinx_proof.nodes.list_rindex(self.body, old_title)
    self.body[idx] = new_title


def _depart_unenumerable_node(self, node: sphinx_proof.nodes.Node) -> None:
    realtyp = node.attributes.get("realtype", "")
    display_name = title_map.get(realtyp, realtyp.title())
    _original_depart_unenumerable_node(self, node)
    default_name = realtyp.title()
    if display_name == default_name:
        return
    if isinstance(self, sphinx_proof.nodes.LaTeXTranslator):
        old_title = default_name
        new_title = display_name
    else:
        old_title = f'<span class="caption-number">{sphinx_proof.nodes._(default_name)} </span>'
        new_title = f'<span class="caption-number">{sphinx_proof.nodes._(display_name)} </span>'
    idx = sphinx_proof.nodes.list_rindex(self.body, old_title)
    self.body[idx] = new_title


# Patch both the nodes module AND sphinx_proof's __init__ namespace.
# sphinx_proof/__init__.py does `from .nodes import depart_enumerable_node`
# which binds the name in its own globals. Sphinx's setup() looks up the name
# there, so patching only sphinx_proof.nodes has no effect.
sphinx_proof.nodes.depart_enumerable_node = _depart_enumerable_node
sphinx_proof.nodes.depart_unenumerable_node = _depart_unenumerable_node
sphinx_proof.depart_enumerable_node = _depart_enumerable_node
sphinx_proof.depart_unenumerable_node = _depart_unenumerable_node

#math_number_all = True             # number *all* displayed equations
math_eqref_format = "({number})"   # how equation refs look

html_theme = 'furo'
html_static_path = ['_static']


math_number_all = False
numfig = False
math_numfig = False

html_theme = 'furo'
html_static_path = ['_static']
