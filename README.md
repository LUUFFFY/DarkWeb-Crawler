# DarkWeb-Crawler
This is a simple web crawler built with Python that is designed to search for specific data on .onion websites. It is a command-line tool that allows users to input a .onion URL and extracts emails, files, and keywords from the website. Which is currently under development, currently it can crawl normal http & https websites only.

Features:

Crawls websites up to a specified depth
Extracts emails, files, and keywords
Supports SOCKS5 proxy

Installation:

gitclone: https://github.com/LUUFFFY/DarkWeb-Crawler.git
unzip the file with: gunzip/unzip
cd file name
Install the required libraries: pip install requests bs4,
Run the script with the URL and depth as arguments: python3 darkweb_crawler.py <URL> <DEPTH>

Usage:

Input the URL of the .onion website you want to crawl.
Specify the depth of the crawl (optional, default is 2).
The crawler will output all emails, files, and keywords found on the website.

Examples:

Crawl the website http://example.onion/ up to a depth of 3: python3 darkweb_crawler.py http://example.onion/ 3,
Crawl the website http://example.onion/ up to the maximum depth with a SOCKS5 proxy: python3 darkweb_crawler.py http://example.onion/ 0 --proxy socks5://user:pass@host:port

Note:

This tool is for educational purposes only.
Using this tool for illegal activities is strictly prohibited.
The performance of this tool may vary depending on the website and internet connection.
Some websites may have restrictions that prevent crawlers from accessing their content.
License:

This project is licensed under the MIT License.

Disclaimer:

This project is not guaranteed to be completely accurate or up-to-date. The creators of this project are not responsible for any misuse or damage caused by this project. Use at your own risk.

