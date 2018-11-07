#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostMathConan(base.BoostBaseConan):
    name = "boost_math"
    url = "https://github.com/bincrafters/conan-boost_math"
    lib_short_names = ["math"]
    cycle_group = "boost_level8group"    
    b2_requires = [
        "boost_level8group",
    ]


