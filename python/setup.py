from setuptools import setup
from setuptools_rust import Binding, RustExtension

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    rust_extensions=[RustExtension('sqlite_zstd.libsqlite_zstd',
        path='../Cargo.toml',
        binding=Binding.NoBinding,
        features=['build_extension'],
        py_limited_api=True,
    )],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
