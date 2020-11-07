import requests
import hashlib
import sys


def get_data_frm_api(password_hash_character):
    url = 'https://api.pwnedpasswords.com/range/' + password_hash_character
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code} , check api')
    return res


def get_password_hash_value(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    sha_first5, tail = sha1password[:5], sha1password[5:]
    response = get_data_frm_api(sha_first5)
    return get_password_leaks(response, tail)


def get_password_leaks(response, password_hash_tail):
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == password_hash_tail:
            return count
    return 0


def main(args):
    for password in args:
        count = get_password_hash_value(password)
        if count:
            print(f'Your password {password} found {count} times')
        else:
            print(f'Your password {password} has NOT found')
    return 'Done!!!'


main(sys.argv[1:])
