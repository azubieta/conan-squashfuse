import os

from conans import ConanFile, CMake, tools


class SquashfuseTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ["pkg_config", "cmake"]
    build_requires = ["lzma/5.2.4@bincrafters/stable"]

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%sexample" % os.sep)
