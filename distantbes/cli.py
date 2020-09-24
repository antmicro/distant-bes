from distantbes import Invocation
from distantbes.enums import EXIT_CODES
from time import sleep
import argparse

H = [
        "gRPC endpoint of the Build Event Service",
        "gRPC endpoint of the Content Addressable Storage",
        "force localhost in File message",
        "build log file",
        "one or more artifact files",
        "build title/command",
        "sleep N seconds before finishing the build",
        "print available status codes and exit",
        "status code of the build",
        "test log file"
        ]

def main_func(args):
    if args.print_status_codes:
        for v in range(0, len(EXIT_CODES)):
            print("{}\t{}".format(str(v), EXIT_CODES[v]))
        return None

    success = not bool(args.status_code)

    i = Invocation(
            grpc_bes_url=args.bes_backend,
            grpc_cas_url=args.cas_backend,
            command=args.command,
            force_localhost_in_cas_msg=args.force_cas_localhost,
            )

    i.open()
    
    if args.stdout_file is not None:
        with open(args.stdout_file, "r") as f:
            i.add_stdout(f.read())

    if args.artifacts is not None or args.test_log_file is not None:
        i.announce_target("default")

        i.finalize_target_upload_files(i.targets[0], success=success, artifacts=args.artifacts)

        if args.test_log_file is not None:
            with open(args.test_log_file, "r") as f:
                i.add_test_to_target(i.targets[0], logstr=f.read())

    i.add_build_metrics(1,1,1,1,1)

    if args.sleep is not None:
        sleep(args.sleep)

    i.close(status_code=args.status_code)

    print(i.invocation_id)

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bes-backend', type=str, default="localhost:1985", help=H[0])
    parser.add_argument('--cas-backend', type=str, default="localhost:1985", help=H[1])
    parser.add_argument('--force-cas-localhost', action="store_true", help=H[2])
    parser.add_argument('--stdout-file', type=str, help=H[3])
    parser.add_argument('--artifacts', nargs="+", help=H[4])
    parser.add_argument('--test-log-file', type=str, help=H[9])
    parser.add_argument('--command', type=str, default="distant-bes", help=H[5])
    parser.add_argument('--sleep', type=int, help=H[6])
    parser.add_argument('--print-status-codes', action="store_true", help=H[7])
    parser.add_argument('--status_code', type=int, default=0, help=H[8])
    parser.set_defaults(func=main_func)
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
