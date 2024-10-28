import uuid

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        
        #criar o id do pagamento na instituição financeira
        bank_payment_id = uuid.uuid4()
        
        #codigo copia e cola
        hash_payment = f'hash_payment_{bank_payment_id}'
        
        #QR code
        img = qrcode.make(hash_payment)
        
        #Salvar a imagem como PNG
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")
        
        return {"bank_payment_id": bank_payment_id, 
                    "qr_code_path": "qr_code_payment_{bank_payment_id}"}
        
    
    
    