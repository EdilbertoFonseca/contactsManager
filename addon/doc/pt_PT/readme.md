# Gestor de Contactos para NVDA

- **Autor**: Edilberto Fonseca (<edilberto.fonseca@outlook.com>)  
- **Data de Criação**: 11/04/2024  
- **Licença**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao **Gestor de Contactos para NVDA**!

Este extra foi desenvolvido para ajudar pessoas com deficiência visual a gerir a sua lista de contactos de forma prática, acessível e eficiente. Com esta ferramenta, é possível:

- Adicionar, editar e remover contactos;
- Pesquisar nomes e dados de contacto rapidamente;
- Importar e exportar contactos em formato CSV, facilitando cópias de segurança e partilhas.

O Gestor de Contactos oferece uma interface simples e intuitiva, sendo uma ferramenta útil para quem procura facilidade na gestão de contactos no NVDA.

## Instalação

1. No NVDA, abra o menu **Ferramentas** e aceda à **Loja de Extras**.
2. Na aba **Extras Disponíveis**, utilize o campo **Procurar**.
3. Escreva `contactsManager`. Quando o resultado aparecer, pressione **Enter** ou clique em **Aplicar** e seleccione **Instalar**.
4. Reinicie o NVDA para concluir a instalação.

Depois disso, o extra estará pronto a ser utilizado.

Ao seleccionar um contacto na lista, as suas informações serão apresentadas numa caixa de texto só de leitura. Pode navegar na lista utilizando a primeira letra do nome do contacto.

## Definições

Aceda ao painel de definições do extra em:  
**Menu NVDA > Preferências > Definições... > Gestor de Contactos para NVDA**.

As seguintes opções estão disponíveis:

1. **Adicionar máscara aos campos de telefone**  
   Aplica uma máscara utilizando o símbolo `#` para formatar os números de telefone. A máscara padrão segue o formato português do Brasil.

2. **Mostrar opção para apagar todos os contactos** (`Alt+T`)  
   Quando ativada, permite eliminar toda a agenda de contactos com um só comando.

3. **Mostrar botão para importar ficheiro CSV** (`Alt+I`)  
   Permite importar contactos a partir de um ficheiro CSV.  
   > Nota: Os campos do ficheiro devem ser compatíveis com o formato do Gestor de Contactos.

4. **Mostrar botão para exportar ficheiro CSV** (`Alt+X`)  
   Exporta todos os contactos da agenda para um ficheiro CSV.

5. **Caminho dos ficheiros da agenda**  
   Define o diretório onde será guardada a base de dados de contactos. Pode alterar o caminho padrão.

## Utilização

Pode abrir o Gestor de Contactos das seguintes formas:

1. Atalho de teclado: `Windows+Alt+L`  
2. Menu do NVDA: `NVDA+N > Ferramentas > Gestor de Contactos > Gestor de Contactos`

Na janela principal do extra, pode:

- Registar, editar e eliminar contactos;
- Pesquisar contactos;
- Importar e exportar ficheiros CSV;
- Apagar todos os registos da agenda (opcional).

As opções de importação, exportação e eliminação total estão ativadas por padrão, podendo ser desativadas nas definições.

### Registar um Novo Contacto

1. Abra o Gestor de Contactos (`Windows+Alt+L` ou via menu do NVDA).
2. Na janela da lista de contactos, pressione `Alt+N` para adicionar um novo contacto.
3. Preencha os campos e pressione `Alt+O` para guardar ou `Alt+C` para cancelar.

> **Nota:**  
> Para navegar entre os campos, recomenda-se a utilização da tecla `Enter`. Embora o `Tab` também funcione, pode apresentar um comportamento imprevisível devido a uma limitação ainda por resolver.

### Editar um Contacto

1. Seleccione um contacto da lista.
2. Pressione `Alt+E` ou `F2` para abrir a janela de edição.
3. Após alterar os dados, pressione `Alt+O` para guardar ou `Alt+C` para cancelar.

> **Nota:**  
> A navegação entre os campos funciona da mesma forma que na janela de novo contacto.

### Pesquisa

Na janela da lista de contactos:

1. Utilize o campo de pesquisa para localizar contactos pelos seguintes campos:
   - Nome
   - Telemóvel
   - Telefone fixo
   - E-mail
2. Após introduzir o termo de pesquisa, pressione `Alt+P` para filtrar os resultados.
3. Para atualizar a lista e limpar a pesquisa, pressione `Alt+A` ou `F5`.

Se o contacto não for encontrado, será apresentada uma mensagem a informar que o item não foi localizado.

## Dicas e Atalhos

### Janela da Lista de Contactos

| Ação                        | Atalho              |
|-----------------------------|---------------------|
| Pesquisar                   | `Alt+P`             |
| Editar                      | `Alt+E` ou `F2`     |
| Novo contacto               | `Alt+N`             |
| Remover contacto            | `Alt+R` ou `Delete` |
| Atualizar lista             | `Alt+A` ou `F5`     |
| Importar CSV                | `Alt+I`             |
| Exportar CSV                | `Alt+X`             |
| Apagar todos os contactos   | `Alt+T`             |
| Sair                        | `Alt+S`             |

> **Importante:**  
> Para **editar** ou **remover** um contacto, é necessário que esteja **previamente selecionado na lista**.  
> Caso nenhum contacto esteja selecionado, será apresentada uma mensagem a indicar que **nenhum contacto foi selecionado**.

### Janela de Novo Contacto / Edição

| Ação              | Atalho    |
|-------------------|-----------|
| Confirmar         | `Alt+O`   |
| Cancelar          | `Alt+C`   |

> **Dica:**  
> Todas as janelas do Gestor de Contactos podem ser fechadas com `Esc` ou `Alt+F4`.

## Agradecimentos

Este extra foi inspirado na agenda criada por:

- Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)  
- Rui Fontes (<rui.fontes@tiflotecnia.com>)  
- Ângelo Abrantes (<ampa4374@gmail.com>)
