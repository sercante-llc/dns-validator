#!/usr/bin/env python3
import argparse, dns.resolver
from time import sleep

parser = argparse.ArgumentParser(description='Given a list of domains, figure out which are valid and which are not')

parser.add_argument('--filename', type=str, help='File with domains, separated by line', required=True)
parser.add_argument('--interval', type=int, help='How long to sleep between DNS requests (in ms)', default=100, required=False)

args, unknownArgs = parser.parse_known_args()

print('Reading domains from file %s' % args.filename)

with open(args.filename, encoding='utf-8') as domainListFile:
    lines = domainListFile.readlines()
    print('Found %d domains to check' % len(lines))

    for line in lines:
        domain = line.strip()
        try:
            sleep(args.interval / 1000)
            result = dns.resolver.query(domain, 'MX')
            print('%s, Accept' % domain)
        except dns.resolver.NoAnswer:
            print('%s, Reject' % domain)
        except dns.resolver.NoNameservers:
            print('%s, Reject' % domain)
        except Exception:
            print('%s, Reject' % domain)

print('Processing complete')