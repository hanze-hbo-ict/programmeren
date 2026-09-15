"""Kleine uitvoerproef voor de verstrekte Mandelbrot-bibliotheek."""

from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile


ARCHIVE = Path(__file__).parents[1] / "source/problems/assets/mandelbrot.zip"


def test_mandelbrot_archive_writes_png():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory) / "mandelbrot"
        with zipfile.ZipFile(ARCHIVE) as archive:
            archive.extractall(directory)
        script = root / "smoke.py"
        script.write_text(
            "from png import PNGImage\n"
            "image = PNGImage(4, 3)\n"
            "image.plot_point(1, 2, (255, 0, 0))\n"
            "image.save_file('smoke.png')\n"
            "assert image.image_data[2][1] == (255, 0, 0)\n",
            encoding="utf-8",
        )
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
        output = root / "smoke.png"
        assert output.is_file()
        assert output.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
