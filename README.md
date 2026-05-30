Urna Digital em Python
Uma simulação em console/terminal desenvolvido em Python, focado em simular um processo de votação eleitoral com rígidos padrões de segurança, autenticação de dois fatores (MFA) e persistência de dados em arquivos locais 

O projeto foi construido para praticar conceitos de lógica de programação, estruturas de dados dinâmicas (dicionários e listas) e manipulação de arquivos com a bibloteca nativa 'json'. 

Funcionalidades:
**Menu do Colaborador:**
- Cadastro de Senha Dinâmica: Primeiro acesso seguro obrigando a criação de uma senha de 4 dígitos com letras e números (*case-sensitive*)
- Dupla Autenticação (MFA): Geração de tokens númericos aleatórios temporários a cada tentativa de login
- Sistema de Recuperação: Fluxo para redefinição de credenciais caso o colaborador esqueça a senha ("ESQUECI"), validando por um super token de segurança. 
**Menu do Votante:** Interface para votação em candidatos disponíveis, voto em branco ou voto nulo.
**Apuração Inteligente:** Exibição de estatísticas, percentuais de votos e definição do vencedor (considerando apenas votos válidos e tratando empates).

Conceitos Aplicados
* Estrutura de repetição ('while True') e condicionais ('if/elif/else').
* Manipulação de dicionários ('{}') e Listas ('[]').Urna Digital em Python
Uma simulação em console/terminal de um sistema de votação eletrônica desenvolvido para praticar conceitos de lógica de programação em Python.

Funcionalidades:
**Menu do Colaborador:** Permite o cadastro e exclusão de candidatos (armazenados em dicionários) e visualização da apuração detalhada
**Menu do Votante:** Interface para votação em candidatos disponíveis, voto em branco ou voto nulo.
**Apuração Inteligente:** Exibição de estatísticas, percentuais de votos e definição do vencedor (considerando apenas votos válidos e tratando empates).

Conceitos Aplicados
* Estrutura de repetição ('while True') e condicionais ('if/elif/else').
* Manipulação de dicionários ('{}') e Listas ('[]').
