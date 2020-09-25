# distant-bes

Copyright (c) 2019-2020 [Antmicro](https://www.antmicro.com)

This repository contains code of `distant-bes`, a library for injecting build results into services implementing [Bazel's Build Event Protocol](https://docs.bazel.build/versions/master/build-event-protocol.html).

## Installation

In order to install the library, clone this repository and run `pip install distant-bes/`.

## Compatibility

The library has been tested against the following implementations of the Build Event Protocol:

1. [BuildBuddy](https://github.com/buildbuddy-io/buildbuddy)

## Usage

Although `distant-bes` was designed primarily with usage as a library in mind, a simple CLI interface is provided for reference/testing.

## CLI

Before executing any commands, you may want to run `distant-bes-cli --help` to see the available arguments and their description.

Below is an example of a possible use of the tool. 
It assumes that both BES and CAS services are running on your local machine (however, if that's not the case, use the `--bes-backend` and `--cas-backend` arguments).

```
$ sudo dmesg > dmesg.log
$ uname -a > uname.log
$ echo "This is a test log." > test.log
$ distant-bes-cli --artifacts uname.log --test-log-file test.log --stdout-file dmesg.log --command test --status_code 0
a5e91847-835d-4aec-b655-1809ad0238d9
```

Upon successful execution, the ID of the uploaded invocation will be returned.

## Library reference

To better understand how the whole thing works under the hood, please inspect the `distant-bes/__init__.py` file to see what the **Invocation** class looks like.

Below is an example of how to use the **Invocation** class to inject build results.

```python
from distantbes import Invocation

# Initialize the object - if no arguments provided,
# both BES and CAS backends default to localhost:1985
i = Invocation(
	grpc_bes_url="example.com:1985",
	grpc_cas_url="example.com:1986",
	command="make all",
	)

# Print generated invocation ID
print(i.invocation_id)

# It may be beneficial to check if the server
# is operational before attempting to open an invocation.
if not i.check_grpc_channel():
    print("Channel not accessible!")
    return None

# Open the channel, start stub thread,
# send started, workspace and config events.
i.open()

# Add some build logs.
i.add_stdout("Build in progress...")
i.add_stdout("Still making!")

# Upload an artifact to CAS. It will be used later.
text_artifact = i.cas_uploader.put_string("Lorem ipsum", "lorem.txt")

# Create a target.
# This will append "cool_target" to the
# i.targets list.
i.announce_target("cool_target")

# Mark target as successful.
i.finalize_target(i.targets[0], success=True, artifacts=[text_artifact])

# Add a test to the target.
i.add_test_to_target(i.targets[0], logstr="This is a cool test!")

# Add some build metrics.
i.add_build_metrics(1,1,1,1,1)

# Send the status code, send elapsed time, 
# close the channel, stop the stub thread.
# There are 17 status codes, but you only
# usually need two:
# 0 - SUCCESS
# 1 - FAIL
i.close(status_code=0)
```

## License

[Apache 2.0](LICENSE)