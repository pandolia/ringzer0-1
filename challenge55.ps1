function Reverse-SecureString([string]$secureString,[string]$key)
{
  $objSecString=ConvertTo-SecureString -String $secureString -Key ([Byte[]]$key.Split(" "))
  $secString=[System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($objSecString)
  $plaintext=[System.Runtime.InteropServices.Marshal]::PtrToStringAuto($secString)
  return $plaintext
}

$password = "76492d1116743f0423413b16050a5345MgB8AEEAYQBNAHgAZQAxAFEAVABIAEEAcABtAE4ATgBVAFoAMwBOAFIAagBIAGcAPQA9AHwAZAAyADYAMgA2ADgAMwBlADcANAA3ADIAOQA1ADIAMwA0ADMAMwBlADIAOABmADIAZABlAGMAMQBiAGMANgBjADYANAA4ADQAZgAwADAANwA1AGUAMgBlADYAMwA4AGEAZgA1AGQAYgA5ADIAMgBkAGIAYgA5AGEAMQAyADYAOAA="
$key = "3 4 2 3 56 34 254 222 205 34 2 23 42 64 33 223 1 34 2 7 6 5 35 12"
$passPlaintext = Reverse-SecureString "$password" "$key"
Write-Host $passPlaintext
