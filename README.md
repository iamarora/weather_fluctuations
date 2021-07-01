# Weather fluctuation data

## Run tests
- git clone this repo.
- Go to the data folder and unzip the data.csv.zip file.
- Run command 
  > python -m unittest tests/test_weather.py

### Context/Thought process
- Didn't optimize for performance. It does take up a few gigs of RAM to run.
- Stayed away from all 3rd party packages.
- There's lack of exception handling and negative test cases, aimed for correctness for the current dataset. If the dataset changes exception handling might become important.
