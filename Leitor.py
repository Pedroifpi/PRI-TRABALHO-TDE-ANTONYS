import re
from typing import List, Union
from pathlib import Path

class TextProcessor:
    """
    Classe para processamento de textos com operações baseadas em expressões regulares.
    (Mantém exatamente a mesma implementação anterior)
    """
    
    def __init__(self, file_path: Union[str, Path]) -> None:
        self.file_path = Path(file_path)
        self.content = ""
        
    def __str__(self) -> str:
        return f"TextProcessor(file='{self.file_path.name}', chars={len(self.content)})"
    
    def read_file(self) -> None:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")
    
    def filter_words_starting_with(self, letter: str) -> List[str]:
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
        pattern = re.compile(rf'\b[{letter.lower()}{letter.upper()}]\w*\b')
        return pattern.findall(self.content)
    
    def filter_words_containing(self, letter: str) -> List[str]:
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
        pattern = re.compile(rf'\b\w*[{letter.lower()}{letter.upper()}]\w*\b')
        return pattern.findall(self.content)
    
    def replace_commas_with_dots(self) -> str:
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
        return self.content.replace(',', '.')
    
    def extract_dates(self) -> List[str]:
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
        pattern = re.compile(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b')
        return pattern.findall(self.content)
    
    def hide_sensitive_info(self) -> str:
        if not self.content:
            raise ValueError("Nenhum conteúdo carregado. Use read_file() primeiro.")
        text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL]', self.content)
        text = re.sub(r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b', '[CPF]', text)
        text = re.sub(r'\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}\b', '[TELEFONE]', text)
        return text
