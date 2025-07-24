from src.principal import TextProcessor  # Alterado para importar de principal

def main():
    try:
        # Criar instância e ler arquivo
        processor = TextProcessor("exemplo.txt")
        processor.read_file()
        
        print("=== Demonstração do TextProcessor ===")
        print(f"Processando arquivo: {processor.file_path.name}\n")
        
        print("1. Palavras começando com 'a':")
        print(processor.filter_words_starting_with('a'))
        
        print("\n2. Palavras contendo 'e':")
        print(processor.filter_words_containing('e'))
        
        print("\n3. Datas encontradas:")
        print(processor.extract_dates())
        
        print("\n4. Texto com vírgulas substituídas:")
        print(processor.replace_commas_with_dots()[:200] + "...")
        
        print("\n5. Ocultação de dados sensíveis:")
        print(processor.hide_sensitive_info()[:200] + "...")
        
        print("\n=== Status do processador ===")
        print(processor)
        
    except Exception as e:
        print(f"\nErro durante a execução: {e}")

if __name__ == "__main__":
    main()
