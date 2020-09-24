#!/usr/bin/env python3

import os, re, sys

def run():
    try:
        import grpc_tools.command
    except ImportError:
        print("Distant-bes requires grpc_tools in order to build gRPC modules.\n"
                "Install it via pip (pip3 install grpcio-tools).")
        exit(1)

    protos_root = 'distantbes/proto'

    grpc_tools.command.build_package_protos(protos_root)

    for root, _, files in os.walk(protos_root):
        for filename in files:
            if filename.endswith('.py'):
                path = os.path.join(root, filename)
                with open(path, 'r') as f:
                    code = f.read()

                code = re.sub(r'^from ', r'from distantbes.proto.',
                        code, flags=re.MULTILINE)

                code = re.sub(r'^from distantbes.proto.google.protobuf', r'from google.protobuf',
                        code, flags=re.MULTILINE)

                with open(path, 'w') as f:
                    f.write(code)


run()
