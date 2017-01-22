import argparse
"""Used to parse command line arguments"""
import urllib3


class HeaderExpectedItem:
    def __init__(self, header, expected, message, risk):
        self.header = header
        self.expected = expected
        self.message = message
        self.risk = risk

    def printitem(self):
        print(self.header)
        print(self.expected)
        print(self.message)
        print(self.risk)


def valid_url(url):
    print('Validating Url: ' + url )
    return True

def scan_url(url, expectedHeaders):
    print('Scanning Url' + url)
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    print('---Response---')
    print(response.status)
    print(response.headers)



def initialize():
    """Used the guidance provided here https://blog.appcanary.com/2017/http-security-headers.html to create this list"""
    headers = []
    headers.append(HeaderExpectedItem('X-Frame-Options', 'testing2', 'testing3', 'testing4'))
    headers.append(HeaderExpectedItem('X-XSS-Protection', 'testing2', 'testing3', 'testing4'))
    headers.append(HeaderExpectedItem('Content-Security-Policy', 'testing2', 'testing3', 'testing4'))
    headers.append(HeaderExpectedItem('Strict-Transport-Security', 'testing2', 'testing3', 'testing4'))
    headers.append(HeaderExpectedItem('Public-Key-Pins', 'testing2', 'testing3', 'testing4'))
    headers.append(HeaderExpectedItem('X-Frame-Options', 'testing2', 'testing3', 'testing4'))
    headers.append(HeaderExpectedItem('X-Content-Type-Options', 'testing2', 'testing3', 'testing4'))
    headers.append(HeaderExpectedItem('Referrer-Policy', 'testing2', 'testing3', 'testing4'))
    headers.append(HeaderExpectedItem('Set-Cookie', 'testing2', 'testing3', 'testing4'))
    return headers
    

def main():
    """Application entry point"""
    parser = argparse.ArgumentParser(description='Http Header Security Scanner')
    parser.add_argument('-s', '--scan', action='store_true', help='Scans the specified url')
    parser.add_argument('-u', '--URL', help='The Url to be checked')
    args = parser.parse_args()

    if args.scan:
        expectedheaders = initialize()
        valid_url(args.URL)
        scan_url(args.URL, expectedheaders)

        for item in expectedheaders:
            print(item.printitem())


    else:
        print('Not going to scan')


if __name__ == '__main__':
    main()
