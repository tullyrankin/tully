# tully
Tully is a command-line tool for common tasks.

## Installation

```
pip install tully
```

## Modules

### COVID19

Retrieve COVID19 cases for today.
```bash
tully covid19 cases_by_date
```

Retrieve COVID19 cases for a given date.
```bash
tully covid19 cases_by_date --date=05-06-2020
```

### Networking

Get IP Address for a given hostname
```bash
tully network host <hostname>
```

Get Default IP Address
```bash
tully network ip 
```

Display Network Cards
```bash
tully network nics
```
