import re
from typing import List, Optional, Union
from pathlib import Path

class TextProcessor:
    """
    Classe para processamento de textos com operações baseadas em expressões regulares.
    
    Atributos:
        file_path (Path): Caminho para o arquivo de texto.
        content (str): Conteúdo do arquivo carregado.
    """
    
    def __init__(self, file_path: Union[str, Path]) -> None:
        """
        Inicializa o processador de texto com o caminho do arquivo.
        
        Args:
            file_path: Caminho para o arquivo de texto.
        """
        self.file_path = Path(file_path)
        self.content = ""
        
    def __str__(self) -> str:
        """Representação em string da classe mostrando informações básicas."""
        return f"TextProcessor(file='{self.file_path.name}', chars={len(self.content)})"
    
    def read_file(self) -> None:
        """
        Lê o conteúdo do arquivo de texto e armazena no atributo content.
        
        Raises:
            FileNotFoundError: Se o arquivo não existir.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")
    
    def filter_words_starting_with(self, letter: str) -> List[str]:
        """
        Filtra palavras que começam com a letra especificada.
        
        Args:
            letter: Letra para filtrar (case insensitive).
            
        Returns:
            Lista de palavras que começam com a letra especificada.
        """
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
            
        pattern = re.compile(rf'\b[{letter.lower()}{letter.upper()}]\w*\b')
        return pattern.findall(self.content)
    
    def filter_words_containing(self, letter: str) -> List[str]:
        """
        Filtra palavras que contêm a letra especificada em qualquer posição.
        
        Args:
            letter: Letra para filtrar (case insensitive).
            
        Returns:
            Lista de palavras que contêm a letra especificada.
        """
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
            
        pattern = re.compile(rf'\b\w*[{letter.lower()}{letter.upper()}]\w*\b')
        return pattern.findall(self.content)
    
    def replace_commas_with_dots(self) -> str:
        """
        Substitui todas as vírgulas por pontos no texto.
        
        Returns:
            Texto com vírgulas substituídas por pontos.
        """
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
            
        return self.content.replace(',', '.')
    
    def extract_dates(self) -> List[str]:
        """
        Extrai datas no formato DD/MM/AAAA ou DD-MM-AAAA do texto.
        
        Returns:
            Lista de datas encontradas no texto.
        """
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
            
        pattern = re.compile(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b')
        return pattern.findall(self.content)
    
    def hide_sensitive_info(self) -> str:
        """
        Oculta informações sensíveis como e-mails, CPFs e telefones.
        
        Returns:
            Texto com informações sensíveis ofuscadas.
        """
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
            
        # Ocultar e-mails
        text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL]', self.content)
        # Ocultar CPFs (formato 000.000.000-00 ou 00000000000)
        text = re.sub(r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b', '[CPF]', text)
        # Ocultar telefones (formato (00) 0000-0000 ou 00 00000-0000)
        text = re.sub(r'\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}\b', '[TELEFONE]', text)
        
        return text
