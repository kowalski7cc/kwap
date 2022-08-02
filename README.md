# KWAP

KWAP, pronounced "quap": Work with "Karaf Web APi"

## Prerequisites

You will need the `webconsole` feature started. You can install with the following command:

```sh
feature:install webconsole
```

## Usage

```text
usage: kwap [-h] --url url -u username -p password command ...

Work with Karaf Web API

positional arguments:
  command
    upload              Upload a bundle
    list                Show installed bundles

optional arguments:
  -h, --help            show this help message and exit
  --url url             Karaf Web API URL
  -u username, --username username
                        Karaf Web API username
  -p password, --password password
                        Karaf Web API password

Example: kwap --url localhost:8181 -u admin -p admin upload /path/to/bundle.jar
```
