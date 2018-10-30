from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext

from disttest import Test

ext_modules = [
    Extension('svmlight',
              ['src/svmlight.pyx',
               'lib/svm_common.c',
               'lib/svm_learn.c',
               'lib/svm_hideo.c'
               ],
              include_dirs=['lib'])]

setup(
    name='pysvmlight',
    cmdclass={'build_ext': build_ext,
              'test': Test},
    ext_modules=cythonize(ext_modules, compiler_directives={'language_level': '3str'}),
    options={'test': {'test_dir': ['test']}}
)
