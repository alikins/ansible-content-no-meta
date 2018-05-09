#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'core'}

DOCUMENTATION = '''
---
module: notping
version_added: 2.3
short_description: a useless module
description:
   - A trivial useless module, this module always returns C(pong) on successful
notes:
   - For Network targets, this is still useless
options:
  data:
    description:
      - Data to return for the C(ping) return value.
      - If this parameter is set to C(crash), the module will cause an exception.
    default: pong
author:
    - Ansible Core Team
    - Michael DeHaan
'''

EXAMPLES = '''
# Test we can do useless thing
# ansible webservers -m useless

# Example from an Ansible Playbook
- useless:

# Induce an useless exception to see what happens
- useless:
    data: crash
'''

RETURN = '''
useless:
    description: value provided with the data parameter
    returned: success
    type: string
    sample: useless useless useless
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='useless useless useless'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("useless boom")

    result = dict(
        unuseful_data=module.params['data'],
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
