from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


# Geração de uma chave privada
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())

# Obtenção de uma chave pública correspondente
public_key = private_key.public_key()

# Serializar e deserializar as chaves
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

private_key = serialization.load_pem_private_key(
    private_key_bytes,
    password=None,
    backend=default_backend()
)

public_key = serialization.load_pem_public_key(
    public_key_bytes,
    backend=default_backend()
)

print(public_key_bytes)
print(private_key_bytes)

# Mensagem para criptografar
# message = b"Hello, world!"

# signature = private_key.sign(
#     message,
#     ec.ECDSA(hashes.SHA256())
# )

# print(f"Assinatura com chave privada: {signature}\n\n")

# try:
#     public_key.verify(
#         signature,
#         message,
#         ec.ECDSA(hashes.SHA256())
#     )
#     print("Assinatura válida.")
# except InvalidSignature:
#     print("Assinatura inválida.")
