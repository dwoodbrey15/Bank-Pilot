from pathlib import Path
root = Path(__file__).resolve().parent
page = root / "index.html"
html = page.read_text()
start = html.index("function bankEngine()")
end = html.index("</script>", start)
page.write_text(html[:start] + (root / "engine.js").read_text() + html[end:])
