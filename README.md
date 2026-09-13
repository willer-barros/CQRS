#CQRS Mnorepo

Repositório contendo múltiplas aplicações que implementam o padrão **CQRS**

## O que é o CQRS

É um padrão de arquitetura que **separa** as operações de escrita e leitura, melhorando a performance da aplicação.

### Benefícios
- **Escala independente** - você pode escalar reads e writes separadamente.
- **Modelos otimizados** - o modelo de leitura é desenhado para a consulta, não para escrita
- **Auditoria natural** - com Event Sourcing, todo o histórico de mudanças é preservado
- **Separação de responsabilidades** - cada lado do sistema tem uma única responsabilidade


## Lista de Projetos usando essa arquitetura
- api-users 
