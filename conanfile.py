from conans import ConanFile


class BoostMathConan(ConanFile):
    name = "Boost.Math"
    version = "1.66.0"
    requires = \
        "Boost.Level8Group/1.66.0@bincrafters/testing"
    lib_short_names = ["math"]
    is_header_only = False
    is_in_cycle_group = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-math"
    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Generator/1.66.0@bincrafters/testing"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    exports = "boostgenerator.py"

    def package_id(self):
        getattr(self, "package_id_after", lambda:None)()
    def source(self):
        self.call_patch("source")
    def build(self):
        self.call_patch("build")
    def package(self):
        self.call_patch("package")
    def package_info(self):
        self.call_patch("package_info")
    def call_patch(self, method, *args):
        if not hasattr(self, '__boost_conan_file__'):
            try:
                from conans import tools
                with tools.pythonpath(self):
                    import boostgenerator  # pylint: disable=F0401
                    boostgenerator.BoostConanFile(self)
            except Exception as e:
                self.output.error("Failed to import boostgenerator for: "+str(self)+" @ "+method.upper())
                raise e
        return getattr(self, method, lambda:None)(*args)
    @property
    def env(self):
        import os.path
        result = super(self.__class__, self).env
        result['PYTHONPATH'] = [os.path.dirname(__file__)] + result.get('PYTHONPATH',[])
        return result
    @property
    def build_policy_missing(self):
        return (getattr(self, 'is_in_cycle_group', False) and not getattr(self, 'is_header_only', True)) or super(self.__class__, self).build_policy_missing

    # END
