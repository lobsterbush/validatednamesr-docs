# validatednamesr documentation

Documentation maintained by Charles Crabtree for the R package authored by
Jae Yeon Kim and Charles Crabtree. Package source: https://github.com/jaeyk/validatednamesr

All initial versions were entirely human-created. AI was used only for later
updates and code fixes. The documentation records **Human – AI (editor) 👤✏️🤖**
under [The Latent Review’s provenance standard](https://thelatentreview.com/provenance/).

## Requirements and replication

Use Python 3.10+, Git, R, pkgdown, here, and the package dependencies listed in
the upstream DESCRIPTION. From this repository root, run:

```sh
python3 01_build_site.py
```

The script builds from upstream commit `f80678c561256a4566898e514e516c265d308cdc`
in an isolated temporary directory. It applies only documentation overlays
from `site/`, leaves upstream R code and reference entries unchanged, and writes
`docs/`. API and data-download examples are displayed but not executed.

GitHub Pages serves `docs/` from the main branch. Build locally and push the
rendered output; no GitHub Actions workflow is required.
