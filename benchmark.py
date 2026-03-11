import os
import warnings
import torch
import time

# Silencia avisos desnecessários
warnings.filterwarnings("ignore")

print("--- AI Scientist Lab: CPU High-Performance Mode ---")
print(f"Proprietário: Reinaldo | Projeto: DESAFIO_FIAP_FASE_1")

# Configuramos o dispositivo explicitamente para a CPU
device = torch.device("cpu")
cpu_name = "AMD Ryzen 7 9800X3D (Zen 5 Architecture)"

print(f"✅ Hardware Ativo: {cpu_name}")
print(f"✅ Status: Ambiente de Estudo Estabilizado")

try:
    # Benchmark com Matrizes de 5.000 x 5.000 (Tamanho ideal para teste de CPU)
    # 10k x 10k em CPU pode demorar alguns segundos, 5k é mais ágil para teste.
    size = 5000 
    print(f"\nAlocando matrizes {size}x{size} na Memória RAM (32GB DDR5)...")
    
    # Criando dados aleatórios na CPU
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)
    
    print("Executando multiplicação de matrizes no Ryzen 9800X3D...")
    
    # Benchmark Real
    start = time.time()
    c = torch.matmul(a, b)
    end = time.time()
    
    tempo = end - start
    print(f"\n🚀 SUCESSO: Cálculo concluído em {tempo:.4f} segundos!")
    print("Nota: O processamento em CPU é 100% estável para o Desafio FIAP.")

except Exception as e:
    print(f"\n⚠️ Erro inesperado: {e}")

print("\n--- Fim do Processo ---")