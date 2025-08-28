class Livro:
  def __init__(self,titulo,autor,ano,disponivel=True):
    self.titulo = titulo
    self.autor = autor
    self.ano = ano
    self.disponivel = disponivel

  def __str__(self):
    status = "Disponível" if self.disponivel else "Indisponível"
    return f"{self.titulo} - {self.autor} ({self.ano}) - {status}"

class Biblioteca:
  def __init__(self):
    self.livros = []

  def adicionar_livros(self,titulo,autor,ano):
    livro = Livro(titulo,autor,ano)
    self.livros.append(livro)

  def emprestar_livro(self,titulo):
    for livro in self.livros:
      if livro.titulo == titulo:
        if livro.disponivel:
          livro.disponivel = False
          print (f"O livro {titulo} foi emprestado")
        else:
          print(f"O livro '{titulo}' não está disponível.")
        return
    print (f"O livro {titulo} não existe na biblioteca")

  def devolver_livro(self,titulo):
    for livro in self.livros:
      if livro.titulo == titulo:
        if not livro.disponivel:
          livro.disponivel = True
          print (f"O livro {titulo} foi devolvido")

        else:
          print (f"O livro {titulo} já esta disponivel")  
        return
    print(f"O livro '{titulo}' não existe na biblioteca.")

  def listar_livro(self):
    print("=== Lista de livros ===")
    for livro in self.livros:
      print(livro)


biblioteca = Biblioteca()


while True:
  print("\n=== Biblioteca ===")
  print("1. Adicionar livro")
  print("2. Listar livros disponíveis")
  print("3. Emprestar livro")
  print("4. Devolver livro")
  print("5. Sair")

  escolha = (input("Escolha uma opção: "))

  if escolha == "1":
    titulo = input("Digite o titulo do livro: ").strip().title()
    autor = input("Digite o autor: ").strip().title()
    ano = int(input("Digite o ano: "))
    biblioteca.adicionar_livros(titulo,autor,ano)

  elif escolha == "2":
    biblioteca.listar_livro()
  
  elif escolha == "3":
    titulo = input("Digite o titulo do livro: ").strip().title()
    biblioteca.emprestar_livro(titulo)

  elif escolha == "4":
    titulo = input("Digite o titulo do livro: ").strip().title()
    biblioteca.devolver_livro(titulo)
  
  elif escolha == "5":
    print("Saindo da biblioteca")
    break

  else:
    print("Valor invalido")