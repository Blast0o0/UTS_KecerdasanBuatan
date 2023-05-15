import random

# Definisikan beberapa respons chatbot
responses = {
    "hai": "Halo! Ada yang bisa saya bantu?",
    "apa kabar": "Saya baik-baik saja, terima kasih.",
    "siapa kamu": "Saya adalah Chatbot dari kelompok 5.",
    "tujuan kamu": "Saya disini bertujuan dalam rangka penyelesaian UTS matkul kecerdasan buatan",
    "default": "Maaf, saya tidak mengerti. Bisa Anda jelaskan lebih lanjut?",
}

# Fungsi untuk memilih respons sesuai input pengguna
def respond(message):
    if message.lower() in responses:
        return responses[message.lower()]
    else:
        return responses["default"]

# Main program chatbot
print("Halo, saya adalah Chatbot. Silakan bertanya atau mengobrol dengan saya.")
while True:
    message = input("Anda: ")
    print("Chatbot: " + respond(message))
