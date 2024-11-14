## Encrypted File Format
|Bytes|DefaultLength|Symbol|Description|
|-----------|--|---|--------------------------|
|0          |1 |sl |Salt length in Bytes      |
|1    - sl  |16|S  |Salt used for derived key generation|
|1+sl       |1 |N  |Parameter n used for key derivation as 2**N|
|2+sl       |1 |r  |Parameter r used for key derivation|
|3+sl       |1 |p  |Parameter p used for key derivation|
|4+sl -19+sl|16|IV |Initialization Vector used for encryption|
|20+sl-51+sl|32|HV |HMAC Value of the IV + encrypted data, length is bound to hash function (we use SHA256)|
|52+sl- EOF |- |ED |Encrypted Data|

## Decrypted Data Format
|Bytes|DefaultLength|Symbol|Description|
|-----------|--|---|--------------------------|
|0    - 7   |8 |pl|Length of the password section|
|8    - 7+pl|- |PS|Password section|
|8+pl - EOF |- |OS|Other section|
