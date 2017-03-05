# Apple Health Data Exporter

This Python script takes a dump of Apple Health data (the `export.zip` file
generated through an Apple Health data export) and saves a subset of fields and
records to a [feather](https://github.com/wesm/feather) file. This can then be
read by both Python and R.

## Prerequisites

* [`feather-format`](https://github.com/wesm/feather)
* [`pandas`](http://pandas.pydata.org/)
* [`lxml`](http://lxml.de/index.html)

If you have [`conda`](https://conda.io/docs/) installed, you can install
prerequisites in a new environment by doing

```bash
conda env create -f environment.yml
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
  ```

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
   import feather
   data = feather.read_dataframe("data.feather")
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
