#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest
if __name__ == "__main__":
    pytest.main(["-v"])