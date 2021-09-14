Write the code corresponding to flake-8 or fail your unittests. 

We do not negotiate with poor formatted code

To install type 
```
pip install -e git+https://github.com/IlyaKozlov/csd.git#egg=csd
```

Define test class 
```python
import os
from typing import List

from style_test import StyleTest
class TestStyle(StyleTest):
    def get_files(self) -> List[str]:
        """
        return list of absolute path to every source file in your project
        """
        test_dir = os.path.dirname(__file__)
        source_dir = os.path.join(test_dir, "..", "src")
        result = []
        for directory in [test_dir, source_dir]:
            for file in os.listdir(directory):
                result.append(os.path.abspath(os.path.join(directory, file)))
        return result
```