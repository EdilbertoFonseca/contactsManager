# Gestor de Contactos para NVDA

* **Autor**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Data de Criação**: 11/04/2024
* **Licença**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao complemento Gestor de Contactos para NVDA! Este é um plug-in desenvolvido especialmente para ajudar pessoas com deficiência visual a gerir a sua lista de contactos com maior facilidade e eficiência. Com este add-on, pode adicionar, editar e excluir contactos, bem como pesquisar nomes e informações de contacto de forma rápida e simples. Além disso, também oferecemos a possibilidade de exportar e importar a sua lista de contactos, para que a possa partilhar. O Gestor de Contactos para NVDA é fácil de usar e possui uma interface intuitiva, tornando-o a escolha ideal para quem precisa de gerir a sua lista de contactos de forma eficiente.

## Instalação

Aqui estão as instruções passo a passo para instalar o Gestor de Contactos para NVDA:

1. **Descarregue o ficheiro de instalação do add-on**: Obtenha o ficheiro na Loja de Complementos ou na página oficial do [Gestor de Contactos](https://github.com/EdilbertoFonseca/contactManager).
   **Nota**: Se o add-on for descarregado da loja, a instalação ocorrerá automaticamente. Caso contrário, siga as instruções abaixo.
2. **Instale o add-on**: Pressione Enter sobre o ficheiro do add-on descarregado.
3. **Siga as instruções no ecrã**: Complete a instalação conforme as orientações fornecidas.
4. **Reinicie o NVDA**: É necessário reiniciar para ativar o add-on.
5. **Verifique a instalação**: Pressione `NVDA+N` para abrir o menu do NVDA, vá até "Ferramentas" e verifique se o add-on Gestor de Contactos está listado.

Agora está pronto para usar o Gestor de Contactos para NVDA e guardar os seus contactos diretamente do NVDA.

## Definições

No menu Preferências, Configurações... do NVDA, na opção Gestor de Contactos para NVDA, pode configurar as seguintes opções:

1. Adicionar máscara para campos de telefone.
   Esta opção adiciona uma máscara usando o símbolo cardinal `#` para a formatação do número de telefone. Por defeito, os campos de telemóvel e telefone fixo estão formatados para o Brasil.
2. Exibir a opção de excluir toda a agenda, caixa de seleção desmarcada. `Alt+T`.
   Quando ativada, permite eliminar todo o conteúdo da agenda.
3. Exibir Importar ficheiro CSV, caixa de seleção desmarcada. `Alt+I`.
   Permite a importação de ficheiros CSV.
   Nota: Todos os campos devem ser compatíveis com o Gestor de Contactos.
4. Exibir Exportar ficheiro CSV, caixa de seleção desmarcada. `Alt+X`.
   Guarda todos os contactos da agenda num ficheiro CSV.
5. Caminho dos ficheiros da agenda.
   Permite seleccionar ou adicionar um diretório diferente do padrão para a base de dados.

## Utilização

Pode aceder ao Gestor de Contactos para NVDA de duas maneiras:

1. Usando o atalho `Windows+Alt+L`;
2. Através do menu do NVDA `NVDA+N`, Ferramentas, Gestor de Contactos.

Terá acesso à janela principal do add-on. Nesta janela pode registar, editar, remover e pesquisar contactos. Também inclui opções para importar CSV, exportar CSV e excluir toda a agenda. Estas três opções estão activadas por defeito e podem ser desactivadas no painel de configurações.

### Registar um Novo Contacto

Para registar um novo contacto:

1. Aceda ao Gestor de Contactos, menu do NVDA, Ferramentas, Gestor de Contactos, Gestor de Contactos, ou use o atalho `Windows+Alt+L`;
2. Na janela Lista de Contactos, pressione `Alt+N` para adicionar um novo contacto.
3. Na janela Novo Contacto, preencha todos os campos e pressione `Alt+O` para salvar ou `Alt+C` para sair sem salvar;
   >Nota: Para navegar entre os campos, basta pressionar a tecla "Enter". Também pode usar a tecla "Tab", mas ela pode apresentar um comportamento imprevisível devido a um problema que ainda não consegui identificar.

### Editar um Contacto

Para editar um contacto:

1. Selecione um contacto da lista;
2. Pressione `Alt+E` ou use a tecla `F2`.

A janela de edição será aberta, com o foco no campo do nome. Basta editar e pressionar `Alt+O` para salvar as alterações ou `Alt+C` para cancelar.
>Nota: Para navegar entre os campos, basta pressionar a tecla "Enter". Também pode usar a tecla "Tab", mas ela pode apresentar um comportamento imprevisível devido a um problema que ainda não consegui identificar.

### Pesquisar

Na janela Lista de Contactos, pode usar o campo de pesquisa para localizar um contacto específico.
Pode pesquisar pelos seguintes campos:

* Nome;
* Telemóvel;
* Telefone Fixo;
* E-mail.

Após seleccionar o campo, insira o item de pesquisa e pressione o atalho `Alt+P` para exibir os resultados na lista. Se nenhum resultado for encontrado, aparecerá uma mensagem informando que o item não foi encontrado. Para actualizar, use o atalho `Alt+A` ou a tecla `F5`.

## Dicas e Atalhos

### Janela Lista de Contactos

* **Botão Pesquisar**: `Alt+P`
* **Botão Editar**: `Alt+E` (também pode ser usada a tecla `F2`)
* **Botão Novo**: `Alt+N`
* **Botão Remover**: `Alt+R` (também pode ser usada a tecla `Delete`)
* **Botão Actualizar**: `Alt+A` (também pode ser usada a tecla `F5`)
* **Botão Importar CSV**: `Alt+I`
* **Botão Exportar CSV**: `Alt+X`
* **Botão Excluir todos os registos**: `Alt+T`
* **Botão Sair**: `Alt+S`

### Janela Novo Contacto e Edição

* **Confirmar operações**: `Alt+O`
* **Botão Cancelar**: `Alt+C`

>Todas as janelas do complemento Gestor de Contactos para NVDA podem ser fechadas com a tecla `Esc` ou `Alt+F4`.

## Agradecimentos

Este add-on foi inspirado na agenda criada por Abel Passos do Nascimento Jr. <abel.passos@gmail.com>, Rui Fontes <rui.fontes@tiflotecnia.com> e Ângelo Abrantes <ampa4374@gmail.com>.
