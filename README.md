# Password Evaluator

This is a utility program that evaluates a list of passwords based on the following criteria
- Passwords must be at least 8 characters long
- Passwords must be at most 64 characters long
- Passwords must only contain [ASCII characters](https://ascii.cl/)
- Passwords cannot match a list of common passwords

## How to run

```git clone``` the repo

Make sure the file is executable

```chmod +x password_evaluator.py```

Pass in a newline-separated file of common passwords to stdin and a newline-separated file of passwords to check
```cat common-passwords.txt | ./password_evaluator.py passwords-to-test.txt```

A list of common passwords is provided in `input_passwords.txt` (sourced from a [list of common passwords](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/10_million_password_list_top_100000.txt)) but any newline-separated file can be provided.

## Next steps
- Add unit tests
	- Sample password file in test_passwords.txt
- Publish to a package manager
