# gabors

Repository for gabor filter setup.

* `parsed_data/` is in the format (image left, image right) : -5 to 5 (with negative numbers meaning image on right is stronger, positive meaning image on left is stronger)

* `parsed_avg/averages.txt` is in the format (image number : average strength)

* `results_parser.py` takes the raw data and creates individual subject files (stored within parsed data/)

* `parse_avg.py` creates the `averages.txt` file from the `parsed_data/` directory.

* `gabor_final.py` creates a series of gabor filters (https://en.wikipedia.org/wiki/Gabor_filter). Gabor filters 
are used as a proxy for simple V1 receptive fields. This code was adapted from David Mely, Serre Lab.
