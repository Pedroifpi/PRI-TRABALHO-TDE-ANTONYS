from src.text_processor import TextProcessor

def main():
    try:
        # Criar instância e ler arquivo
        processor = TextProcessor("exemplo.txt")
        processor.read_file()
        
        print("=== Texto Original ===")
        print(processor.content[:200] + "...")  # Mostrar apenas parte do texto
        
        print("\n=== Palavras que começam com 'a' ===")
        print(processor.filter_words_starting_with('a'))
        
        print("\n=== Palavras que contêm 'e' ===")
        print(processor.filter_words_containing('e'))
        
        print("\n=== Texto com vírgulas substituídas ===")
        print(processor.replace_commas_with_dots()[:200] + "...")
        
        print("\n=== Datas encontradas ===")
        print(processor.extract_dates())
        
        print("\n=== Texto com informações sensíveis ofuscadas ===")
        print(processor.hide_sensitive_info()[:200] + "...")
        
        print("\n=== Representação do objeto ===")
        print(processor)
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
