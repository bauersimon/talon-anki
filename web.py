from os import path, listdir

import jinja2

TEMPLATE_VALUE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>talon-anki</title>
</head>

<body>
  <h1>talon-anki</h1>
  <hr>
  <h2>csv</h2>
  <ul>
  {% for c in csv %}
    <li>
      <a href="csv/{{c}}"> {{c}} </a>
    </li>
  {% endfor %}
  </ul>
  <h2>apkg</h2>
  <ul>
  {% for c in apkg %}
    <li>
      <a href="apkg/{{c}}"> {{c}} </a>
    </li>
  {% endfor %}
  </ul>
</body>
</html>
"""

environment = jinja2.Environment()
TEMPLATE = environment.from_string(TEMPLATE_VALUE)


def render_html(p: str) -> str:
    csv = [
        f
        for f in listdir(path.join(p, 'csv'))
    ]
    apkg = [
        f
        for f in listdir(path.join(p, 'apkg'))
    ]
    return TEMPLATE.render(csv=csv, apkg=apkg)


def save_html(d: str, p: str):
    with open(p, 'w')as f:
        f.write(d)


if __name__ == "__main__":
    save_html(render_html('decks'), path.join('decks', 'index.html'))
