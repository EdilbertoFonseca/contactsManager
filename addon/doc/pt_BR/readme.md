# Gerenciador de Contatos para NVDA

- **Autor**: Edilberto Fonseca (<edilberto.fonseca@outlook.com>)  
- **Data de Criação**: 11/04/2024  
- **Licença**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao **Gerenciador de Contatos para NVDA**!

Este complemento foi desenvolvido para ajudar pessoas com deficiência visual a gerenciar sua lista de contatos de forma prática, acessível e eficiente. Com ele, você pode:

- Adicionar, editar e excluir contatos;
- Pesquisar nomes e dados de contato rapidamente;
- Importar e exportar contatos em formato CSV, facilitando o backup e o compartilhamento.

O Gerenciador de Contatos oferece uma interface simples e intuitiva, sendo uma ferramenta útil para quem busca facilidade no gerenciamento de contatos dentro do NVDA.

## Instalação

1. No NVDA, abra o menu **Ferramentas** e acesse a **Loja de Complementos**.
2. Na aba **Complementos Disponíveis**, utilize o campo **Procurar**.
3. Digite `contactsManager`. Quando o resultado aparecer, pressione **Enter** ou clique em **Aplicar** e depois selecione **Instalar**.
4. Reinicie o NVDA para concluir a instalação.

Após isso, o complemento estará pronto para uso.

Ao selecionar um contato na lista, suas informações serão exibidas em uma caixa de texto somente leitura. É possível navegar pela lista utilizando a primeira letra do nome do contato.

## Configurações

Acesse o painel de configurações do complemento em:  
**Menu NVDA > Preferências > Configurações... > Gerenciador de Contatos para NVDA**.

As seguintes opções estão disponíveis:

1. **Adicionar máscara para campos de telefone**  
   Aplica uma máscara utilizando o símbolo `#` para formatar os números de telefone. A máscara padrão segue o formato brasileiro.

2. **Mostrar opção para excluir todos os contatos** (`Alt+T`)  
   Quando habilitada, permite remover toda a agenda com um único comando.

3. **Mostrar botão de importação de arquivo CSV** (`Alt+I`)  
   Permite importar contatos de um arquivo CSV.  
   > Obs: Os campos do arquivo devem ser compatíveis com o formato do Gerenciador de Contatos.

4. **Mostrar botão para exportar arquivo CSV** (`Alt+X`)  
   Exporta todos os contatos da agenda para um arquivo CSV.

5. **Caminho dos arquivos da agenda**  
   Define o diretório onde o banco de dados de contatos será salvo. É possível alterar o caminho padrão.

## Uso

Você pode abrir o Gerenciador de Contatos das seguintes maneiras:

1. Atalho de teclado: `Windows+Alt+L`
2. Menu do NVDA: `NVDA+N > Ferramentas > Gerenciador de Contatos > Gerenciador de Contatos`

A janela principal do complemento permite:

- Registrar, editar e excluir contatos;
- Pesquisar por contatos;
- Importar e exportar arquivos CSV;
- Excluir todos os registros da agenda (opcional).

As opções de importação, exportação e exclusão em massa estão ativadas por padrão, mas podem ser desabilitadas nas configurações.

### Cadastrando um Novo Contato

1. Abra o Gerenciador de Contatos (`Windows+Alt+L` ou via menu do NVDA).
2. Na janela da lista de contatos, pressione `Alt+N` para adicionar um novo contato.
3. Preencha os campos e pressione `Alt+O` para salvar ou `Alt+C` para cancelar.

> **Observação**:  
> Para navegar entre os campos, recomenda-se o uso da tecla `Enter`. Embora o `Tab` também funcione, pode apresentar comportamento imprevisível devido a uma limitação ainda não solucionada.

### Editando um Contato

1. Selecione um contato da lista.
2. Pressione `Alt+E` ou `F2` para abrir a janela de edição.
3. Após modificar os dados, pressione `Alt+O` para salvar ou `Alt+C` para cancelar.

> **Observação**:  
> A navegação entre os campos funciona da mesma forma que na janela de novo contato.

### Pesquisa

Na janela da lista de contatos:

1. Utilize o campo de pesquisa para localizar contatos pelos seguintes campos:
   - Nome
   - Celular
   - Telefone Fixo
   - E-mail
2. Após digitar o termo de busca, pressione `Alt+P` para filtrar os resultados.
3. Para atualizar a lista e limpar a busca, pressione `Alt+A` ou `F5`.

Caso o contato não seja encontrado, uma mensagem informará que o item não está na agenda.

## Dicas e Atalhos

### Janela da Lista de Contatos

| Ação                        | Atalho              |
|-----------------------------|---------------------|
| Pesquisar                   | `Alt+P`             |
| Editar                      | `Alt+E` ou `F2`     |
| Novo contato                | `Alt+N`             |
| Remover contato             | `Alt+R` ou `Delete` |
| Atualizar lista             | `Alt+A` ou `F5`     |
| Importar CSV                | `Alt+I`             |
| Exportar CSV                | `Alt+X`             |
| Excluir todos os contatos   | `Alt+T`             |
| Sair                        | `Alt+S`             |

> **Importante:**  
> Para **editar** ou **remover** um contato, ele precisa estar **previamente selecionado na lista**.  
> Caso nenhuma seleção tenha sido feita, uma mensagem será exibida informando que **nenhum contato foi selecionado**.

### Janela de Novo Contato / Edição

| Ação              | Atalho    |
|-------------------|-----------|
| Confirmar         | `Alt+O`   |
| Cancelar          | `Alt+C`   |

> **Dica:**  
> Todas as janelas do Gerenciador de Contatos podem ser fechadas com `Esc` ou `Alt+F4`.

## Agradecimentos

Este complemento foi inspirado na agenda criada por:

- Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)  
- Rui Fontes (<rui.fontes@tiflotecnia.com>)  
- Ângelo Abrantes (<ampa4374@gmail.com>)
