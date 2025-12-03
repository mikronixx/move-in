# move-in

A **Platform/SRE move-in kit** with dotfiles and Python helpers.  

this repository is **actively maintained** and designed for others to copy, adapt, and extend.

## Why?

I reuse this stuff constantly. Putting it in one repo saves me time. Maybe it helps someone else too.

## Usage 

Clone and copy what you need:

```bash
git clone https://github.com/mkrohn-repo/move-in.git
#or
git clone git@github.com:mkrohn-repo/move-in.git
```

## What's Inside:

### [`dotfiles`](./dotfiles)
**Platform/SRE toolbox — dotfiles**  
- zsh configuration with sample aliases and pyenv setup you can toggle on/off  
- sample git, vim, and bash profiles  
- **Note:** automation doesn’t auto-rename files — shells are personal. Use what fits.


### [`useful_python`](./useful_python)
**Platform/SRE toolbox — Python helpers**  
- **boto3**: reusable for AWS sessions, pagination, and common tasks
- **requests**: wrappers for handling HTTP requests
- **requests_v2**: Improved HTTP request wrappers with timeouts, tests, typing and docstrings.

## Roadmap
- Add bearer token and retry support to HTTP(S) request functions 
- Expand boto3 session/pagination into a reusable module  
- Grow test coverage for all new functions