This code is built on top of
https://github.com/anibali/h36m-fetch


[Human3.6M](http://vision.imar.ro/human3.6m/description.php) is a 3D
human pose dataset containing 3.6 million human poses and corresponding
images. The scripts in this repository make it easy to download,
extract, and preprocess the images and annotations from Human3.6M.

**Please do not ask me for a copy of the Human3.6M dataset. I do not own
the data, nor do I have permission to redistribute it. Please visit
http://vision.imar.ro/human3.6m/ in order to request access and contact
the maintainers of the dataset.**

## Requirements

* Python 3
* [`axel`](https://github.com/axel-download-accelerator/axel)
* CDF (https://www.scivision.dev/spacepy-install-anaconda-python/)

## Usage

1. Firstly, you will need to create an account at
   http://vision.imar.ro/human3.6m/ to gain access to the dataset.
2. Once your account has been approved, log in and inspect your cookies
   to find your PHPSESSID.
3. Copy the configuration file `config.ini.example` to `config.ini`
   and fill in your PHPSESSID.
4. download_all.py -> extract_all.py -> video_to_images.py -> generate_labels.py


## License

The code in this repository is licensed under the terms of the
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Please read the
[license agreement](http://vision.imar.ro/human3.6m/eula.php) for the
Human3.6M dataset itself, which specifies citations you must make when
using the data in your own research. The file `metadata.xml` is directly
copied from the "Visualisation and large scale prediction software"
bundle from the Human3.6M website, and is subject to the same license
agreement.
