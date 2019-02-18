# TP1 



## Pergunta P1.1


Os ficheiros **/dev/random** e **/dev/urandom/** são fontes de entropia para a geração de números pseudoaleatórios. Enquanto que o ficheiro **/dev/random** bloqueia quando não existe entropia suficiente para geração do número, a diretoria **/dev/urandom** nunca bloqueia.<br> 
Posto isto após a execução os dois primeiros comandos correm sem qualquer tipo problema, mas o terceiro comando bloqueia pois não existe entropia suficiente no ficheiro /dev/random. Já no caso do ultimo comando corre sem qualquer tipo de problema visto que o ficheiro /dev/urandom não bloqueia com a falta de entropia.<br>
Podemos concluir que como o **/dev/urandom** não espera por entropia suficiente, é teoricamente mais vulnerável a ataques criptográficos.


## Pergunta P1.2


Após a instalção do *havaged*, executando os comandos o comando que usa o ficheiro /dev/random não bloqueia, podemos então concluir que o ficheiro /dev/random já possui entropia suficiente, isto deve-se ao facto de o *havaged* solucionar o problema da falta de entropia no sistema.


## Pergunta P1.3

1\. O programa *generateSecret-app.py* invoca a função *generateSecret* do módulo *shamirsecret* da bilbioteca eVotUm.Cripto e escreve o output da função no ecrã. A função *generateSecret* invoca uma função que cria uma random string de bytes com base na entropia do sistema, posteriormente a string é percorrida de forma a filtrar apenas as letras e os números(*string.ascii_letters e string.digits*) este processo é repetido até obter o tamanho desejado dado como argumento à função.
<br>
2\. Para que o output não seja restrito a letras e números podemos modificar a função *generateRandomData* da biblioteca *utils* usando a função *b64encode* da biblioteca *base64* para modificar o seu resultado e deixa de ser necessário filtrar por printable characters.


## Pergunta P2.1

A\. Inicialmente começamos por gerar uma private key usando o openssl, depois executamos a função dando como argumentos o número de partes em que o segredo vai ser dividido, o número de partes necessárias para reconstruir o segredo, o seu identificador e por ultimo a chave privada. Este metodo de dividir o segredo é usado para garantir confidencialidade e também confiabilidade.

```root@CSI:~/Desktop/TPS/aula2/ShamirSharing# python2 createSharedSecret-app.py 8 5 1 mykey.pem 
Private key passphrase: 1234
Secret: Agora temos um segredo extremamente confidencial
Component: 1
eyJhbGciOiAiUlMyNTYifQ.eyJvYmplY3QiOiBbIjEtN2Q1YTNjNjVmMDFhODM3ZDU4NzYwNmI4Yjk5NzFhYWIwOTk3YjliZWVjZjA4MjllYmE1ZTEzYzhiZmE1ZGMyMDY5MGNmOTY3ZDliMGQ0MjI5N2RiMjI5MjMzYmNhMTAzIiwgIjEiLCA1LCA4LCAiMmY5ZjA2ZmFkZTIxZmUwYmY0MzA2YzRmOGIyNWRhNjRjOGI0NTBlZmRjNzc5NTA2ODU2NjZjNzEwMDJmNzZiZSJdfQ.OsbQyAbJyo1jBOIfAHTIWdUH8jO3LoFSsDmA-H-QkElps_0bGfro5Lc7sTS633BV7akvR6RwWtLJE8httMUDgMwHb5rrFbany3FC6ZbeKbdYIRhq9F5ZCRT-Xe6aZEN6YC0I01tW82zGgoW0_NY_0NzrRlMzy0ZHTXAGrVYa8GM
Component: 2
eyJhbGciOiAiUlMyNTYifQ.eyJvYmplY3QiOiBbIjItNWRmNDAwOWYwOTZkM2FlZTVkNmU2NWUzYjliYTMyNWEzOWM5ZWYyNzNmMDFmZjhjODZlNWJjYWU4NWRiM2VkNjQ5OGUyZTU5MjI3ZDZkNDk5NmFlNjFjMDIwMmE4YzgiLCAiMSIsIDUsIDgsICJmY2ZjY2FiZjNiZmQ5ODRiN2VkZDQzOTEzNTY4MjVjZTQwMGYzMDIzMGVlOTIxNTBhNzhhYThiZmQ0ZjQxMzY5Il19.heSykES8f6jWgHMauUUbOOmX4vMsvj0vWrJHm7cCeMVLLpsnp5KZ3xFO1VSrI3kwu8K0YNDwJcjPmoRVP81GVx0aNSHVvCQ6BRM2975I6ZyazHrUt_vF9vjRdzZzJ3GS9bcwslDMM3SywzbU2BK9KJfyqv9v8RU8Q4J6J1X5F0E
Component: 3
eyJhbGciOiAiUlMyNTYifQ.eyJvYmplY3QiOiBbIjMtNTA1ZTkwYzM0OWE3MTgzMTNjYWY4ZjYwYTI4YTBiZGQ3MDI4OTg2M2QyNTYxOTkxMmFhZWFmZGUyZTljNTEzZTMzNjgyMzk0MTJiODY2NzY5ZTlmNjQ0YmY0NjQ3NGQ0IiwgIjEiLCA1LCA4LCAiNjVlNTlhMTgxOWU5OWM3ZTE2MjMxM2QwZjQ1ZmVhYWQ2Zjk3ZGQ5NWIwZmY5N2E2N2NiMzMwYjhkYzkzNTUyZSJdfQ.XGhWjN9_R8CYTkrZ0T4NVEZyOhY2TKTsoQyTKsfah52D_unaiW4WVLCU0sc5jba7veQBch7dXouqHoUnGmVRfWd8OqBl0PTQGjvyPvj06x3JkYZ8QDgK0E9Im8VBgJDlqKmKsKFSj7HI-v4wcjNSYlPagPq8xl8k488QQM4KIck
Component: 4
eyJhbGciOiAiUlMyNTYifQ.eyJvYmplY3QiOiBbIjQtZDA4OGZjMzg0MTUwM2ViZTQyZmI1N2NhMTJmZWY0ZDA2Y2MyZDFhZDJmOWE1OTViM2YzYjdhOTFhYTBlZDYyYTRkY2YyNmRlZjVmNWY3ZjM2ZGI5ODNkYmQzMTQ2NGY2IiwgIjEiLCA1LCA4LCAiOWQ2YTBmYmFhM2QyNjI2NWM5Yzg1NmZiZGIxOGMzY2NlZDk4MjlhZWZiMTAxYTczODE2ODFjM2M2OGJkMGMxMyJdfQ.YAf9cOort_8pFQR7SmOPZGJDngGmrIhYEnNO7SyEuhxYTFENgQV0-9QMUS73efLsXvI9VRmHLFG-O2l1Q5VMgWoNe87tBFIi7-OFh5PgawRQ2EVZC1GP97XXG1K-k2r0j9hnKO4erpSa6abkSual4ZFrI71Wn1tsbhmgAtqK7PI
Component: 5
eyJhbGciOiAiUlMyNTYifQ.eyJvYmplY3QiOiBbIjUtZjg1ODA3NTA3YzhhNmY5MjlkOTM2ZTVmMmYyNDRjMDA1N2M3MmI5ZjAxYzQ5MjIwM2E0NDJiOTE0MmZjMmE2ZWQyMjZjMWEyZWIyMzg1MjY2MmFmNWRmZjA4NGUzZTgxIiwgIjEiLCA1LCA4LCAiMjQxMGUyMWQwNGJiMjUxY2E0ZmJkN2ZmZjgzY2FjYjA4M2RlMTJhMzI4Y2Q5MWJjMjRhMzNmZmNmMWYxZjZmMyJdfQ.PUsUD12HzY9ePE5tj9HE0Kt6qKILIOqszqm7-gtwXFEP6tvpx2x7fWRxZ6BMIGLOTbUp_aPFdw3ZyScMHFnaWJo4FemOmLSHvBMmtnpG6QWa6F-oHFc9iJTCzJJCGU-cFfh08VqftDp04o62Q6Oo4ivPoNIuOoipW8tahqMjyQk
Component: 6
eyJhbGciOiAiUlMyNTYifQ.eyJvYmplY3QiOiBbIjYtMzgwZGVlMzRmZjQxMGQ2ZGIwMmVkYTlmMTZiMTRkNzJiMDY2M2M0MDBkNmMzZjdmMjYwYjM3YTViMjQ0ZmI2ZTg0Y2MzMjJkYjYzMzhjZGI2ZjJjM2U2MmEwNTcyYzRjIiwgIjEiLCA1LCA4LCAiZTY3NTNmNDk1YWRmNmI3ZTQ1ZTU2ZmVhOTgyNzI3MmIyOWJjMmE5M2U4YmYzZGM5N2FjY2U5NmE3MzVkZTE2YiJdfQ.V9mboMWGz6wX0JEwgpuwnDBKmQ3k4nVCbKHl8cHqKQyticVbMbGcDQPkkWLwVNdYGGan4xTTlsnbhncNGMYydxpXFtTI0zRtvE2THFznG7uwxElJvFmU_CkGhz4RJnhFisr5GJajV7LvCBrjnuJqdPJ100Vghyp24JI0h-Nqrl0
Component: 7
eyJhbGciOiAiUlMyNTYifQ.eyJvYmplY3QiOiBbIjctZmUzNWE0NTAyYzUyYjU5MTlkNjI3Y2MzNjZlYTgzMzBiNmE1NGVjZDY1YjhhNWVjZTJlNjE4YjQ4MTYzYmMzMWQwMjEyMDNlMmZjODEyY2YxYTkwYTMyZDQ5N2RjMTY3IiwgIjEiLCA1LCA4LCAiMjA2NWRlMjg4ZDAyZGY1NGVkN2JjZjAzZTdjYzJiMDA5YTFlY2E0MjliOTcwMDI4ZTgxODgxMjNlMWRjY2ZhNyJdfQ.LnNTPr6VbFfa7JWMiFBJto4fbfonFqq8y2DDpno_VED1FyqK1oN33CcoyUPC7khdSMsvmDpWegzdnFCMk1ailf3PiVNIcvFANdf6p5iLyGtdm8F_QLg2TfyZGOUrFLYqaF6uPQqYzBvrbU_NeGVTSQE8xVSiVIU0ZyiecZO_UT0
Component: 8
eyJhbGciOiAiUlMyNTYifQ.eyJvYmplY3QiOiBbIjgtYjdhMmQ0NGRjNTkxM2ZjMzQ2YTEwZGMwM2FhMWM1NDc2YjVlNjNiYTZjNjBkMmI0MjczZDRkYzAwYTZjYTU2NmM0OGI5ZDA0NDUzMjlmYWU4MWYyM2NmZjU0MTlmMWUzIiwgIjEiLCA1LCA4LCAiYzM0YWU2YmUwOTkwMTZhYzUzZTJiNmFmY2RhMTIyNTlkZDU3NGM2MGVkNzY2MDVlMmU1Y2M3MTFiYjdmOWExNyJdfQ.FqNd3sl1REBeXfeBZ1rDhq0uGYaQFZRVtQXkUQzJWA-EcDQbYigP-b-fJ_ObI-uwCPgCU8w3c3SjabxTLbjU-f5MsC95C--kBdjr2WoxO-G_SfTsa7vVtoH6QX83C8jtYWXO84XWVvPpl6hND5puKyCuywVhYwCgTkwHTzznYu4```

B\. A principal diferença entre os dois programas é o número de componentes necessárias para recuperar o segredo. No caso do programa *recoverSecretFromComponents-app.py* são necessárias 5 componentes(quorom) para podermos obter o segredo, já no caso do programa *recoverSecretFromAllComponents-app.py* são necessárias todas as componentes(8) para podermos obter o segredo. Se dermos menos componentes do que as necessárias os programas não revelam o segredo.<br>
O programa *recoverSecretFromAllComponents-app.py* pode ser usado quando o nivel de criticidade do segredo é bastante elevado, o outro programa pode ser usado para segredos não tão criticos.

## Pergunta P3.1

Sim, deve-se utilizar *Authenticated Encryption* pois esta forma de cifra garante simultaneamente autenticidade, integridade e confidencialidade.
Optamos por usar o método *Encrypt-then-mac*.

```
def Cifra(mensagem, etiqueta):
    ciphertext = cifra(mensagem)
    key = raw_input()
    mac = hmac(key,cyphertext+etiqueta)
    return ciphertext,mac
        
def Decifra(ciphertext,etiqueta,datakey(do tipo ano.mes.dia),mac):
    key=raw_input()
    if(hmac(key,ciphertext+etiqueta)==mac):
      mensagem = decifra(ciphertext,datakey)
    else:
      print("ERROR: Authentication Failed")
    return mensagem```


## Pergunta P4.1

Ambas as entidades certificadoras da Lituania, *Identity Documents Personalisation Centre under the Ministry of the Interior* e *State Enterprise Centre of Registers*, usam o algoritmo *SHA256WITHRSAEncryption* para a assinatura digital, e usam o algoritmo de chave publica RSA com uma chave de comprimento de 2048 bits. Este algoritmo ainda é considerado seguro apesar de já ser aconselhado o uso de uma chave maior para o RSA.