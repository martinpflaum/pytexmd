# TikZ Example

A citation example: {cite}`BouGTC1-4`.


A simple node diagram:

```{tikz}
   \draw[thick,rounded corners=8pt]
   (0,0)--(0,2)--(1,3.25)--(2,2)--(2,0)--(0,2)--(2,2)--(0,0)--(2,0);
```

A commutative square using `tikz-cd`:

::::{prf:paragraph}
This is a test paragraph rendered via the `prf:paragraph` directive.
::::

::::{prf:theorem_and_definition}
This is a test remark rendered via the `prf:Remarks` directive.
::::

## References

```{bibliography}
```
