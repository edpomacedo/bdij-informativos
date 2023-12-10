# bdij-informativos

Automação de rotina de publicação de informativos na Base de Dados de Institutos Jurídicos.

## Estrutura

- `/payload`: Diretório dividido em subdiretórios, sendo cada subdiretório um informativo e cada arquivo `.txt` as informações do inteiro teor a serem publicadas.

## Pré-requisitos

Utiliza credenciais [OAuth](https://web.bdij.com.br/wiki/Special:OAuthListConsumers) da Base de Dados de Institutos Jurídicos e as bibliotecas `requests` e `requests_oauthlib`.

```bash
pip install -r requirements.txt
```

## Instalação

```bash
git clone https://github.com/edpomacedo/bdij-informativos.git
cd bdij-informativos
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

1. Selecione um informativo de algum Tribunal ou órgão.
2. Crie um subdiretório dentro de `./payload/`.
3. Crie um `arquivo.txt` segundo as diretrizes abaixo.
4. A primeira linha do `arquivo.txt` será o título da página, equivalente a um instituto jurídico, seja ele um termo simples ou composto.
5. A segunda linha do `arquivo.txt` será o tema do informativo, referente ao instituto jurídico em comento.
6. Da terceira linha em diante no `arquivo.txt` será o texto extraído das informações do inteiro teor.
7. Execute o comando `python main.py`.
8. Informe o nome do subdiretório criado e pressione `enter`.

A versão atual não faz distinção se a seção existe ou não. Evite conteúdo duplicado.

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -am 'Adicione uma nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Licença

Copyright 2023 EDPO AUGUSTO FERREIRA MACEDO

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contato

[Base de Dados de Institutos Jurídicos](https://github.com/bdij)