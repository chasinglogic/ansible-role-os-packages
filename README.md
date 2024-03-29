Ansible role: os-packages
==================================

Install packages using variable files

[![GitHub Actions](https://github.com/chasinglogic/ansible-role-os-packages/workflows/Molecule%20Test/badge.svg)](https://github.com/chasinglogic/ansible-role-os-packages/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/chasinglogic/ansible-role-os-packages/workflows/Release/badge.svg)](https://github.com/chasinglogic/ansible-role-os-packages/actions?query=workflow%3A%22Release%22)

When and why to use this role
--------------------------

Inevitably when specifying configuration for multiple systems you will
need too install OS packages which don't need any setup beyond being
installed. Packages like `build-essential` or `gcc` for a build
server. It would be extremely cumbersome to create many bespoke single
package roles to install these files. Even if you don't go the "one
role per package" route, you can end up in a situation where you have
multiple bespoke packages lists spread throughout your roles that
handle the various details of different package managers and the lists
can be hard to cross-reference and keep up to date with each other.

This role allows you to centralize your package lists in variable
files so they are easily referenced with each other. It works in a 
heterogeneous environment, if you have `deb_packages` specified but
Ansible is not running against a host with apt installed the
`deb_packages` they will just be ignored. No when conditions necessary.

It is not recommend to use this role to install software that requires
lots of configuration or other setup. For example Nextcloud, NGINX, or
Apache would be poor choices to install this way because inevitably
they will need additional setup (SELinux, configuration, firewall
rules, etc.) and so should get their own dedicated role that handles
all the details of their deployment.

Role Variables
--------------

| Name                                  | Description                                                                                                                                                                    | Type    | Default | Required |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------:|:-------:|:--------:|
| packages\_apt\_globally\_update\_cache | Indicates if a global `apt update` should be run before package installs.                                                                                                      | boolean | true    | no       |
| generic_packages                      | A list of packages that will use the `package` module in Ansible. Many packages have generic and consistent names across Linux distributions. They should go in this variable. | list    | []      | no       |
| deb_packages                          | A list of packages that will use the correct packaging module based on the target system in Ansible for .deb packages                                                          | list    | []      | no       |
| rpm_packages                          | A list of packages that will use the correct packaging module based on the target system in Ansible for .rpm packages                                                          | list    | []      | no       |
| pacman_packages                       | A list of packages that will use the pacman Ansible packaging module                                                                                                           | list    | []      | no       |
| generic_package_specs                      | A list of package_specs that will use the `package` module in Ansible. Many packages have generic and consistent names across Linux distributions. They should go in this variable. | list    | []      | no       |
| deb_package_specs                          | A list of package_specs that will use the correct packaging module based on the target system in Ansible for .deb package_specs                                                          | list    | []      | no       |
| rpm_package_specs                          | A list of package_specs that will use the correct packaging module based on the target system in Ansible for .rpm package_specs                                                          | list    | []      | no       |
| pacman_package_specs                       | A list of package_specs that will use the pacman Ansible packaging module                                                                                                           | list    | []      | no       |


### Specifying Dependencies

The variables `generic_packages`, `deb_packages`, `pacman_packages`, and `rpm_packages`
are lists of packages to install. They are simply lists of strings
that will be ensure to be installed:

```yaml
generic_packages:
  - gcc
  - tmux
  - vim
```

### Use state's other than present

The variables `generic_package_specs`, `deb_package_specs`, etc. are
used for finer grained control over package installation. They can
also be used to remove packages, install the latest version, or get
specific listings of installed packages via loop variables in the
Ansible output. To use a package spec it looks like the following:

```yaml
generic_package_specs:
  - name: gcc
    state: latest
```

The `deb_package_specs` list additionally allows for the `update_cache` option to be specified:

```yaml
deb_package_specs:
  - name: gcc
    state: latest
    update_cache: yes
```

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: os-packages
```

License
-------

[Apache License](LICENSE)
