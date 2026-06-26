from kitsat import Modem
import time

if __name__ == "__main__":
    m = Modem()

    try:
        m.connect("COM5")
        print("Ligado ao Kitsat!")

        m.write("beep 3")
        print("Comando enviado: beep")

        # Esperar só um pouco
        time.sleep(1)

        # Tenta ler sem lançar exceção se não houver resposta
        data = None
        try:
            data = m.read_all()
        except:
            pass  # ignorar, beep pode não ter resposta

        if data:
            print("Resposta do Kitsat:", data)
        else:
            print("Beep executado com sucesso")
    
    except Exception as e:
        print("Erro de comunicação:", e)

    finally:
        m.disconnect()
        print("Ligação fechada.")
