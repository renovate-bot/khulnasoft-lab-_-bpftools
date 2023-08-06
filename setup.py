import os
import setuptools
import shutil
import sys


if not os.path.exists('ebpf-toolkit/bpf_asm'):
    os.system("make -C linux_tools")
    if not os.path.exists('linux_tools/bpf_asm'):
        print >> sys.stderr, "Type 'make' before packaging"
        sys.exit(-1)
    shutil.copy('linux_tools/bpf_asm', 'ebpf-toolkit')


setuptools.setup(
    name='ebpf-toolkit',
    version='1.0',
    description='BPF Tools - packet analyst toolkit',
    url='https://github.com/cloudflare/ebpf-toolkit',
    packages=['ebpf-toolkit'],
    maintainer="Md Sulaiman",
    maintainer_email="devops@khulnasoft.com",
    package_data = {
        '': ['bpf_asm'],
        },
    zip_safe = False,
    )
