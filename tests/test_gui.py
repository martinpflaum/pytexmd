import queue
import unittest
from unittest.mock import patch

from app.gui import _QueueWriter, main, parse_mathjax_macros
from pytexmd.sphinx_doc import DEFAULT_MATHJAX_MACROS


class GuiTests(unittest.TestCase):
    def test_default_mathjax_macros_are_editable_json(self):
        import json

        self.assertEqual(
            parse_mathjax_macros(json.dumps(DEFAULT_MATHJAX_MACROS)),
            DEFAULT_MATHJAX_MACROS,
        )

    def test_mathjax_macros_must_be_an_object(self):
        with self.assertRaises(ValueError):
            parse_mathjax_macros("[]")

    def test_queue_writer_forwards_build_output(self):
        events = queue.Queue()
        writer = _QueueWriter(events)

        length = writer.write("building\n")

        self.assertEqual(length, 9)
        self.assertEqual(events.get_nowait(), ("log", "building\n"))

    def test_missing_tkinter_has_linux_install_guidance(self):
        with patch("app.gui.tk", None), self.assertRaises(SystemExit) as error:
            main()

        self.assertIn("python3-tk", str(error.exception))


if __name__ == "__main__":
    unittest.main()
