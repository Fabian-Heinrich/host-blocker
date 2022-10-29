# Host Blocker

Host blocker for Windows. Requires administration rights. 
Rewrites hosts file based on block list. Redirects specified hosts to 127.0.0.1. Allows to manually activate and deactivate block list.

Create file with hosts to block. Add a new line for each host.

Enable blocklist:

```
main.py --blocklist blocklist.txt --enable
```

Disable blocklist:

```
main.py --blocklist blocklist.txt --disable
```