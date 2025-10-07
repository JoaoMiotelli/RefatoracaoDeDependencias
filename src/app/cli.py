from .repository import InMemoryUserRepository
from .email import FileEmailSender
from .api import JsonPlaceholderClient
from .usecases import add_user, list_users, deactivate_user, fetch_user_from_api

class CLI:
    def __init__(self):
        self.repo = InMemoryUserRepository()
        self.mailer = FileEmailSender()
        self.api = JsonPlaceholderClient()

    def _print_users(self):
        users = list_users(self.repo)
        print("\n=== Lista de Usuários ===")
        if not users:
            print("Nenhum usuário cadastrado.")
            return
        for u in users:
            status = "Ativo" if u.active else "Inativo"
            print(f"{u.id} - {u.name} ({u.email}) - {status}")
        print()

    def run(self):
        while True:
            print("\n=== Sistema de Usuários ===")
            print("1 - Adicionar usuário")
            print("2 - Listar usuários")
            print("3 - Desativar usuário")
            print("4 - Buscar usuário na API")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                name = input("Nome: ").strip()
                email = input("Email: ").strip()
                user = add_user(name, email, self.repo, self.mailer)
                print(f"Usuário {user.name} adicionado com sucesso!")
                self._print_users()

            elif opcao == "2":
                self._print_users()

            elif opcao == "3":
                try:
                    user_id = int(input("ID do usuário: "))
                    ok = deactivate_user(user_id, self.repo)
                    print("Usuário desativado." if ok else "Usuário não encontrado.")
                except ValueError:
                    print("ID inválido.")

            elif opcao == "4":
                try:
                    user_id = int(input("ID do usuário na API: "))
                    data = fetch_user_from_api(user_id, self.api)
                    if data:
                        print(f"Usuário encontrado: {data['name']} ({data['email']})")
                    else:
                        print("Usuário não encontrado na API.")
                except ValueError:
                    print("ID inválido.")

            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida!")