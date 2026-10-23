"""Behavior checks for the skill's deterministic image helpers."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def run_script(name: str, *args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / name), *(str(arg) for arg in args)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


class ImageHelperTests(unittest.TestCase):
    def test_reference_is_scaled_without_overwriting(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.png"
            output = Path(directory) / "reference.png"
            Image.new("RGB", (300, 150), "white").save(source)

            first = run_script("prepare_reference.py", source, output, "--max-long-side", 128)
            self.assertEqual(first.returncode, 0, first.stderr)
            with Image.open(output) as image:
                self.assertEqual(image.size, (128, 64))

            second = run_script("prepare_reference.py", source, output)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("already exists", second.stderr)

    def test_final_image_is_exact_size_without_overwriting(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.png"
            output = Path(directory) / "final.png"
            Image.new("RGB", (300, 150), "black").save(source)

            first = run_script("finalize_ratio.py", source, output, "--size", "150x60")
            self.assertEqual(first.returncode, 0, first.stderr)
            with Image.open(output) as image:
                self.assertEqual(image.size, (150, 60))

            second = run_script("finalize_ratio.py", source, output, "--size", "150x60")
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("already exists", second.stderr)

    def test_validator_rejects_wrong_size_and_background(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            image_path = Path(directory) / "dark.png"
            Image.new("RGB", (150, 60), "black").save(image_path)

            valid = run_script(
                "validate_output.py", image_path, "--size", "150x60", "--background", "dark"
            )
            wrong_size = run_script("validate_output.py", image_path, "--size", "160x60")
            wrong_background = run_script(
                "validate_output.py", image_path, "--size", "150x60", "--background", "light"
            )
            self.assertEqual(valid.returncode, 0, valid.stdout)
            self.assertEqual(wrong_size.returncode, 2)
            self.assertEqual(wrong_background.returncode, 3)


if __name__ == "__main__":
    unittest.main()
