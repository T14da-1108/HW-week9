## JSON TO CSV CONVERTER (3 POINTS)

`json` `csv` `file conversion`

### Task

Write a function that converts a JSON file to a CSV file.
It accepts the name of a JSON file and a name of CSV file
to be produced from the former. You can assume
that the input JSON file always exists and it is correct, 
so you do not need to handle edge cases such as lack of 
permissions to read/write, JSON file not being correct etc. etc.

The JSON file contains a list of records, where each record is a dictionary with the same set of keys.

```json
[
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Jane",
        "age": 25,
        "city": "San Francisco"
    },
    {
        "name": "Tom",
        "age": 32,
        "city": "Chicago"
    }
]
```

Example:
```python
>>> json_to_csv('records.json', 'records.csv')
```

The resulting CSV file should look like this:

```csv
name,age,city
John,30,New York
Jane,25,San Francisco
Tom,32,Chicago
```

**Important**: there are many ways to implement this
but we ask you to NOT spend time on
writing your own parsers. Instead, you
can use built-in `csv` and `json` libraries
or something similar from `pandas`.

### About the Task

This task involves the practical application of file format conversion, which is a common requirement in data processing and manipulation (e.g. Kaggle datasets are usually in CSV format). It helps to understand the structure of JSON and CSV files and how to convert data between these two popular formats.

JSON and CSV are widely used data formats, I recommend you to read about them (e.g. [here](https://devforid.medium.com/the-basics-of-json-a-7794b2d3fa5f) or on YouTube) to understand their structure and how they are used in real-world applications.
