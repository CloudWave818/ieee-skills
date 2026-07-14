# Compile Debug

Use the first real error, not the final cascade. Check missing braces, undefined commands, missing packages, package conflicts, duplicate labels, and broken bibliography runs.

Typical sequence:

```text
pdflatex -> bibtex -> pdflatex -> pdflatex
```

or the venue/compiler-specific equivalent.
