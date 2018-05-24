# ansible-role-systemd-notify

[![Build Status](https://travis-ci.org/Temelio/ansible-role-systemd-notify.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-systemd-notify)
[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-systemd-notify/master.svg?label=travis_master)](https://travis-ci.org/Temelio/ansible-role-systemd-notify)
[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-systemd-notify/develop.svg?label=travis_develop)](https://travis-ci.org/Temelio/ansible-role-systemd-notify)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-systemd-notify/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-systemd-notify/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-systemd-notify/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-systemd-notify/)

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
# Dependencies management
systemd_notify_use_ansible_galaxy_dependencies: True  # Use role dependencies in meta


service_name_to_modify: 'statsd'

notify_mail_config:
  - src: "{{ role_path }}/templates/systemd.email.j2"
    dest: '/usr/local/bin/systemd-email'
    owner: 'root'
    group: 'root'
    mode: '0755'

notify_service_systemd:
  - src: "{{ role_path }}/templates/notify.service.j2"
    dest: '/etc/systemd/system/notify@.service'
    owner: 'root'
    group: 'root'
    mode: '0644'
    options:
      Unit:
        Description: 'status email for %i to user'
        After: 'network.target'
      Service:
        Type: 'oneshot'
        ExecStart: '/usr/local/bin/systemd-email {{ notify_toEmail }} %i'
        User: 'nobody'
        Group: 'systemd-journal'

notify_fromEmail: 'toto@example.com'
notify_toEmail: 'toto@example.com'

systemd_service_states:
  - name: "{{ service_name_to_modify }}"
    state: "started"
    enabled: True
    daemon_reload: True

systemd_notify_options:
  - dest: "/etc/systemd/system/{{ service_name_to_modify }}.service"
    insertafter: '^Description'
    line: 'OnFailure=notify@%n'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.systemd-notify }
```

## License

MIT

## Author Information

Lise Machetel (for Temelio company)
- https://temelio.com
- lise.machetel [at] temelio.com
