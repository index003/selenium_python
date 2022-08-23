import unittest

# 默认test开头的py文件
# suite = unittest.TestLoader().discover("../cases")
# 这种也是默认的
suite = unittest.defaultTestLoader.discover("../cases")

# 指定tp开头的py文件
# suite = unittest.TestLoader().discover("../cases", pattern="tp*.py")

unittest.TextTestRunner().run(suite)

