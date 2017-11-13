# apichallenge

## /towns - Returns a list of towns

Provides acces to a list of french towns.
Available options:
* ordering=<any_field>
* Filtering:
    * <any_field>=<value>
    * 'population' and 'department_code' accept '__lt' or '__gt' suffixes for lower/greater than
    * 'town_name' accepts '__icontains' for case insensitive sub-strings

## /aggs - Returns aggregation results on towns populations

Returns the count of towns and their minimum, maximum, and average population.
This can be applied to a sub-set of towns, using a filter based on any field and comparison suffixes specified in the Django [documentation](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups).

## Usage

Launch the application using command line 'docker build . && docker run'.