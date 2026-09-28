# Gerenciador de Contatos para NVDA

* **Autor**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Criado em**: 11/04/2024
* **Licença**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao **Gerenciador de Contatos para NVDA**!

Este complemento foi desenvolvido especialmente para pessoas com deficiência visual, permitindo organizar e acessar informações de contato com praticidade, acessibilidade e autonomia.

Com ele, você pode:

* Adicionar, editar, excluir e pesquisar contatos;
* Importar e exportar listas de contatos no formato CSV;
* Aplicar formatação personalizada de número de telefone;
* Escolher um local personalizado para armazenar seu banco de dados de contatos;
* Navegar por uma interface intuitiva e totalmente acessível por teclado.

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

* Adicionar, editar e excluir contatos;
* Pesquisar contatos específicos;
* Importar e exportar arquivos CSV;
* Excluir todos os registros da lista de contatos (se ativado).

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

| Ação                                      | Atalho            |
| ----------------------- | ------------------- |
| Adicionar novo contato  | `Alt+N`             |
| Editar contato selecionado | `Alt+E` ou `F2`     |
| Remover contato selecionado | `Alt+R` ou `Delete` |
| Pesquisar               | `Alt+P`             |
| Atualizar lista de contatos | `Alt+A` ou `F5`     |
| Importar arquivo CSV    | `Alt+I`             |
| Exportar para CSV       | `Alt+X`             |
| Excluir todos os contatos | `Alt+T`             |
| Sair                    | `Alt+S`             |

> Para **editar** ou **remover** um contato, certifique-se de que ele esteja selecionado na lista.
> Se nenhum contato for selecionado, uma mensagem de aviso será exibida.

### Janela Adicionar/Editar Contato

| Ação  | Atalho |
| ------- | -------- |
| Confirmar | `Alt+O`  |
| Cancelar | `Alt+C`  |

> Você pode fechar todas as janelas com `Esc` ou `Alt+F4`.

## Agradecimentos

Este add-on foi inspirado na Agenda Acessível, desenvolvida originalmente por:

* Rui Fontes (<rui.fontes@tiflotecnia.com>)
* Ângelo Abrantes (<ampa4374@gmail.com>)
* Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)

## Tradução

As traduções para este complemento são gerenciadas por meio do [projeto de complementos do NVDA no Crowdin](https://crowdin.com/project/nvdaaddons).

Para contribuir com uma tradução, crie uma conta no Crowdin, junte-se à equipe do idioma correspondente (se necessário) e traduza as strings de interface e documentação disponíveis diretamente no Crowdin.

Você também pode usar o Poedit para trabalhar localmente com arquivos `.po` e `.xliff`. As traduções concluídas são sincronizadas com o repositório do complemento por meio do fluxo de trabalho de localização.

Para dúvidas ou assistência, junte-se à [lista de discussão de traduções do NVDA](https://groups.io/g/nvda-translations).
