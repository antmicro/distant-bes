from enum import Enum

EXIT_CODES = [
        "SUCCESS", 
        "BUILD_FAILURE", 
        "PARSING_FAILURE", 
        "COMMAND_LINE_ERROR", 
        "TESTS_FAILED",
        "PARTIAL_ANALYSIS_FAILURE",
        "NO_TESTS_FOUND",
        "RUN_FAILURE",
        "ANALYSIS_FAILURE",
        "INTERRUPTED",
        "LOCK_HELD_NOBLOCK_FOR_LOCK",
        "REMOTE_ENVIRONMENTAL_ERROR",
        "OOM_ERROR",
        "REMOTE_ERROR",
        "LOCAL_ENVIRONMENT_ERROR",
        "BLAZE_INTERNAL_ERROR",
        "PUBLISH_ERROR",
        "PERSISTENT_BUILD_EVENT_SERVICE_UPLOAD_ERROR"
        ]

class DistantEnum(Enum):
    def __str__(self):
        return str(self.value)

class CPU(DistantEnum):
    k8 = "k8"
    piii = "piii"
    darwin = "darwin"
    freebsd = "freebsd"
    armeabi = "armeabi-v7a"
    arm = "arm"
    aarch64 = "aarch64"
    x64_windows = "x64_windows"
    x64_windows_msvc = "x64_windows_msvc"
    s390x = "s390x"
    ppc = "ppc"
    ppc64 = "ppc64"

class CompilationMode(DistantEnum):
    fastbuild = "fastbuild"
    dbg = "dbg"
    opt = "opt"
