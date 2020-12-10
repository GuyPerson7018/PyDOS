# PyDOS
A DOS attack made with a mash up of the range attack and slow read. Takes down apache servers, or greatly increases loading time(more than five times)

wget before the attack - 46.8KB/s   in 1.9s

wget after the attack - 

11.6KB/s   in 7.7s

12.6KB/s   in 7.0s

16.3KB/s   in 5.5s

Note that I performed the attack with an external computer, to prevent network interference

Here are some error messages that appeared when I ran this attack on a locally hosted server:

Failed to accept a client (reason: Too many open files)

This attack should only work on Apache servers
