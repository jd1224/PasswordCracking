# PasswordCracking
Password cracking tools and word lists

This program will crack cisco type5 passwords or any salted md5 hash as long as you have the salt.
Some word lists such as the popular ROCKYOU word list will not properly ingest as they produce an 
unrecognized character error.  I will work on the fix once I have a bit more time, but it hangs at
the for loop which reads in the file, so I cannot simply pass it by.

Syntax python type5crack.py <salted hash> <path to word list>
