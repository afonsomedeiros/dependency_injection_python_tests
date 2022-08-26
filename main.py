from typing import List
from dataclasses import dataclass
from abc import ABC, abstractmethod
import inject


usuarios = []

@dataclass
class Usuario:
    nome: str
    idade: int


class UsuarioRepository(ABC):
    @abstractmethod
    def cadastrar_usuarios(self, usuario: Usuario) -> bool:
        """Cadastrar novo usuário."""

    @abstractmethod
    def listar_usuarios(self) -> List[Usuario]:
        """Listar usuários."""


class InMemoryUsuarioRepository(UsuarioRepository):
    def cadastrar_usuarios(self, usuario: Usuario) -> bool:
        usuarios.append(usuario)

    def listar_usuarios(self) -> List[Usuario]:
        return list(usuarios)


class UsuarioService:
    @inject.autoparams()
    def __init__(self, usuario_repository: UsuarioRepository) -> None:
        self.usuario_repository = usuario_repository

    def cadastrar(self, nome, idade):
        self.usuario_repository.cadastrar_usuarios(Usuario(nome=nome, idade=idade))

    def print_usuarios(self):
        for usuario in usuarios:
            print(f"nome: {usuario.nome} - Idade: {usuario.idade}")


def ioc_config(binder):
    binder.bind(UsuarioRepository, InMemoryUsuarioRepository())


def register_ioc():
    inject.configure(ioc_config)


def main():
    register_ioc()
    service = UsuarioService()
    service.cadastrar("Afonso 001", "10")
    service.cadastrar("Afonso 002", "11")
    service.cadastrar("Afonso 003", "12")
    service.cadastrar("Afonso 004", "13")
    service.cadastrar("Afonso 005", "14")
    service.print_usuarios()


if __name__ == "__main__":
    main()