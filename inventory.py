#!/usr/bin/env python3
import json
import os
from typing import (
    Any,
    Dict,
    Optional,
)


def env(name: str, default: Optional[str] = None) -> str:
    return os.getenv(f'ANSIBLE_{name}', default)


def generate_inventory() -> Dict[str, Any]:
    host = 'coffee.sugar-code.space'

    return {
        'vps': {
            'hosts': [host],
            'vars': {
                'ansible_python_interpreter': '/usr/bin/python3',
                'ansible_ssh_user': env('SSH_USER'),
            }
        },
        "_meta": {
            "hostvars": {
                host: {
                    'vps': host,
                    'ssh_user': env('SSH_USER'),
                    'github_token': env('GITHUB_TOKEN'),
                    'git_branch': 'HEAD',
                    'django_secret_key': env('DJANGO_SECRET_KEY'),
                    'allowed_hosts': env('ALLOWED_HOSTS'),
                },
            },
        },
    }


def main() -> None:
    print(json.dumps(generate_inventory(), indent=4))


if __name__ == '__main__':
    main()
