# move-in

A **Platform/SRE move-in kit** with dotfiles and Python helpers.

this repository is **actively maintained** and designed for others to copy, adapt, and extend.

## Why?

I reuse this stuff constantly. Putting it in one repo saves me time. Maybe it helps someone else too.

## Usage

A virtual environment is strongly recommended before cloning.

Clone into a directory named after your intended branch — this keeps your working tree and branch name in sync.


```bash
git clone https://github.com/mikronixx/move-in.git your_dir_name_which_should_be_a_branch_name_or_something_uniq_like_JIRA_number
#or
git clone git@github.com:mikronixx/move-in.git your_dir_name_which_should_be_a_branch_name_or_something_uniq_like_JIRA_number

cd your_dir_name_which_should_be_a_branch_name_or_something_uniq_like_JIRA_number

make install

git checkout -b your_dir_name_which_should_be_a_branch_name_or_something_uniq_like_JIRA_number

#do stuff

```



## What's Inside:

### [`dotfiles`](./dotfiles)
**Platform/SRE toolbox — dotfiles**
- zsh configuration with sample aliases and pyenv setup you can toggle on/off
- sample git, vim, and bash profiles
- **Note:** automation doesn’t auto-rename files — shells are personal. Use what fits.

### [`useful_python`](./useful_python)
**Platform/SRE toolbox — Python helpers**
- **boto3**: helpers for AWS sessions, pagination, and common tasks
- **requests**: HTTP request helpers with timeouts, tests, typing, and docstrings
- **requests_legacy**: deprecated wrappers retained for reference

## Roadmap
- Add bearer token and retry support to HTTP(S) request functions
- Expand boto3 session/pagination into a reusable module
- Grow test coverage for all new functions
# test
