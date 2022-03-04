# Apple Health Data Exporter

This Python 3 script takes a dump of Apple Health data (the `export.zip` file
generated through an Apple Health data export) and saves a subset of fields and
records to a [feather](https://github.com/wesm/feather) file. This can then be
read by both Python and R.

## Prerequisites

- [`pandas`](http://pandas.pydata.org/)
- [`pyarrow`](https://pypi.org/project/pyarrow/)
- [`lxml`](http://lxml.de/index.html)

You can install the above three packages (preferably in a new virtual
environment):

```sh
# optional: create virtualenv within directory to avoid polluting system Python
python -m venv .venv
source .venv/bin/activate

pip install pandas pyarrow lxml
```

You can also use one of the included `requirements.txt` file for `pip`:

```sh
pip install -r requirements.txt
```

### Installing Feather in R

If you'd like to do data analysis on the generated data file in R, then you'll
need the feather package:

```r
install.packages("feather")
```

## Steps

1. Export Apple Health data from within the Health app.

![click on "user" icon and then on "export health data"](images/exporting.png)

2. Pick a location (I usually export to Dropbox) and then run the script:

```bash
$ python export.py ~/Dropbox/export.zip ~/Downloads/data.feather

# Specify XML file name in case zip file has been renamed
$ python export.py ~/Dropbox/export_renamed.zip ~/Downloads/data.feather --xml_file_name export.zip
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
