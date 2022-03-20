# Apple Health Exporter

This Python 3 module takes a dump of Apple Health data (the `export.zip` file
generated through an Apple Health data export) and saves a subset of fields and
records to a [feather](https://github.com/wesm/feather) file. This can then be
read by both Python and R.

## Getting started

The package can be used either as an executable module, or as an importable library.

First, install from PyPI (preferably in a new virtual environment):

```bash
# optional: create virtualenv within directory to avoid polluting system Python
python -m venv .venv
source .venv/bin/activate

pip install apple-health-exporter
```

This will also install the following dependencies:

- [`pandas`](http://pandas.pydata.org/)
- [`pyarrow`](https://pypi.org/project/pyarrow/)
- [`lxml`](http://lxml.de/index.html)

### Installing Feather in R

If you'd like to do data analysis on the generated data file in R, then you'll
need the feather package:

```r
install.packages("feather")
```

## Usage

1. Export Apple Health data from within the Health app.

![click on "user" icon and then on "export health data"](images/exporting.png)

2. Pick a location (I usually export to Dropbox) and then run the script:

```bash
apple-health-exporter ~/Dropbox/export.zip ~/Downloads/data.feather
# alternative method:
python -m apple_health_exporter ~/Dropbox/export.zip ~/Downloads/data.feather

# Specify XML file name in case zip file has been renamed
apple-health-exporter ~/Dropbox/export_renamed.zip ~/Downloads/data.feather --xml_file_name export.zip
```

> The export zip file contains an XML file containing
> actual data. By default, this name can be inferred
> from the stem of the zip file name (for example
> `export.zip` will contain a file named `export.xml`).
> However, if the zip file has been renamed, you may
> need to explicitly provide the name of the XML file
> with the `--xml_file_name` option.

3. Now you can load the data in either R or Python.

   In R:

   ```r
   library(feather)
   library(dplyr)
   data <- read_feather("~/Downloads/data.feather")
   data %>% group_by(type) %>% summarize(entries = n())
   ```

   ```
   # A tibble: 28 × 2
                                               type entries
                                             <chr>   <int>
   1     HKQuantityTypeIdentifierActiveEnergyBurned   84742
   2      HKQuantityTypeIdentifierAppleExerciseTime    5997
   3      HKQuantityTypeIdentifierBasalEnergyBurned   52477
   4      HKQuantityTypeIdentifierBodyFatPercentage      44
   5               HKQuantityTypeIdentifierBodyMass      84
   6          HKQuantityTypeIdentifierBodyMassIndex      40
   7         HKQuantityTypeIdentifierDietaryCalcium      84
   8   HKQuantityTypeIdentifierDietaryCarbohydrates      84
   9     HKQuantityTypeIdentifierDietaryCholesterol      84
   10 HKQuantityTypeIdentifierDietaryEnergyConsumed      84
   # ... with 18 more rows
   ```

   In Python:

   ```python
   import pandas as pd
   data = pd.read_feather("data.feather")
   data.groupby("type").size()
   ```

   ```
   type
   HKQuantityTypeIdentifierActiveEnergyBurned           84742
   HKQuantityTypeIdentifierAppleExerciseTime             5997
   HKQuantityTypeIdentifierBasalEnergyBurned            52477
   HKQuantityTypeIdentifierBodyFatPercentage               44
   HKQuantityTypeIdentifierBodyMass                        84
   HKQuantityTypeIdentifierBodyMassIndex                   40
   HKQuantityTypeIdentifierDietaryCalcium                  84
   HKQuantityTypeIdentifierDietaryCarbohydrates            84
   HKQuantityTypeIdentifierDietaryCholesterol              84
   HKQuantityTypeIdentifierDietaryEnergyConsumed           84
   HKQuantityTypeIdentifierDietaryFatMonounsaturated       84
   HKQuantityTypeIdentifierDietaryFatPolyunsaturated       84
   HKQuantityTypeIdentifierDietaryFatSaturated             84
   HKQuantityTypeIdentifierDietaryFatTotal                 84
   HKQuantityTypeIdentifierDietaryFiber                    84
   HKQuantityTypeIdentifierDietaryIron                     84
   HKQuantityTypeIdentifierDietaryPotassium                84
   HKQuantityTypeIdentifierDietaryProtein                  84
   HKQuantityTypeIdentifierDietarySodium                   84
   HKQuantityTypeIdentifierDietarySugar                    84
   HKQuantityTypeIdentifierDietaryVitaminC                 84
   HKQuantityTypeIdentifierDistanceCycling                 21
   HKQuantityTypeIdentifierDistanceWalkingRunning       49111
   HKQuantityTypeIdentifierFlightsClimbed                 562
   HKQuantityTypeIdentifierHeartRate                    26502
   HKQuantityTypeIdentifierHeight                          41
   HKQuantityTypeIdentifierLeanBodyMass                    39
   HKQuantityTypeIdentifierStepCount                     8810
   dtype: int64
   ```

## Examples

Some examples using this data export can be found in my
[apple-health-examples](https://github.com/mganjoo/apple-health-examples) repo.

## Contributing

This package uses [Poetry](https://python-poetry.org) for package management.

To build and test the package locally, check out the repo and:

1. Install Poetry (one-time) using one of the methods on the [Installation](https://python-poetry.org/docs/#installation) page.

2. Install all dependencies (automatically creates a virtual environment):

```
poetry install
```

3. Make changes, and test using the following commands:

```bash
# Type checking
poetry run mypy .
# Linting
poetry run flake8 apple_health_exporter/
# Formatting
poetry run black .
```

## Contributors

Thanks to contributors who have helped improve this package!

- [@aapris](https://github.com/aapris)
- [@brunoamaral](https://github.com/brunoamaral)
- [@Jeanselme](https://github.com/Jeanselme)
