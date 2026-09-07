# validatednamesr documentation

I maintain this documentation for `validatednamesr`, which I wrote with Jae Yeon
Kim. See the [package source](https://github.com/jaeyk/validatednamesr) and
[documentation](https://lobsterbush.github.io/validatednamesr-docs/).

Author of this documentation copy: Charles Crabtree.

We wrote every initial version ourselves, without AI. We've used AI only for
later updates and code fixes. The documentation records **Human – AI (editor) 👤✏️🤖**
under [The Latent Review’s provenance standard](https://thelatentreview.com/provenance/).

## Requirements and replication

Use Python 3.10+, Git, R, pkgdown, here, and the package dependencies listed in
the upstream DESCRIPTION. From this repository root, run:

```sh
python3 01_build_site.py
```

The script builds from upstream commit `f80678c561256a4566898e514e516c265d308cdc`
in an isolated temporary directory. It applies the page content and function help from `site/`, keeps upstream R
code unchanged, and writes `docs/`. API and data-download examples are displayed but not executed.

GitHub Pages serves `docs/` from the main branch. Build locally and push the
rendered output.
