# Gestor de Contactos para NVDA

* **Autor**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Data de Criação**: 11/04/2024
* **Licença**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao Gestor de Contactos para NVDA! Este complemento foi especialmente desenvolvido para ajudar pessoas com deficiência visual a gerir as suas listas de contactos de forma mais fácil e eficiente. Com este complemento, pode adicionar, editar e eliminar contactos, bem como pesquisar nomes e informações de contacto de forma rápida e simples. Adicionalmente, oferecemos a possibilidade de exportar e importar a sua lista de contactos, permitindo que a partilhe. O Gestor de Contactos para NVDA é fácil de usar e apresenta uma interface intuitiva, tornando-se a escolha ideal para quem precisa de gerir os seus contactos com eficiência.

## Instalação

Aqui estão as instruções passo a passo para instalar o Gestor de Contactos para NVDA:

1. **Descarregue o ficheiro de instalação do complemento**: Obtenha o ficheiro a partir da Loja de Complementos ou da página oficial do [Gestor de Contactos](https://github.com/EdilbertoFonseca/contactManager).
   **Nota**: Se o complemento for descarregado da loja, a instalação será feita automaticamente. Caso contrário, siga as instruções abaixo.
2. **Instale o complemento**: Pressione Enter no ficheiro do complemento que descarregou.
3. **Siga as instruções no ecrã**: Complete a instalação conforme as orientações fornecidas.
4. **Reinicie o NVDA**: É necessário reiniciar para ativar o complemento.
5. **Verifique a instalação**: Pressione `NVDA+N` para abrir o menu do NVDA, navegue até "Ferramentas" e verifique se o complemento Gestor de Contactos está listado.

Agora está pronto para utilizar o Gestor de Contactos para NVDA e guardar os seus contactos diretamente no NVDA.

## Configurações

No menu do NVDA, Preferências > Configurações > Gestor de Contactos para NVDA, pode configurar as seguintes opções:

1. Adicionar máscara aos campos de telefone.
   Esta opção adiciona uma máscara utilizando o símbolo cardinal `#` para a formatação do número de telefone. Por padrão, os campos de telemóvel e telefone fixo estão formatados para Portugal.
2. Mostrar opção para eliminar todo o calendário, caixa de seleção marcada `Alt+t`.
   Quando ativada, permite eliminar todo o conteúdo do calendário.
3. Mostrar botão de importação de ficheiro CSV, caixa de seleção marcada `Alt+I`.
   Permite a importação de ficheiros CSV.
   Nota: Todos os campos devem ser compatíveis com o Gestor de Contactos.
4. Mostrar botão de exportação de ficheiro CSV, caixa de seleção marcada `Alt+X`.
   Guarda todos os contactos do calendário num ficheiro CSV.
5. Caminho dos ficheiros do calendário.
   Permite selecionar ou adicionar um diretório diferente do padrão para a base de dados.

## Utilização

Pode aceder ao Gestor de Contactos para NVDA de duas maneiras:

1. Através do atalho, `Windows+Alt+L`;
2. Pelo menu do NVDA: `NVDA+N` > Ferramentas > Gestor de Contactos.

Terá acesso à janela principal do complemento. Nesta janela, pode registar, editar, remover e pesquisar contactos. Também inclui as opções de importar CSV, exportar CSV e eliminar todo o calendário. Estas três opções estão ativadas por padrão, mas podem ser desativadas no painel de configurações.

### Registar um novo contacto

Para registar um novo contacto:

1. Aceda ao Gestor de Contactos: Menu do NVDA > Ferramentas > Gestor de Contactos, ou pelo atalho `Windows+Alt+L`;
2. Na janela Lista de Contactos, pressione `Alt+N` para adicionar um novo contacto;
3. Na janela Novo Contacto, preencha todos os campos e pressione `Alt+O` para guardar ou `Alt+C` para sair sem guardar.
   > **Nota**: Para navegar entre os campos, pressione a tecla "Enter". Também pode utilizar a tecla "Tab", mas esta pode apresentar um comportamento imprevisível devido a um problema que ainda não consegui identificar.

### Editar um contacto

Para editar um contacto:

1. Selecione um contacto da lista;
2. Pressione `Alt+E` ou utilize a tecla `F2`.

A janela de edição será aberta com o foco no campo do nome. Basta editar os campos e pressionar `Alt+O` para guardar as alterações ou `Alt+C` para cancelar.
> **Nota**: Para navegar entre os campos, pressione a tecla "Enter". Também pode utilizar a tecla "Tab", mas esta pode apresentar um comportamento imprevisível devido a um problema que ainda não consegui identificar.

### Pesquisar

Na janela Lista de Contactos, pode utilizar o campo de pesquisa para localizar um contacto específico.
Pode pesquisar pelos seguintes campos:

* Nome;
* Telemóvel;
* Telefone fixo;
* Email.

Depois de selecionar o campo, introduza o termo de pesquisa e pressione o atalho `Alt+P` para exibir os resultados na lista. Se não forem encontrados resultados, aparecerá uma mensagem a informar que o item não foi encontrado. Para atualizar, utilize o atalho `Alt+A` ou a tecla `F5`.

## Dicas e Atalhos

### Janela Lista de Contactos

* **Botão Pesquisar**: `Alt+P`
* **Botão Editar**: `Alt+E` (também pode utilizar a tecla `F2`)
* **Botão Novo**: `Alt+N`
* **Botão Remover**: `Alt+R` (também pode utilizar a tecla Delete)
* **Botão Atualizar**: `Alt+A` (também pode utilizar a tecla `F5`)
* **Botão Importar CSV**: `Alt+I`
* **Botão Exportar CSV**: `Alt+X`
* **Botão Eliminar todos os registos**: `Alt+T`
* **Botão Sair**: `Alt+S`

### Janela Novo Contacto e Edição

* **Confirmar operações**: `Alt+O`
* **Botão Cancelar**: `Alt+C`

> Todas as janelas do complemento Gestor de Contactos para NVDA podem ser fechadas utilizando a tecla `Esc` ou `Alt+F4`.

## Agradecimentos

Este complemento foi inspirado na agenda criada por Abel Passos do Nascimento Jr. <abel.passos@gmail.com>, Rui Fontes <rui.fontes@tiflotecnia.com> e Ângelo Abrantes <ampa4374@gmail.com>.
