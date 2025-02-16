from setuptools import setup, find_packages

setup(
    name='video-processor-app',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A PyQt5 application for processing videos with audio commentary.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'PyQt5',
        'easyocr',
        'opencv-python',
        'moviepy',
        'torch',
        'TTS',
        'matplotlib',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'video-processor-app=main:main',
        ],
    },
)