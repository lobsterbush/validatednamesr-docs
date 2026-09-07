"""Build an isolated documentation copy from pinned upstream code with local documentation overlays."""
from pathlib import Path
import shutil
import subprocess
import tempfile


def run(args: list[str], cwd: Path) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def main() -> None:
    cache = Path('.build')
    cache.mkdir(exist_ok=True)
    build = Path(tempfile.mkdtemp(prefix='site_', dir=cache))
    source = build / 'source'
    run(['git', 'clone', '--quiet', 'https://github.com/jaeyk/validatednamesr.git', str(source)], Path('.'))
    run(['git', 'checkout', '--quiet', '--detach', 'f80678c561256a4566898e514e516c265d308cdc'], source)
    if (source / 'docs').exists():
        shutil.move(str(source / 'docs'), str(build / 'upstream_docs'))
    shutil.copytree('site', source / 'pkgdown', dirs_exist_ok=True)
    shutil.copy2('site/_pkgdown.yml', source / '_pkgdown.yml')
    for help_file in Path('site/reference').glob('*.Rd'):
        shutil.copy2(help_file, source / 'man' / help_file.name)
    (source / 'man/figures').mkdir(exist_ok=True)
    shutil.copy2('site/figures/provenance.svg', source / 'man/figures/provenance.svg')
    script = source / 'build_docs.R'
    script.write_text('''# Render documentation without running network examples.
pkgdown::init_site()
pkgdown::build_home()
pkgdown::build_reference(examples = FALSE)
public <- c("index.html", "404.html", "authors.html", "LICENSE.html", "LICENSE-text.html")
pages <- list.files(here::here("docs"), pattern = "[.]html$", full.names = TRUE)
unlink(pages[!basename(pages) %in% public])
pkgdown::build_search()
file.create(here::here("docs", ".nojekyll"))
''')
    run(['Rscript', 'build_docs.R'], source)
    destination = Path('docs')
    # Preserve a backup of the last generated site before replacing it.
    if destination.exists():
        shutil.move(str(destination), str(build / 'previous_docs'))
    shutil.copytree(source / 'docs', destination)
    (destination / '.nojekyll').touch()
    print('Built docs/ from pinned upstream source.')


if __name__ == '__main__':
    main()
