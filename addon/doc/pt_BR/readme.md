# Gerenciador de Contatos para NVDA

* **Author**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Created on**: 11/04/2024
* **License**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao **Gerenciador de Contatos para NVDA**!

Este complemento foi desenvolvido especialmente para pessoas com deficiência visual, permitindo organizar e acessar informações de contato com praticidade, acessibilidade e autonomia.

Com ele, você pode:

* Add, edit, delete, and search for contacts;
* Import and export contact lists in CSV format;
* Apply custom phone number formatting;
* Choose a custom location to store your contact database;
* Navigate an intuitive and fully keyboard-accessible interface.

## Instalação

1. No NVDA, abra o menu **Ferramentas** e acesse a **Loja de Complementos**.
2. Na aba **Complementos Disponíveis**, digite "Gerenciador de Contatos" no campo de busca.
3. Selecione o complemento e pressione **Enter** ou clique em **Aplicar**, depois escolha **Instalar**.
4. Reinicie o NVDA para concluir a instalação.

Após a instalação, o complemento está pronto para uso.

Ao selecionar um contato na lista, os detalhes dele serão exibidos em uma caixa de texto somente leitura. Você pode navegar pela lista usando a primeira letra do nome do contato.

## Configuração

Acesse o painel de configurações em:
**Menu NVDA > Preferências > Configurações > Gerenciador de Contatos para NVDA**

Opções disponíveis:

1. **Máscara para número de telefone**: Use `#` para aplicar uma máscara de formatação (por exemplo, para números brasileiros).
2. **Exclusão completa da agenda** (`Alt+T`) Permite remover todos os contatos de uma só vez.
3. **Importação de contatos via CSV** (`Alt+I`) Permite importar contatos de arquivos CSV compatíveis.
4. **Exportação da agenda para CSV** (`Alt+X`) Exporta todos os contatos para um arquivo CSV.
5. **Caminho do banco de dados** Define um diretório personalizado para salvar os dados da agenda.

## Acessando o complemento

Você pode abrir o Gerenciador de Contatos de duas maneiras:

1. Atalho de teclado: `Windows+Alt+L`
2. Menu NVDA: `NVDA+N > Ferramentas > Gerenciador de Contatos`

Na janela principal, você pode:

* Add, edit, and delete contacts;
* Search for specific contacts;
* Import and export CSV files;
* Delete all records in the contact list (if enabled).

## Adicionar um novo contato

1. Abra o Gerenciador de Contatos (pressione `Windows+Alt+L` ou através do menu).
2. Pressione `Alt+N` para adicionar um novo contato.
3. Preencha os campos.
4. Pressione `Alt+O` para salvar ou `Alt+C` para cancelar.

> **Nota:** Use a tecla **Enter** para navegar entre os campos.
A tecla **Tab** pode apresentar comportamento imprevisível devido a um problema conhecido.

## Editar um contato

1. Selecione um contato na lista.
2. Pressione `Alt+E` ou `F2`.
3. Faça as alterações.
4. Pressione `Alt+O` para salvar ou `Alt+C` para cancelar.

## Pesquisando contatos

1. Digite um termo de pesquisa (nome, telefone ou e-mail).
2. Pressione `Alt+P` para filtrar os resultados.
3. Pressione `Alt+A` ou `F5` para atualizar a lista completa.

Se nenhuma correspondência for encontrada, você será informado.

## Atalhos de teclado

### Janela principal

| Action                  | Shortcut            |
| ----------------------- | ------------------- |
| Add new contact         | `Alt+N`             |
| Edit selected contact   | `Alt+E` or `F2`     |
| Remove selected contact | `Alt+R` or `Delete` |
| Search                  | `Alt+P`             |
| Refresh contact list    | `Alt+A` or `F5`     |
| Import CSV file         | `Alt+I`             |
| Export to CSV           | `Alt+X`             |
| Delete all contacts     | `Alt+T`             |
| Exit                    | `Alt+S`             |

> Para **editar** ou **remover** um contato, certifique-se de que ele esteja selecionado na lista.
> Se nenhum contato for selecionado, uma mensagem de aviso será exibida.

### Janela Adicionar/Editar Contato

| Action  | Shortcut |
| ------- | -------- |
| Confirm | `Alt+O`  |
| Cancel  | `Alt+C`  |

> Você pode fechar todas as janelas com `Esc` ou `Alt+F4`.

## Agradecimentos

This add-on was inspired by the Accessible Agenda, originally developed by:

* Rui Fontes (<rui.fontes@tiflotecnia.com>)
* Ângelo Abrantes (<ampa4374@gmail.com>)
* Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)

## Translation

Translations for this add-on are managed through the [NVDA Add-ons Crowdin project](https://crowdin.com/project/nvdaaddons).

To contribute a translation, create a Crowdin account, join the appropriate language team if required, and translate the available interface and documentation strings directly in Crowdin.

You can also use Poedit to work with `.po` and `.xliff` files locally. Completed translations are synchronized to the add-on repository through the localization workflow.

For questions or assistance, please join the [NVDA Translations mailing list](https://groups.io/g/nvda-translations).
