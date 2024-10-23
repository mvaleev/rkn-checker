# rkn-checker

Check for an IP address within a RKN block list.

## Example Usage

### Help

```console
$ python3 ipcheck.py -h
usage: ipcheck.py [-h] -d <filename> -i <ip address>

RKN IP Checker

options:
  -h, --help            show this help message and exit
  -d <filename>, --data_file <filename>
                        CSV dump file from here https://github.com/zapret-info/z-i/blob/master/dump.csv.

  -i <ip address>, --ip_address <ip address>
                        IP address to check in dump.
```

### Install requirements

```console
$ pip3 install -r requirements.txt
```

### Download dump.csv

```console
$ python3 download_dump.py
```

### Check ip

```console
$ python3 ipcheck.py -d ./dump.csv -i 104.21.82.4
IP 104.21.82.4 banned.
```

