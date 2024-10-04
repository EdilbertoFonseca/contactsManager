# Gerenciador de contatos para NVDA

* **Autor**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Data de Criação**: 11/04/2024
* **Licença**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao complemento Gerenciador de contatos para NVDA! Este é um plug-in especialmente desenvolvido para ajudar pessoas com deficiência visual a gerenciar sua lista de contatos com mais facilidade e eficiência. Com este Addon você pode adicionar, editar e excluir contatos, bem como pesquisar nomes e informações de contato de forma rápida e simples. Além disso, também oferecemos a possibilidade de exportar e importar sua lista de contatos, para que você possa compartilhá-la. O Gerenciador de contatos para NVDA é fácil de usar e oferece uma interface intuitiva, tornando-o a escolha ideal para quem precisa gerenciar sua lista de contatos com eficiência.

## Instalação

Aqui estão as instruções passo a passo para instalar o Gerenciador de contatos para NVDA:

1. **Baixe o arquivo de instalação do add-on**: Obtenha o arquivo da Loja de Complementos ou da página oficial do [Gerenciador de contatos](https://github.com/EdilbertoFonseca/contactManager).
   **Nota**: Se o add-on for baixado da loja, a instalação ocorrerá automaticamente. Caso contrário, siga as instruções abaixo.
2. **Instale o add-on**: Pressione Enter sobre o arquivo do add-on baixado.
3. **Siga as instruções na tela**: Complete a instalação conforme as orientações fornecidas.
4. **Reinicie o NVDA**: É necessário reiniciar para ativar o add-on.
5. **Verifique a instalação**: Pressione "NVDA + N" para abrir o menu do NVDA, vá até "Ferramentas" e verifique se o add-on Gerenciador de contatos está listado.

Agora você está pronto para usar o Gerenciador de contatos para NVDA e salvar seus contatos diretamente do NVDA. Certifique-se de verificar a documentação do complemento para obter informações adicionais sobre como usá-lo e personalizá-lo de acordo com suas necessidades.

## Configurações

No menu Preferências, Configurações... do NVDA na opção Gerenciador de contatos para NVDA. Você pode configurar as seguintes opções:

1. Adicionar máscara para campos de telefone.
   Esta opção adiciona a máscara usando o símbolo cardinal `#` para a formatação do número de telefone. Por padrão, os campos de celular e telefone fixo estão formatados para o Brasil.
2. Exibir a opção de excluir toda a agenda, caixa de seleção desmarcada. Alt+e.
   Quando habilitada, permite deletar todo o conteúdo da agenda.
3. Exibir Importar arquivo CSV, caixa de seleção desmarcada. Alt+e.
   Permite a importação de arquivos csv. Obs: todos os campos devem ser compatíveis com o Gerenciador de contatos.
4. Exibir Exportar arquivo CSV, caixa de seleção desmarcada. Alt+e.
   Salva todos os contatos da agenda em um arquivo csv.
5. Caminho dos arquivos da agenda.
   Permite selecionar ou adicionar um diretório diferente do padrão para o banco de dados.

## Uso

Você pode acessar o Gerenciador de contatos para NVDA de duas maneiras:

1. Pelo atalho, Windows+Alt+L;
2. Através do menu do NVDA (NVDA+N) ferramentas Gerenciador de contatos.

Você terá acesso à janela principal do addon. Nesta janela você pode registrar, editar, remover e pesquisar contatos. Ele também tem as opções de importar csv, exportar csv e excluir toda a agenda. Essas três opções estão ativadas por padrão. Podendo ser desativadas no painel de configuração.

### Cadastrando um novo contato

Para registrar um novo contato:

1. Acesse o Gerenciador de contatos, menu do NVDA, Ferramentas, Gerenciador de contatos, Gerenciador de contatos. ou por atalho (windows+Alt+L);
2. Na janela Lista de contatos, pressione Alt+N para adicionar um novo contato.
3. Na janela Novo Contato, preencha todos os campos e pressione Alt+E para salvar e Alt+F para sair sem salvar;

### Editando um contato

Para editar um contato:

1. Selecione um contato da lista;
2. Pressione ALT+E;

A janela de edição será aberta com foco no campo do nome. Basta editar e pressionar ALT+E para salvar as alterações ou ALT+F para cancelar.

### Pesquisar

Na janela Lista de contatos, você pode usar o campo de pesquisa para localizar um contato específico.
Você pode pesquisar pelos campos:

* Nome;
* Celular;
* Telefone Fixo;
* E-mail.

Após selecionar o campo, basta informar o item de busca, e pressionar o atalho ALT+P, que exibirá o resultado da busca na lista. Se nada for retornado, uma mensagem será exibida informando que o item não foi encontrado. Basta atualizar usando o atalho ALT+A.

## Dicas e Atalhos

### Janela Lista de contatos

* Botão Buscar Alt+P
* Botão Editar Alt+E
* Novo botão Alt+N
* Remover botão Alt+R
* Botão Atualizar Alt+A
* Importar csv... Botão Alt+I
* Exportar csv... Botão Alt+X
* Excluir todos os registros. Botão Alt+T
* Botão Sair Alt+S

### Janela novo contato e edição

* Adicionar contato botão Alt+O
* Botão Fechar Alt+C

Todas as janelas do complemento Gerenciador de contatos para NVDA podem ser fechadas com a tecla Esc ou alt+f4.

## Agradecimentos

Este addon foi inspirado na agenda criada por Abel Passos do Nascimento Jr. <abel.passos@gmail.com>, Rui Fontes <rui.fontes@tiflotecnia.com> e Ângelo Abrantes <ampa4374@gmail.com>.

[1]: https://www.gnu.org/licenses/gpl-2.0.html
