# ansible-role-systemd-notify

[![Build Status](https://travis-ci.org/Temelio/ansible-role-systemd-notify.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-systemd-notify)

Install ansible-role-systemd-notify package.

## Requirements

This role requires Ansible 2.2, 2.3, 2.4
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Debian Stretch
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.ansible-role-systemd-notify }
```

## License

MIT

## Author Information

Lise Machetel (for Temelio company)
- https://temelio.com
- lise.machetel [at] temelio.com
