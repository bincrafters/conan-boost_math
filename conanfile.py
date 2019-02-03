#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostMathConan(base.BoostBaseConan):
    name = "boost_math"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_math"
    lib_short_names = ["math"]
    cycle_group = "boost_cycle_group_b"
    b2_requires = ["boost_cycle_group_b"]
