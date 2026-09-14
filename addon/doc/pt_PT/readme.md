# - Gestor de Contactos para o NVDA

* **Author**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Created on**: 11/04/2024
* **License**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao **Gestor de Contactos para o NVDA**!

Este extra foi desenvolvido especialmente para pessoas com deficiência visual que pretendem organizar e aceder aos seus contactos com autonomia, acessibilidade e facilidade.

Com esta ferramenta, é possível:

* Add, edit, delete, and search for contacts;
* Import and export contact lists in CSV format;
* Apply custom phone number formatting;
* Choose a custom location to store your contact database;
* Navigate an intuitive and fully keyboard-accessible interface.

## Instalação

1. No NVDA, abra o menu **Ferramentas** e aceda à **Loja de Extras**.
2. No separador **Complementos disponíveis**, utilize o campo **Pesquisa** e procure por `Contact Manager`.
3. Seleccione-o, prima Enter ou clique em Aplicar e, em seguida, seleccione Instalar.
4. Reinicie o NVDA para concluir a instalação.

Após a instalação, o extra estará pronto a ser utilizado.

Ao seleccionar um contacto na lista, os seus dados serão apresentados numa caixa de texto só de leitura. Pode navegar pela lista utilizando a primeira letra do nome.

## Definições

Aceda ao painel de definições em:
**Menu NVDA > Preferências > Definições... > Gestor de Contactos para o NVDA**

As seguintes opções estão disponíveis:

1. **Máscara para campos de telefone**.
2. **Mostrar opção para apagar todos os contactos** (`Alt+T`)
3. **Mostrar botão para importar ficheiro CSV** (`Alt+I`)
4. **Activar a exportação para CSV** (`Alt+X`): Apresenta um botão para exportar a lista de contactos para um ficheiro CSV.
5. **Caminho dos ficheiros da agenda**: Define a directoria onde a base de dados será guardada. Pode alterar este caminho.

## Aceder ao Extra

Pode aceder ao Gestor de Contactos das seguintes formas:

1. Atalho de teclado: `Windows+Alt+L`
2. Menu do NVDA: `NVDA+N > Ferramentas > Gestor de Contactos`

Na janela principal, pode:

* Add, edit, and delete contacts;
* Search for specific contacts;
* Import and export CSV files;
* Delete all records in the contact list (if enabled).

## Registar um Novo Contacto

1. Abra o Gestor de Contactos.
2. Prima `Alt+N` para adicionar um novo contacto.
3. Preencha os campos.
4. Prima Alt+O para guardar ou Alt+C para cancelar.Press `Alt+O` to save or `Alt+C` to cancel.

> **Nota:** Utilize **Enter** para navegar entre os campos.
> A tecla **Tab** pode comportar-se de forma imprevisível devido a um problema conhecido.

## Editar um Contacto

1. - Selecione um contacto da lista.
2. - Prima `Alt+E` ou `F2`.
3. - Faça as suas alterações.
4. - Prima `Alt+O` para guardar ou `Alt+C` para cancelar.

## Pesquisar Contactos

1. - Digite um termo de pesquisa (nome, telefone ou e-mail).
2. - Prima `Alt+P` para filtrar os resultados.
3. - Prima `Alt+A` ou `F5` para atualizar a lista completa.

> Se não for encontrado nenhum resultado, será exibida uma mensagem a informá-lo.

## Atalhos de Teclado

### Janela Principal

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

> Para **editar** ou **remover** um contacto, certifique-se de que o mesmo está selecionado na lista.
> Se nenhum contacto for selecionado, será apresentada uma mensagem de aviso.

### Janela Adicionar/Editar Contacto

| Action  | Shortcut |
| ------- | -------- |
| Confirm | `Alt+O`  |
| Cancel  | `Alt+C`  |

> Pode fechar todas as janelas com `Esc` ou `Alt+F4`.

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
