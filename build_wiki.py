import os
import sys
import urllib2
from shutil import copyfile

# urls to fetch files from
html_src = "https://raw.githubusercontent.com/Yonder-Dynamics/wiki-common/master/index.html"  # NOQA
css_src = "https://raw.githubusercontent.com/Yonder-Dynamics/wiki-common/master/index.css"  # NOQA
js_src = "https://raw.githubusercontent.com/Yonder-Dynamics/wiki-common/master/markdown.js"  # NOQA


def ensure_dirs(path):
    try:
        os.makedirs(path)
    except OSError:
        pass  # ignore path creation errors


def traverse(path, src_name, tree=None):
    if tree is None:
        tree = {}
    for file in os.listdir(path):
        if os.path.isdir(file):
            tree[file] = {}
            traverse(path + "/" + file, src_name, tree[file])
        else:
            if file.lower() == src_name.lower():
                tree["."] = file
    return tree


# step back into the
build_target = sys.argv[1]
build_src = sys.argv[2].lower()
html_base = build_target + "/html_base"


def build(tree, path, base):
    for subdir in tree:
        if subdir == ".":
            ensure_dirs(base)
            subpath = path + "/" + tree[subdir]
            copyfile(html_base, base + "/" + "index.html")
            copyfile(subpath, base + "/" + "wiki.md")
        else:
            build(tree[subdir], path + "/" + subdir, base + "/" + subdir)


ensure_dirs(build_target)

# download the webpage files
with open(html_base, "w") as html:
    raw = urllib2.urlopen(html_src).read().format(
        repo_name=os.environ['CI_PROJECT_NAME'],
    )
    html.write(raw)
with open(build_target + "/index.css", "w") as css:
    css.write(urllib2.urlopen(css_src).read())
with open(build_target + "/markdown.js", "w") as js:
    js.write(urllib2.urlopen(js_src).read())

tree = traverse(".", build_src)

print(tree)

build(tree, ".", build_target)
