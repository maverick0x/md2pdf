from setuptools import find_packages, setup

setup(
    name="md2pdf",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["markdown", "weasyprint"],
    author="Maverick",
    description="A tool to convert markdown to PDF",
    python_requires=">=3.6",
)
