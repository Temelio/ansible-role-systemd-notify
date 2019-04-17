"""
Role tests
"""

import pytest
import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('item_type,path,user,group,mode', [
    ('file', '/etc/systemd/system/notify@.service', 'root', 'root', 0o644),
    ('file', '/usr/local/bin/systemd-email', 'root', 'root', 0o755),
])
def test_paths_properties(host, item_type, path, user, group, mode):
    """
    Test systemd notify files properties
    """

    current_item = host.file(path)

    if item_type == 'directory':
        assert current_item.is_directory
    elif item_type == 'file':
        assert current_item.is_file

    assert current_item.exists
    assert current_item.user == user
    assert current_item.group == group
    assert current_item.mode == mode


def test_contains(host):
    current_item = host.file("/etc/systemd/system/sshd.service")

    assert current_item.contains("OnFailure=notify@%n")
