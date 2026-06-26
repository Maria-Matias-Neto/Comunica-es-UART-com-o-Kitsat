from kitsat import Modem

if __name__ == "__main__":
    m = Modem()
    m.connect("COM5")         
    m.write("ping") 
    try:
        data = m.read()       # Recebe resposta decodificada
        print("Dados recebidos do Kitsat:", data)
    except Exception as e:
        print("Não devolve dados", e)
    m.disconnect()
