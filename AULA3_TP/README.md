# TP2 



## Pergunta P2.1

&nbsp;&nbsp;&nbsp;The server that showed worst results was the server of the **Governament of Namibia**. <br>
&nbsp;&nbsp;&nbsp;This server does not support **Autenthicated Encryption (AEAD)**, which is the only encryption aproach without any known weaknesses. Without this aproach the server is vulnerable to **Timing Attacks**. It also does not use **Foward Secrecy**, a property of secure communication protocols. It protects passed sessions against future compromises of private-key. <br>
&nbsp;&nbsp;&nbsp;The server accepts **RC4-Cipher**, but only with older protocols. This cipher is demonstrably broken and unsafe to use in **TLS** as currently implemented, although the attack is not yet practical. <br>
&nbsp;&nbsp;&nbsp;It supports only older protocols, but not the best TLS1.2. Instead it uses TLS1.0, which is insecure and remains vulnerable to attacks, like the **Lucky 13 attack** .  <br>
&nbsp;&nbsp;&nbsp;Mozilla and Google distrust this server's certificate because it was issued by **Symantec** and they lost confidence in their cerficate issuance policies and practices. <br>
&nbsp;&nbsp;&nbsp; This server uses **SSL3**, that makes it vulnerable to the **POODLE Attack**. This attack will be explained in the next question. <br>
&nbsp;&nbsp;&nbsp; The last problem is that it supports insecure **Diffie-Hellman** key exchange parameters, making it vulnerable to the **Logjam attack**, allowing a **Men-in-the-Middle .  

