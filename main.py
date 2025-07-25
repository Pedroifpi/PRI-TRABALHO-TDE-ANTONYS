from pathlib import Path
from src.principal import TextProcessor

def main():
    # Configuração robusta de caminhos
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "data"
    DATA_DIR.mkdir(exist_ok=True)  # Cria a pasta se não existir
    
    file_path = DATA_DIR / "exemplo.txt"
    
    try:
        # Verificação explícita do arquivo
        if not file_path.exists():
            raise FileNotFoundError(
                f"Crie o arquivo '{file_path}' com texto para processamento!\n"
                f"Local esperado: {file_path.absolute()}"
            )
        
        # Processamento
        processor = TextProcessor(file_path)
        processor.read_file()
        
        print("="*50)
        print(f"{processor}\n")
        
        print("[1] Palavras começando com 'a':")
        print(processor.filter_words_starting_with('a'))
        
        print("\n[2] Datas encontradas:")
        print(processor.extract_dates())
        
        print("\n[3] Texto com dados sensíveis ocultos:")
        print(processor.hide_sensitive_info()[:300] + "...")
        
        print("\n" + "="*50)
        
    except Exception as e:
        print(f"\nERRO: {e}\n")
        print("Solução:")
        print(f"1. Crie a pasta 'data' na raiz do projeto")
        print(f"2. Adicione um arquivo 'exemplo.txt' dentro dela")

if __name__ == "__main__":
    main()
