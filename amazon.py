import uuid
from datetime import datetime, timedelta

class GiftCardGenerator:
    def _init_(self, balance):
        self.code = self.generate_code()
        self.balance = balance
        self.expiration_date = datetime.now() + timedelta(days=365)  # Expiración en 1 año

    def generate_code(self):
        """Genera un código alfanumérico único de 10 caracteres para la tarjeta de regalo."""
        return str(uuid.uuid4()).replace("-", "").upper()[:10]

    def _str_(self):
        return f"Gift Card Code: {self.code}, Balance: ${self.balance}, Expiration Date: {self.expiration_date}"

# Ejemplo de uso
gift_card = GiftCardGenerator(100)  # Crear una tarjeta de regalo con $100 de saldo
print(gift_card)