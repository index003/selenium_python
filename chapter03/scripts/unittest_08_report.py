import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./", pattern="unittest_08_skipcase.py")

with open("../report/report.html", "wb") as f:
    HTMLTestRunner(stream=f, verbosity=2, title="private title",
                   description="private desc").run(suite)

# with open("../report/report.txt", "w", encoding="utf-8") as f:
#     unittest.TextTestRunner(stream=f, verbosity=2).run(suite)
