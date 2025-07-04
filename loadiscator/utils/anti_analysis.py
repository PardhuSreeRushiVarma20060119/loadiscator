import platform
import os
import time
import random

def generate_vm_detection():
    """Generate VM detection code."""
    return '''
def check_vm():
    """Basic VM detection checks."""
    vm_indicators = [
        "VMware", "VirtualBox", "QEMU", "Xen", "Parallels",
        "vbox", "vmware", "virtual", "qemu"
    ]
    
    # Check system info
    system_info = platform.system() + " " + platform.release()
    for indicator in vm_indicators:
        if indicator.lower() in system_info.lower():
            return True
    
    # Check common VM files
    vm_files = [
        "/sys/class/dmi/id/product_name",
        "/proc/scsi/scsi",
        "/proc/cpuinfo"
    ]
    
    for file_path in vm_files:
        try:
            with open(file_path, 'r') as f:
                content = f.read().lower()
                for indicator in vm_indicators:
                    if indicator.lower() in content:
                        return True
        except:
            pass
    
    return False

# Anti-analysis timing
if check_vm():
    time.sleep(random.uniform(2, 5))
else:
    time.sleep(random.uniform(0.1, 0.5))
'''

def generate_sandbox_evasion():
    """Generate sandbox evasion code."""
    return '''
def evade_sandbox():
    """Basic sandbox evasion techniques."""
    # Check for common sandbox indicators
    sandbox_indicators = [
        "sandbox", "analysis", "debug", "test"
    ]
    
    # Check environment variables
    for key, value in os.environ.items():
        for indicator in sandbox_indicators:
            if indicator.lower() in value.lower():
                return True
    
    # Check hostname
    hostname = platform.node().lower()
    for indicator in sandbox_indicators:
        if indicator in hostname:
            return True
    
    return False

# Execute only if not in sandbox
if not evade_sandbox():
    # Main payload execution
    pass
'''

def generate_timing_checks():
    """Generate timing-based anti-analysis."""
    return '''
import time
import random

def timing_check():
    """Timing-based anti-analysis."""
    start_time = time.time()
    
    # Perform some operations
    for i in range(random.randint(100, 1000)):
        _ = i * i
    
    execution_time = time.time() - start_time
    
    # If execution is too fast, likely in sandbox
    if execution_time < 0.01:
        return False
    
    return True

# Only proceed if timing check passes
if timing_check():
    # Main payload execution
    pass
''' 