#!/usr/bin/env python3

import argparse
import sys

import urllib3

from kwap.kwap import fetch_bundle_list, upload_bundle

# YOLO
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():
    parser = argparse.ArgumentParser(
        description='Work with Karaf Web API',
        prog='kwap',
        epilog='Example: kwap --url localhost:8181 -u admin -p admin upload /path/to/bundle.jar'
    )

    subparsers = parser.add_subparsers(
        metavar='command', required=True, dest='command')
    upload_parser = subparsers.add_parser('upload', help='Upload a bundle')
    subparsers.add_parser(
        'list', help='Show installed bundles')

    parser.add_argument('--url', metavar='url', type=str,
                        required=True, help='Karaf Web API URL')
    parser.add_argument('-u', '--username', metavar='username',
                        type=str, required=True, help='Karaf Web API username')
    parser.add_argument('-p', '--password', metavar='password',
                        type=str, required=True, help='Karaf Web API password')
    upload_parser.add_argument('file', metavar='file', type=str, nargs='+',
                               help='Bundle file to upload')
    args = parser.parse_args()

    if args.command == 'upload':
        try:
            print(f'Uploading {len(args.file)} bundle(s)...')
            for file_path in args.file:
                upload_bundle(args.url, args.username,
                              args.password, file_path)
            print("Upload complete")
        except FileNotFoundError as error:
            print(f'File {error.filename} not found')
            sys.exit(1)
        except IOError as error:
            print(error)
            sys.exit(2)

    if args.command == "list":
        data = fetch_bundle_list(args.url, args.username, args.password)
        bundles = sorted(data['data'], key=lambda x: x['id'])
        for bundle in bundles:
            print("{:<5}| {:<10}| {:<20}| {:<30}".format(
                bundle['id'],
                bundle['state'],
                bundle['version'],
                bundle['name']
            ))


if __name__ == '__main__':
    main()
