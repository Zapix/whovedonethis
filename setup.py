from setuptools import setup, find_packages

setup(
    name="django-whovedonethis",
    version="0.0.9",
    author="Aleksandr Aibulatov",
    author_email="zap.aibulatov@gmail.com",
    description="Simple pluggable django application",
    license="BSD",
    url="https://github.com/Zapix/whovedonethis",
    keywords="django application, created by, mixins",
    package_dir={'whovedonethis': 'whovedonethis'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
    ],
    zip_safe=False
)
