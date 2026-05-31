Urna Digital em Python
Uma simulação em console/terminal desenvolvido em Python, focado em simular um processo de votação eleitoral com rígidos padrões de segurança, autenticação de dois fatores (MFA) e persistência de dados em arquivos locais 

O projeto foi construido para praticar conceitos de lógica de programação, estruturas de dados dinâmicas (dicionários e listas) e manipulação de arquivos com a bibloteca nativa 'json'. 

Funcionalidades:
**Menu do Colaborador:**
- Cadastro de Senha Dinâmica: Primeiro acesso seguro obrigando a criação de uma senha de 4 dígitos com letras e números (*case-sensitive*)
- Dupla Autenticação (MFA): Geração de tokens númericos aleatórios temporários a cada tentativa de login
- Sistema de Recuperação: Fluxo para redefinição de credenciais caso o colaborador esqueça a senha ("ESQUECI"), validando por um super token de segurança.
- Gerenciamento de Candidatos: Cadastro completo e exclusão de candidatos (protegida com token de confirmação para evitar fraudes)
- Apuração em tempo real: Exibição total de votos, percentuais de votos brancos, nulos e válidos, listagem individual e declaração automática de vencedor ou empate.

**Menu do Votante:** 
- Listagem Dinâmica: Vizualização de todos os candidatos cadastrados no sistema com seus respectivos números e cargos.
- Votação intuitiva: Suporte para votos válidos em candidatos, votos em Branco (0) e votos Nulos (-1).
- Confirmação Eleitoral: Sistema de dupla confirmação antes de computar o voto para evitar erros do eleitor.

---
**Persistência de Dados (bibloteca JSON)**
Para garantir que nenhuma informação seja perdida caso o programa seja fechado ou ocorra uma queda de energia, o sistema utiliza a bibloteca nativa 'json' do Python.

Os dados são salvos no arquivo físico 'votos.json' em 5 momentos críticos: 
1. Ao cadastrar novo candidato.
2. Ao excluir um candidato existente.
3. Ao computar um voto para um candidato
4. Ao comutar um voto em branco
5. Ao computar um voto nul
6. A senha do colaborador

Quando o sistema é reiniciado, ele verifica a existência do arquivo utilizando a bibloteca 'os' e reconstroi o estado anterior da urna automaticamente.

---

**Tecnologias Utilizadas**
- Linguagem: Python 3
- Biblotecas Nativas:
  * 'json': Para serialização e persistência dos dados.
  * 'random': Para geração de Tokens de segurança (MFA e Exclusão).
  * 'os': Para verificação e manipulação de caminhos de arquivos.

---

**Futuras implementações**
O projeto está em constante evolução. Os próximos passos planejados para o desenvolvimento são: 

- [] Múltiplos Colaboradores: Evoluir o sistema de autenticação simples para um gerenciamento de usuários por dicionário, permitindo múltiplos logins de mesários.
- [] Interface Web (Front-end): Separar a lógica de negócios (Back-end) para conectar a urna a uma interface gráfica de site, tornando a experiência do votante mais visual e parecida com a urna real.
- [] Criptografia de Senhas: Implementar hash de segurança para que as senhas dos colaboradores não fiquem salvas em texto limpo dentro do arquivo JSON.
