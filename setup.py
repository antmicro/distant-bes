from setuptools import setup, find_packages

setuptools.setup(
        name="distant-bes",
        version="0.1",
        author="Adam Olech",
        author_email="aolech@antmicro.com",
        description="BES client",
        url="https://github.com/antmicro/distant-bes",
        packages=find_packages(),
        entry_points = {
            "console_scripts": [
                "distant-bes-cli = distantbes.cli:main",
                ]
            },
        install_requires=["protobuf", "grpcio", "termcolor", "requests"],
        python_requires='>=3.6',
        )

