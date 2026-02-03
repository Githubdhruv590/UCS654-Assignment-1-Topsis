# Package Description

_This package is built as a submission to_ [Assignment 1](https://github.com/psrana/Assignment-Topsis)

_Submitted by:_ **Dhruv Sethi (102303785)**

*Definition:*  
TOPSIS, acronym for Technique for Order Preference by Similarity to Ideal Solution, is a
multi-criteria decision-making (MCDM) method used to rank alternatives by selecting the
option that is closest to the ideal solution and farthest from the worst (negative ideal)
solution.

### Use this package as a [WebApp](https://github.com/Githubdhruv590/UCS654-Assignment-1-Topsis) here.

<br>

## Installation

Use the package manager pip to install Topsis-Dhruv-102303785

```bash
pip install Topsis-Dhruv-102303785
```

## ⚙️ **Usage**

```bash
topsis data.csv 1,1,1,1,1 +,+,-,+,+ result.csv
```                                                        
where,

data.csv is your input file

Weights to be assigned to each feature

Impacts to optimize each feature (+: Maximize, -: Minimize)

Output file path to save the results

<br>

## 🪴 Example

### Input Dataset (`data.csv`)

| Fund Name | P1 | P2 | P3 | P4 | P5 |
|----------|----|----|----|----|----|
| M1 | 0.72 | 0.54 | 4.1 | 43.2 | 12.05 |
| M2 | 0.69 | 0.51 | 3.6 | 59.8 | 15.92 |
| M3 | 0.67 | 0.44 | 5.0 | 62.1 | 17.10 |
| M4 | 0.78 | 0.61 | 3.9 | 41.4 | 11.80 |
| M5 | 0.83 | 0.68 | 5.4 | 39.6 | 11.35 |
| M6 | 0.80 | 0.65 | 5.6 | 55.9 | 15.88 |
| M7 | 0.86 | 0.74 | 6.5 | 52.3 | 14.70 |
| M8 | 0.92 | 0.85 | 5.7 | 66.2 | 18.30 |

**Weights:** `1,1,1,1,1`  
**Impacts:** `+,+,-,+,+`

---

### Output after applying TOPSIS (`result.csv`)

| Fund Name | P1 | P2 | P3 | P4 | P5 | Topsis Score | Rank |
|----------|----|----|----|----|----|--------------|------|
| M1 | 0.72 | 0.54 | 4.1 | 43.2 | 12.05 | 0.3834 | 7 |
| M2 | 0.69 | 0.51 | 3.6 | 59.8 | 15.92 | 0.5435 | 2 |
| M3 | 0.67 | 0.44 | 5.0 | 62.1 | 17.10 | 0.4540 | 5 |
| M4 | 0.78 | 0.61 | 3.9 | 41.4 | 11.80 | 0.4385 | 6 |
| M5 | 0.83 | 0.68 | 5.4 | 39.6 | 11.35 | 0.3678 | 8 |
| M6 | 0.80 | 0.65 | 5.6 | 55.9 | 15.88 | 0.5044 | 3 |
| M7 | 0.86 | 0.74 | 6.5 | 52.3 | 14.70 | 0.4702 | 4 |
| M8 | 0.92 | 0.85 | 5.7 | 66.2 | 18.30 | 0.7073 | 1 |


## Notes

The package handles the following:
- Correct number of parameters (input file, weights, impacts, output file)
- Appropriate error messages for invalid inputs
- Handling of File Not Found exception
- Input file must contain three or more columns
- From second to last columns must contain numeric values only
- Number of weights, impacts and criteria columns must be the same
- Impacts must be either `+` or `-`
- Weights and impacts must be separated by commas

## License

[MIT License](https://github.com/Githubdhruv590/UCS654-Assignment-1-Topsis/blob/main/LICENSE)