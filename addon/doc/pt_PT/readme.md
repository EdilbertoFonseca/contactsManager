# Gestor de Contactos para NVDA

* **Autor**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Data de Criação**: 11/04/2024
* **Licença**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao complemento Gestor de Contactos para NVDA! Este é um plug-in especialmente desenvolvido para ajudar pessoas com deficiência visual a gerir a sua lista de contactos com mais facilidade e eficiência. Com este add-on, pode adicionar, editar e eliminar contactos, assim como pesquisar nomes e informações de contacto de forma rápida e simples. Além disso, também oferecemos a possibilidade de exportar e importar a sua lista de contactos, para que possa partilhá-la. O Gestor de Contactos para NVDA é fácil de usar e oferece uma interface intuitiva, tornando-o a escolha ideal para quem precisa de gerir a sua lista de contactos de forma eficiente.

## Instalação

Aqui estão as instruções passo a passo para instalar o Gestor de Contactos para NVDA:

1. **Descarregue o ficheiro de instalação do add-on**: Obtenha o ficheiro na Loja de Complementos ou na página oficial do [Gestor de Contactos](https://github.com/EdilbertoFonseca/contactManager).
   **Nota**: Se o add-on for descarregado da loja, a instalação ocorrerá automaticamente. Caso contrário, siga as instruções abaixo.
2. **Instale o add-on**: Pressione Enter sobre o ficheiro do add-on descarregado.
3. **Siga as instruções no ecrã**: Complete a instalação conforme as orientações fornecidas.
4. **Reinicie o NVDA**: É necessário reiniciar para ativar o add-on.
5. **Verifique a instalação**: Pressione "NVDA + N" para abrir o menu do NVDA, vá até "Ferramentas" e verifique se o add-on Gestor de Contactos está listado.

Agora está pronto para usar o Gestor de Contactos para NVDA e salvar os seus contactos diretamente do NVDA. Certifique-se de consultar a documentação do complemento para obter informações adicionais sobre como utilizá-lo e personalizá-lo de acordo com as suas necessidades.

## Configurações

No menu Preferências, Configurações... do NVDA, na opção Gestor de Contactos para NVDA, pode configurar as seguintes opções:

1. Adicionar máscara para campos de telefone.
   Esta opção adiciona a máscara usando o símbolo cardinal `#` para a formatação do número de telefone. Por padrão, os campos de telemóvel e telefone fixo estão formatados para o Brasil.
2. Exibir a opção de excluir toda a agenda, caixa de seleção desmarcada. Alt + e.
   Quando habilitada, permite eliminar todo o conteúdo da agenda.
3. Exibir Importar ficheiro CSV, caixa de seleção desmarcada. Alt + e.
   Permite a importação de ficheiros CSV.
   Nota: Todos os campos devem ser compatíveis com o Gestor de Contactos.
4. Exibir Exportar ficheiro CSV, caixa de seleção desmarcada. Alt + e.
   Salva todos os contactos da agenda num ficheiro CSV.
5. Caminho dos ficheiros da agenda.
   Permite selecionar ou adicionar um diretório diferente do padrão para a base de dados.

## Uso

Pode aceder ao Gestor de Contactos para NVDA de duas maneiras:

1. Pelo atalho, Windows + Alt + L;
2. Através do menu do NVDA (NVDA + N) Ferramentas > Gestor de Contactos.

Terá acesso à janela principal do add-on. Nesta janela, pode registar, editar, remover e pesquisar contactos. Ele também tem as opções de importar CSV, exportar CSV e excluir toda a agenda. Estas três opções estão ativadas por padrão, podendo ser desativadas no painel de configuração.

### Cadastrando um novo contacto

Para registar um novo contacto:

1. Aceda ao Gestor de Contactos através do menu do NVDA, Ferramentas, Gestor de Contactos, ou por atalho (Windows + Alt + L);
2. Na janela Lista de Contactos, pressione Alt + N para adicionar um novo contacto.
3. Na janela Novo Contacto, preencha todos os campos e pressione Alt + O para salvar e Alt + C para sair sem salvar;

### Editando um contacto

Para editar um contacto:

1. Selecione um contacto da lista;
2. Pressione ALT + E ou utilize a tecla F2.

A janela de edição será aberta com foco no campo do nome. Basta editar e pressionar ALT + O para salvar as alterações ou ALT + C para cancelar.

### Pesquisar

Na janela Lista de Contactos, pode usar o campo de pesquisa para localizar um contacto específico.
Pode pesquisar pelos campos:

* Nome;
* Telemóvel;
* Telefone Fixo;
* E-mail.

Após selecionar o campo, informe o item de busca e pressione o atalho ALT + P para exibir os resultados na lista. Se nenhum resultado for encontrado, uma mensagem aparecerá informando que o item não foi encontrado. Para atualizar, utilize o atalho ALT + A ou a tecla F5.

## Dicas e Atalhos

### Janela Lista de Contactos

* **Botão Buscar:** ALT + P
* **Botão Editar:** ALT + E (também pode ser utilizado a tecla F2)
* **Novo Botão:** ALT + N
* **Remover Botão:** ALT + R (também pode ser utilizado a tecla Delete)
* **Botão Atualizar:** ALT + A (também pode ser utilizado a tecla F5)
* **Importar CSV:** ALT + I
* **Exportar CSV:** ALT + X
* **Excluir todos os registos:** ALT + T
* **Botão Sair:** ALT + S

### Janela Novo Contacto e Edição

* **Confirmar operações:** ALT + O
* **Botão Cancelar:** ALT + C

>Todas as janelas do complemento Gestor de Contactos para NVDA podem ser fechadas com a tecla Esc ou Alt + F4.

## Agradecimentos

Este add-on foi inspirado na agenda criada por Abel Passos do Nascimento Jr. <abel.passos@gmail.com>, Rui Fontes <rui.fontes@tiflotecnia.com> e Ângelo Abrantes <ampa4374@gmail.com>.
