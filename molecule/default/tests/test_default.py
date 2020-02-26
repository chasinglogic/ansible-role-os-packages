import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_generic_packages_installed(host):
    assert host.package("git").is_installed
    assert host.package("gcc").is_installed


def only_on(os):
    if not isinstance(os, list):
        os = [os]

    def decorator(fn):
        def wrapper(host):
            facts = host.facter()
            if facts["operatingsystem"] in os:
                return fn(host)
            return None

        return wrapper

    return decorator


@only_on(["Debian", "Ubuntu"])
def test_apt_packages_installed(host):
    assert host.package("g++").is_installed


@only_on("Arch")
def test_pacman_packages_installed(host):
    assert host.package("gcc-d")
