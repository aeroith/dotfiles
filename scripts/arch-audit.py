#!/usr/bin/env python

import collections
import lxml.html
import requests
import pyalpm

WIKIPAGE_URL= "https://wiki.archlinux.org/api.php?format=json&action=parse&page=CVE&section=5"

print("Downloading CVE wiki page...")
r = requests.get(WIKIPAGE_URL)
r.raise_for_status()

json = r.json()
document = json["parse"]["text"]["*"]
doc = lxml.html.fromstring(document)

infos = collections.defaultdict(lambda: collections.defaultdict(list)) # whelp.

print("Parsing CVE list...")

for tr in doc.xpath('//table/tr'):
    tds = tr.xpath('td')
    if len(tds) == 0:
        continue

    texts = [el.text_content().strip() for el in tds]

    cves = filter(lambda x: x.startswith("CVE"), texts[0].split())
    pkgname = texts[1]
    version = texts[3]
    if version == "?" or version == "-":
        version = ""
    version = version.strip(' <=')
    status = texts[6]
    if status.startswith("Invalid") or status.startswith("Not affected"):
        continue
    infos[pkgname][version] += cves

print("Checking CVE list against local PKG DB...")

alpm_handle = pyalpm.Handle("/", "/var/lib/pacman")
alpmdb = alpm_handle.get_localdb()

for pkgname, info in infos.items():
    pkg = alpmdb.get_pkg(pkgname)
    if not pkg:
        continue # Not installed

    for cve_version, cves in info.items():
        if pyalpm.vercmp(pkg.version, cve_version) == -1:
            print("{} {} is vulnerable to {}".format(pkgname, pkg.version, ','.join(cves)))
