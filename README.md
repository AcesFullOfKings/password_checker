# password_checker
Safely and securely checks a password to see if it appears in online leaks. 

Uses the pwnedpasswords.com api to check for a leaked password matching the entered query. 

Never sends any password over the network - only the first 5 characters of the hash of the password are sent.
