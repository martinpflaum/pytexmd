project = 'My Project'
copyright = '2025, Author'
author = 'Author'
release = '1.0'

extensions = ['myst_parser',
              "sphinx_proof"]

templates_path = ['_templates']
exclude_patterns = []



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

import sphinx_proof.nodes
import sphinx_proof.proof_type
import sphinx_proof.directive
import sphinx_proof.domain
from docutils import nodes
from sphinx_proof.directive import ElementDirective


# --- paragraph ---

class paragraph_node(nodes.Admonition, nodes.Element):
    pass


class ParagraphDirective(ElementDirective):
    name = "paragraph"

# Patch all 4 locations so sphinx-proof fully recognises each custom type.
# Node classes live in proof_ext.py (a real importable module) so pickle can
# find them. ProofDomain.directives is built once at class-import time from
# PROOF_TYPES, so it must be patched explicitly.
_CUSTOM_TYPES = {
    "paragraph": (paragraph_node, ParagraphDirective),
    # "exercise": (exercise_node, ExerciseDirective),
}
for _name, (_node_cls, _directive_cls) in _CUSTOM_TYPES.items():
    sphinx_proof.nodes.NODE_TYPES[_name] = _node_cls
    sphinx_proof.proof_type.PROOF_TYPES[_name] = _directive_cls
    sphinx_proof.directive.DEFAULT_REALTYP_TO_COUNTERTYP[_name] = _name
    sphinx_proof.domain.ProofDomain.directives[_name] = _directive_cls

#prf_types = ["axiom", "theorem", "lemma", "algorithm", "definition", "remark", "conjecture", "corollary", "criterion", "example", "property", "observation", "proposition", "assumption", "notation"]

prf_realtyp_to_countertyp = {
    "paragraph": "theorem",
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
}

#math_number_all = True             # number *all* displayed equations
math_eqref_format = "({number})"   # how equation refs look

html_theme = 'furo'
html_static_path = ['_static']


#math_number_all = True             # number *all* displayed equations
math_eqref_format = "({number})"   # how equation refs look
numfig = True                      # enable section-prefixed numbering
math_numfig = True                 # apply section prefix to equations
numfig_secnum_depth = 2            # use # and ## levels (e.g. 1.2.3)

html_theme = 'furo'
html_static_path = ['_static']