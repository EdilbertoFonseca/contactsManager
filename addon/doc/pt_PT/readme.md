# Gestor de Contactos para NVDA

- **Autor**: Edilberto Fonseca (<edilberto.fonseca@outlook.com>)
- **Data de Criação**: 11/04/2024
- **Licença**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Introdução

Bem-vindo ao **Gestor de Contactos para NVDA**!  
Este extra foi desenvolvido especialmente para pessoas com deficiência visual, permitindo organizar e aceder a informações de contacto com praticidade, acessibilidade e autonomia.

Com ele, pode:

- Adicionar, editar e eliminar contactos;
- Abrir os seus contactos no WhatsApp;
- Pesquisar nomes e dados rapidamente;
- Importar e exportar listas em formato CSV;
- Personalizar a formatação de números de telefone;
- Armazenar os dados num diretório personalizado;
- Utilizar uma interface simples e acessível via teclado.

## Instalação

1. No NVDA, abra o menu **Ferramentas** e aceda à **Loja de Extras**.
2. No separador **Extras Disponíveis**, digite "Gestor de Contactos" no campo de busca.
3. Selecione o extra e pressione **Enter** ou clique em **Aplicar**, depois escolha **Instalar**.
4. Reinicie o NVDA para concluir a instalação.

## Configurações

Aceda a:  
**NVDA > Preferências > Definições... > Gestor de Contactos para NVDA**

As seguintes opções estão disponíveis:

1. **Código do país** permite selecionar o código internacional a ser usado na formatação do número do WhatsApp. Por predefinição, o código selecionado é o (+55) do Brasil.

2. **Máscara para campos de telefone** Aplica uma máscara usando `#` para formatar números. A máscara padrão é baseada no formato brasileiro.

3. **Eliminação completa da agenda** (`Alt+T`)  
   Permite remover todos os contactos de uma só vez.

4. **Importação de contactos via CSV** (`Alt+I`)  
   Permite importar contactos de ficheiros CSV compatíveis.

5. **Exportação da agenda para CSV** (`Alt+X`)  
   Exporta todos os contactos para um ficheiro CSV.

6. **Caminho da base de dados** Define um diretório personalizado para guardar os dados da agenda.

## Acesso

Pode abrir o Gestor de Contactos das seguintes formas:

1. Atalho: `Windows+Alt+L`
2. Menu NVDA: `NVDA+N > Ferramentas > Gestor de Contactos`

A janela principal permite:

- Registar, editar, remover e procurar contactos;
- Importar/exportar contactos;
- Apagar toda a agenda (opcional nas configurações).
- Pressionando Enter na lista de contactos, o contacto é aberto no WhatsApp. Caso o campo do telemóvel esteja vazio, esta condição será verbalizada pelo NVDA.

## Registar um Novo Contacto

1. Abra o Gestor (`Windows+Alt+L` ou pelo menu NVDA);
2. Pressione `Alt+N` para adicionar;
3. Preencha os campos e pressione `Alt+O` para guardar ou `Alt+C` para cancelar.

> Observação:  
> Use a tecla `Enter` para navegar entre os campos. O uso do `Tab` pode gerar comportamentos imprevisíveis. Agora também é possível colar números diretamente da área de transferência.

## Editar um Contacto

1. Selecione um contacto na lista;
2. Pressione `Alt+E` ou `F2`;
3. Edite os dados e pressione `Alt+O` para guardar ou `Alt+C` para cancelar.

## Pesquisar Contactos

Na janela principal:

1. Digite o termo de busca (nome, telemóvel, fixo ou e-mail);
2. Selecione o campo correspondente;
3. Pressione `Alt+P` para pesquisar ou a tecla `enter`;
4. Pressione `Alt+A` ou `F5` para atualizar a lista.

Caso nenhum resultado seja encontrado, uma mensagem será exibida.

## Atalhos Disponíveis

### Janela Principal

| Ação                                   | Atalho                       |
| -------------------------------------- | ---------------------------- |
| Novo contacto                          | `Alt+N`                      |
| Editar                                 | `Alt+E` ou `F2`              |
| Remover contacto                       | `Alt+R` ou `Delete`          |
| Pesquisar                              | `Alt+P` ou `enter`           |
| Abre o contacto selecionado no WhatsApp| `Enter na lista de contactos`|
| Atualizar lista                        | `Alt+A` ou `F5`              |
| Importar CSV                           | `Alt+I`                      |
| Exportar CSV                           | `Alt+X`                      |
| Eliminar todos os contactos            | `Alt+T`                      |
| Sair                                   | `Alt+S`                      |

> Para editar ou remover, é necessário selecionar um contacto primeiro.

### Janela de Registo/Edição

| Ação      | Atalho  |
| --------- | ------- |
| Confirmar | `Alt+O` |
| Cancelar  | `Alt+C` |

> Dica: Use `Esc` ou `Alt+F4` para fechar qualquer janela.

## Agradecimentos

Este extra foi inspirado na agenda criada por:

- Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)
- Rui Fontes (<rui.fontes@tiflotecnia.com>)
- Ângelo Abrantes (<ampa4374@gmail.com>)

## Traduções

- **Português (Brasil)** – Edilberto Fonseca
- **Português (Portugal)** – Edilberto Fonseca
- **Ucraniano** – George‑br
- **Turco** – Umut KORKMAZ
