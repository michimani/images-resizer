image-resizer
===
This is a simple script that resize image and out put some kinds of size image.

# Runtime
Python 3.x

# Usage
1. This scrpit uses Pillow library.

```
pip3 install Pillow
```

2. Create `resize_manifest.json`. In this file, set the name, size and alpha channel of the resized output.

```
cp resize_manifest.sample resize_manifest
```

3. Run this script.

```
python resize.py base_image.png
```

Resized images will created in `dist` directly with sub directly named UNIX timestamp.

```
./dist
└── 1559903048
    ├── android-chrome-192x192.png
    ├── android-chrome-512x512.png
    ├── apple-touch-icon-120x120.png
    ├── apple-touch-icon-152x152.png
    ├── apple-touch-icon-180x180.png
    ├── apple-touch-icon-180x76.png
    ├── apple-touch-icon-60x60.png
    ├── apple-touch-icon.png
    ├── favicon-16x16.png
    ├── favicon-32x32.png
    ├── msapplication-icon-144x144.png
    └── mstile-150x150.png
```