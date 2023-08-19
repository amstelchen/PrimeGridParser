# PrimeGridParser

Show a PrimeGrid user's badges.

```
usage: PrimeGridParser [-h] [-t] [-j] [-s] [-d] [-c] [-n] [-q] [-v] userid

Show a PrimeGrid user's badges.

positional arguments:
  userid         PrimeGrid user-id

options:
  -h, --help     show this help message and exit
  -t, --csv      display as comma-separated list
  -j, --json     display as JSON
  -s, --single   use singleborder lines
  -d, --double   use double border lines
  -c, --color    use colorized output
  -n, --none     suppress (none) output
  -q, --quiet    suppress debug timing output
  -v, --version  show program's version number and exit
```
This will result in a table like below:

```
$ PrimeGridParser 130644 -s
┌────────────────────────────────────────────┬────────────────┬───────────────┬─────────────────────────────┬────────────┬──────────────────────────────┐
│                  Project                   │ Current Credit │ Current Badge │ Credit Level for Next Badge │ Next Badge │ Credit Needed for Next Badge │
├────────────────────────────────────────────┼────────────────┼───────────────┼─────────────────────────────┼────────────┼──────────────────────────────┤
│                  SGS LLR                   │    217,577     │     Silver    │           500,000           │    Gold    │           282,423            │
│                 PPS Sieve                  │    889,040     │      Gold     │          1,000,000          │  Amethyst  │           110,960            │
│ Sierpinski (ESP/PSP/SoB) Sieve (suspended) │       5        │     (none)    │                             │            │                              │
│                    AP27                    │     3,682      │     (none)    │            10,000           │   Bronze   │            6,318             │
└────────────────────────────────────────────┴────────────────┴───────────────┴─────────────────────────────┴────────────┴──────────────────────────────┘

```
By omitting the -s and -d options, the table will be printed in the default simple ASCII format. By cutting the first and last line from the output, the table is markdown-ready.