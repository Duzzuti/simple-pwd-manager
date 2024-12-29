# File Formats
## v0.1
### Encrypted File Format
|Bytes|DefaultLength|Symbol|Description|
|-----------|--|---|--------------------------|
|0          |1 |mv |Major version number      |
|1          |1 |mi |Minor version number      |
|2          |1 |sl |Salt length in Bytes      |
|3    - sl+2|16|S  |Salt used for derived key generation|
|3+sl       |1 |N  |Parameter n used for key derivation as 2**N|
|4+sl       |1 |r  |Parameter r used for key derivation|
|5+sl       |1 |p  |Parameter p used for key derivation|
|6+sl -21+sl|16|IV |Initialization Vector used for encryption|
|22+sl-53+sl|32|HV |HMAC Value of the whole file data except this section, length is bound to hash function (we use SHA256)|
|54+sl- EOF |- |ED |Encrypted Data|

### Decrypted Data Format (decrypted ED)
|Bytes|DefaultLength|Symbol|Description|
|---------------|--|---|--------------------------|
|0              |1 |rl |Length of the random padding section|
|1    - rl      |- |RP |Random padding section|
|1+rl - 8+rl    |8 |pl |Length of the password section|
|9+rl - 8+pl+rl |- |PS |Password section|
|9+pl+rl - EOF  |- |OS |Other section|
