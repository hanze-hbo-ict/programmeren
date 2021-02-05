import os
import re
import glob
from pathlib import Path


text = """
one line

second line

:::{admonition,tip} The title
Tip text
:::

third line

  :::{admonition,warning} Opmerking
  Deze code werkt niet in GlowScript, maar er zitten wel een paar handige ideeën in.
  :::
"""

pattern = re.compile(r"(?P<prefix>\s*):::{admonition,\s*(?P<class>\w+)}\s*(?P<title>.+)")


def clean_text(text: str) -> str:
    lines = []
    for line in text.split("\n"):
        if match := pattern.match(line):
            prefix = match.group('prefix')
            title = match.group('title')
            klass = match.group('class')

            out = f"{prefix}:::{{admonition}} {title}\n"
            out += f"{prefix}:class: {klass}\n"
        else:
            out = line
        lines.append(out)

    return "\n".join(lines)

print(clean_text(text))
exit()

dirs = ["about", "class", "examples," "practice", "problems", "projects", "readings", "support"]

for dir in dirs:
    for dir_name, subdirs, files in os.walk(dir):
        for filename in files:
            if filename.endswith(".md"):
                file = Path(dir_name) / filename
                with file.open() as handle:
                    text = handle.read()

                text = clean_text(text)

                with file.open("w") as handle:
                    handle.write(text)