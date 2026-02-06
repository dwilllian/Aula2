# Aula2# Prova Técnica Arquitetomulticloud (Pleno)

**Quantidade de questões:** 50

**Tempo estimado:** 60–90 minutos

**Peso das questões:** iguais

**Instruções:** Marque todas as alternativas corretas.

### Questão 01

**Categoria:** Troubleshooting & Incident Response

**Provedor:** AWS

Durante operação de observabilidade cross-cloud, o time observou falhas na autenticação no provedor AWS. Os alerts indicam impacto direto nos usuários finais.

Restrições: ambiente com compliance PCI.

Objetivo: manter SLAs de resposta.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q01.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** revisar métricas de saturação e ajustar limites (SLO 99.9%, VAR 694, Q01)
- **B.** eliminar logs para economizar storage (SLO 97.0%, VAR 531, Q01)
- **C.** expor o banco diretamente à internet (SLO 97.0%, VAR 934, Q01)
- **D.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 503, Q01)

**Respostas corretas:** A

**Racional:** A opção correta prioriza manter SLAs de resposta sem violar ambiente com compliance PCI. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 02

**Categoria:** Arquitetura & Estratégia

**Provedor:** GCP

Você está trabalhando em segurança zero trust para um sistema crítico no provedor GCP. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: conformidade com ISO 27001 e LGPD.

Objetivo: evitar regressões de performance.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** eliminar logs para economizar storage (SLO 97.0%, VAR 912, Q02)
- **B.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 264, Q02)
- **C.** adotar GKE com auto scaling baseado em métricas (SLO 99.9%, VAR 369, Q02)
- **D.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 314, Q02)

**Respostas corretas:** C

**Racional:** A opção correta prioriza evitar regressões de performance sem violar conformidade com ISO 27001 e LGPD. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 03

**Categoria:** Arquitetura & Estratégia

**Provedor:** AWS

Você está trabalhando em governança e tagging para um sistema crítico no provedor AWS. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: RTO máximo de 60 minutos.

Objetivo: garantir segurança de dados sensíveis.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** incluir WAF com TTL e invalidation (SLO 99.95%, VAR 872, Q03)
- **B.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 116, Q03)
- **C.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 214, Q03)
- **D.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 294, Q03)

**Respostas corretas:** A

**Racional:** A opção correta prioriza garantir segurança de dados sensíveis sem violar RTO máximo de 60 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 04

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Azure

Durante operação de observabilidade cross-cloud, o time observou expiração inesperada de tokens no provedor Azure. Os alerts indicam impacto direto nos usuários finais.

Restrições: orçamento com teto mensal.

Objetivo: garantir rastreabilidade de mudanças.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q04.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 126, Q04)
- **B.** verificar latência entre zonas e ajustar routing (SLO 99.9%, VAR 258, Q04)
- **C.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 606, Q04)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 329, Q04)

**Respostas corretas:** B

**Racional:** A opção correta prioriza garantir rastreabilidade de mudanças sem violar orçamento com teto mensal. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 05

**Categoria:** Arquitetura & Estratégia

**Provedor:** OCI

Você está trabalhando em governança e tagging para um sistema crítico no provedor OCI. O cenário atual envolve equipes distribuídas, e há necessidade de padronização técnica.

Restrições: ambiente com compliance PCI.

Objetivo: garantir segurança de dados sensíveis.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 809, Q05)
- **B.** adotar Autonomous DB com auto scaling baseado em métricas (SLO 99.5%, VAR 653, Q05)
- **C.** eliminar logs para economizar storage (SLO 97.0%, VAR 237, Q05)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 429, Q05)

**Respostas corretas:** B

**Racional:** A opção correta prioriza garantir segurança de dados sensíveis sem violar ambiente com compliance PCI. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 06

**Categoria:** Arquitetura & Estratégia

**Provedor:** GCP

Você está trabalhando em roteamento global e DNS para um sistema crítico no provedor GCP. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: ambiente com compliance PCI.

Objetivo: garantir segurança de dados sensíveis.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q06.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 798, Q06)
- **B.** incluir KMS com TTL e invalidation (SLO 99.95%, VAR 823, Q06)
- **C.** eliminar logs para economizar storage (SLO 97.0%, VAR 462, Q06)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 166, Q06)

**Respostas corretas:** B

**Racional:** A opção correta prioriza garantir segurança de dados sensíveis sem violar ambiente com compliance PCI. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 07

**Categoria:** Troubleshooting & Incident Response

**Provedor:** GCP

Durante operação de padronização de landing zones, o time observou falha na replicação de banco no provedor GCP. Os alerts indicam impacto direto nos usuários finais.

Restrições: RTO máximo de 60 minutos.

Objetivo: manter SLAs de resposta.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q07.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** inspecionar erros de autenticação no IdP (SLO 99.5%, VAR 165, Q07)
- **B.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 265, Q07)
- **C.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 850, Q07)
- **D.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 299, Q07)

**Respostas corretas:** A

**Racional:** A opção correta prioriza manter SLAs de resposta sem violar RTO máximo de 60 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 08

**Categoria:** Troubleshooting & Incident Response

**Provedor:** OCI

Durante operação de roteamento global e DNS, o time observou alta taxa de cache miss no provedor OCI. Os alerts indicam impacto direto nos usuários finais.

Restrições: RPO máximo de 10 minutos.

Objetivo: diminuir tempo de build.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q08.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 762, Q08)
- **B.** expor o banco diretamente à internet (SLO 97.0%, VAR 748, Q08)
- **C.** revisar métricas de saturação e ajustar limites (SLO 99.95%, VAR 332, Q08)
- **D.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 183, Q08)

**Respostas corretas:** C

**Racional:** A opção correta prioriza diminuir tempo de build sem violar RPO máximo de 10 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 09

**Categoria:** Arquitetura & Estratégia

**Provedor:** Agnóstico

Você está trabalhando em topologia hub-spoke multi-cloud para um sistema crítico no provedor Agnóstico. O cenário atual envolve dependências legadas, e há necessidade de padronização técnica.

Restrições: sem janela de manutenção.

Objetivo: padronizar governança.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q09.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** adotar Ingress com auto scaling baseado em métricas (SLO 99.9%, VAR 323, Q09)
- **B.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 799, Q09)
- **C.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 258, Q09)
- **D.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 714, Q09)

**Respostas corretas:** A

**Racional:** A opção correta prioriza padronizar governança sem violar sem janela de manutenção. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 10

**Categoria:** Troubleshooting & Incident Response

**Provedor:** AWS

Durante operação de federacao de identidades, o time observou erros 5xx intermitentes no provedor AWS. Os alerts indicam impacto direto nos usuários finais.

Restrições: RPO máximo de 60 minutos.

Objetivo: reduzir custo de infraestrutura.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** mitigar com feature flag e rollback controlado (SLO 99.5%, VAR 784, Q10)
- **B.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 352, Q10)
- **C.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 474, Q10)
- **D.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 244, Q10)

**Respostas corretas:** A

**Racional:** A opção correta prioriza reduzir custo de infraestrutura sem violar RPO máximo de 60 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 11

**Categoria:** Arquitetura & Estratégia

**Provedor:** Agnóstico

Você está trabalhando em segurança zero trust para um sistema crítico no provedor Agnóstico. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: requisitos de latência abaixo de 200 ms.

Objetivo: diminuir tempo de build.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 724, Q11)
- **B.** implementar Queue com regras de cache e WAF (SLO 99.95%, VAR 429, Q11)
- **C.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 498, Q11)
- **D.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 413, Q11)

**Respostas corretas:** B

**Racional:** A opção correta prioriza diminuir tempo de build sem violar requisitos de latência abaixo de 200 ms. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 12

**Categoria:** Troubleshooting & Incident Response

**Provedor:** AWS

Durante operação de governança e tagging, o time observou expiração inesperada de tokens no provedor AWS. Os alerts indicam impacto direto nos usuários finais.

Restrições: orçamento com teto mensal.

Objetivo: manter SLAs de resposta.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** expor o banco diretamente à internet (SLO 97.0%, VAR 308, Q12)
- **B.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 607, Q12)
- **C.** validar políticas de autoscaling e backoff (SLO 99.9%, VAR 174, Q12)
- **D.** eliminar logs para economizar storage (SLO 97.0%, VAR 311, Q12)

**Respostas corretas:** C

**Racional:** A opção correta prioriza manter SLAs de resposta sem violar orçamento com teto mensal. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 13

**Categoria:** Troubleshooting & Incident Response

**Provedor:** GCP

Durante operação de topologia hub-spoke multi-cloud, o time observou picos de latência no tráfego de API no provedor GCP. Os alerts indicam impacto direto nos usuários finais.

Restrições: ambiente com compliance PCI.

Objetivo: diminuir tempo de build.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 384, Q13)
- **B.** revisar métricas de saturação e ajustar limites (SLO 99.95%, VAR 943, Q13)
- **C.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 962, Q13)
- **D.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 294, Q13)

**Respostas corretas:** B

**Racional:** A opção correta prioriza diminuir tempo de build sem violar ambiente com compliance PCI. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 14

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Azure

Durante operação de estratégia active-active global, o time observou degeneração de throughput no provedor Azure. Os alerts indicam impacto direto nos usuários finais.

Restrições: RTO máximo de 60 minutos.

Objetivo: diminuir tempo de build.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q14.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 966, Q14)
- **B.** mitigar com feature flag e rollback controlado (SLO 99.5%, VAR 306, Q14)
- **C.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 609, Q14)
- **D.** eliminar logs para economizar storage (SLO 97.0%, VAR 305, Q14)

**Respostas corretas:** B

**Racional:** A opção correta prioriza diminuir tempo de build sem violar RTO máximo de 60 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 15

**Categoria:** Troubleshooting & Incident Response

**Provedor:** OCI

Durante operação de roteamento global e DNS, o time observou fila crescendo sem consumo no provedor OCI. Os alerts indicam impacto direto nos usuários finais.

Restrições: ciclos de release semanais.

Objetivo: aumentar disponibilidade global.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 157, Q15)
- **B.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 500, Q15)
- **C.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 489, Q15)
- **D.** verificar latência entre zonas e ajustar routing (SLO 99.9%, VAR 759, Q15)

**Respostas corretas:** D

**Racional:** A opção correta prioriza aumentar disponibilidade global sem violar ciclos de release semanais. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 16

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Azure

Durante operação de observabilidade cross-cloud, o time observou picos de latência no tráfego de API no provedor Azure. Os alerts indicam impacto direto nos usuários finais.

Restrições: sem janela de manutenção.

Objetivo: garantir rastreabilidade de mudanças.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q16.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 106, Q16)
- **B.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 490, Q16)
- **C.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 103, Q16)
- **D.** validar políticas de autoscaling e backoff (SLO 99.5%, VAR 339, Q16)

**Respostas corretas:** D

**Racional:** A opção correta prioriza garantir rastreabilidade de mudanças sem violar sem janela de manutenção. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 17

**Categoria:** Arquitetura & Estratégia

**Provedor:** OCI

Você está trabalhando em roteamento global e DNS para um sistema crítico no provedor OCI. O cenário atual envolve dependências legadas, e há necessidade de padronização técnica.

Restrições: times distribuídos com autonomia.

Objetivo: reduzir custo de infraestrutura.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q17.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 264, Q17)
- **B.** adotar CDN com auto scaling baseado em métricas (SLO 99.5%, VAR 278, Q17)
- **C.** eliminar logs para economizar storage (SLO 97.0%, VAR 476, Q17)
- **D.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 857, Q17)

**Respostas corretas:** B

**Racional:** A opção correta prioriza reduzir custo de infraestrutura sem violar times distribuídos com autonomia. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 18

**Categoria:** Troubleshooting & Incident Response

**Provedor:** OCI

Durante operação de roteamento global e DNS, o time observou expiração inesperada de tokens no provedor OCI. Os alerts indicam impacto direto nos usuários finais.

Restrições: times distribuídos com autonomia.

Objetivo: evitar regressões de performance.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q18.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 775, Q18)
- **B.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 902, Q18)
- **C.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 733, Q18)
- **D.** corrigir health checks e probes (SLO 99.5%, VAR 846, Q18)

**Respostas corretas:** D

**Racional:** A opção correta prioriza evitar regressões de performance sem violar times distribuídos com autonomia. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 19

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Agnóstico

Durante operação de topologia hub-spoke multi-cloud, o time observou falha na replicação de banco no provedor Agnóstico. Os alerts indicam impacto direto nos usuários finais.

Restrições: ciclos de release semanais.

Objetivo: minimizar risco de rollback.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q19.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 796, Q19)
- **B.** verificar latência entre zonas e ajustar routing (SLO 99.5%, VAR 276, Q19)
- **C.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 676, Q19)
- **D.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 887, Q19)

**Respostas corretas:** B

**Racional:** A opção correta prioriza minimizar risco de rollback sem violar ciclos de release semanais. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 20

**Categoria:** Arquitetura & Estratégia

**Provedor:** AWS

Você está trabalhando em estratégia active-active global para um sistema crítico no provedor AWS. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: tráfego com picos imprevisíveis.

Objetivo: garantir rastreabilidade de mudanças.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** adotar EKS com auto scaling baseado em métricas (SLO 99.9%, VAR 738, Q20)
- **B.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 557, Q20)
- **C.** expor o banco diretamente à internet (SLO 97.0%, VAR 586, Q20)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 446, Q20)

**Respostas corretas:** A

**Racional:** A opção correta prioriza garantir rastreabilidade de mudanças sem violar tráfego com picos imprevisíveis. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 21

**Categoria:** Arquitetura & Estratégia

**Provedor:** GCP

Você está trabalhando em estratégia active-active global para um sistema crítico no provedor GCP. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: sem janela de manutenção.

Objetivo: minimizar risco de rollback.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 120, Q21)
- **B.** expor o banco diretamente à internet (SLO 97.0%, VAR 603, Q21)
- **C.** usar GCS com health checks avançados (SLO 99.5%, VAR 286, Q21)
- **D.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 787, Q21)

**Respostas corretas:** C

**Racional:** A opção correta prioriza minimizar risco de rollback sem violar sem janela de manutenção. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 22

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Azure

Durante operação de segurança zero trust, o time observou falhas na autenticação no provedor Azure. Os alerts indicam impacto direto nos usuários finais.

Restrições: sem janela de manutenção.

Objetivo: padronizar governança.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q22.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** corrigir health checks e probes (SLO 99.9%, VAR 270, Q22)
- **B.** expor o banco diretamente à internet (SLO 97.0%, VAR 817, Q22)
- **C.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 413, Q22)
- **D.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 369, Q22)

**Respostas corretas:** A

**Racional:** A opção correta prioriza padronizar governança sem violar sem janela de manutenção. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 23

**Categoria:** Troubleshooting & Incident Response

**Provedor:** GCP

Durante operação de service mesh entre clouds, o time observou falhas na autenticação no provedor GCP. Os alerts indicam impacto direto nos usuários finais.

Restrições: sem janela de manutenção.

Objetivo: diminuir tempo de build.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q23.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 600, Q23)
- **B.** validar políticas de autoscaling e backoff (SLO 99.95%, VAR 367, Q23)
- **C.** eliminar logs para economizar storage (SLO 97.0%, VAR 388, Q23)
- **D.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 373, Q23)

**Respostas corretas:** B

**Racional:** A opção correta prioriza diminuir tempo de build sem violar sem janela de manutenção. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 24

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Azure

Durante operação de estratégia active-active global, o time observou falhas na autenticação no provedor Azure. Os alerts indicam impacto direto nos usuários finais.

Restrições: RPO máximo de 10 minutos.

Objetivo: garantir rastreabilidade de mudanças.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** eliminar logs para economizar storage (SLO 97.0%, VAR 224, Q24)
- **B.** eliminar logs para economizar storage (SLO 97.0%, VAR 157, Q24)
- **C.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 821, Q24)
- **D.** validar políticas de autoscaling e backoff (SLO 99.5%, VAR 727, Q24)

**Respostas corretas:** D

**Racional:** A opção correta prioriza garantir rastreabilidade de mudanças sem violar RPO máximo de 10 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 25

**Categoria:** Troubleshooting & Incident Response

**Provedor:** AWS

Durante operação de padronização de landing zones, o time observou picos de latência no tráfego de API no provedor AWS. Os alerts indicam impacto direto nos usuários finais.

Restrições: requisitos de latência abaixo de 200 ms.

Objetivo: reduzir custo de infraestrutura.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 247, Q25)
- **B.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 655, Q25)
- **C.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 689, Q25)
- **D.** verificar latência entre zonas e ajustar routing (SLO 99.5%, VAR 369, Q25)

**Respostas corretas:** D

**Racional:** A opção correta prioriza reduzir custo de infraestrutura sem violar requisitos de latência abaixo de 200 ms. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 26

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Azure

Durante operação de segurança zero trust, o time observou degeneração de throughput no provedor Azure. Os alerts indicam impacto direto nos usuários finais.

Restrições: conformidade com ISO 27001 e LGPD.

Objetivo: diminuir tempo de build.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q26.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 556, Q26)
- **B.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 112, Q26)
- **C.** validar políticas de autoscaling e backoff (SLO 99.95%, VAR 882, Q26)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 862, Q26)

**Respostas corretas:** C

**Racional:** A opção correta prioriza diminuir tempo de build sem violar conformidade com ISO 27001 e LGPD. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 27

**Categoria:** Troubleshooting & Incident Response

**Provedor:** GCP

Durante operação de segurança zero trust, o time observou degeneração de throughput no provedor GCP. Os alerts indicam impacto direto nos usuários finais.

Restrições: requisitos de latência abaixo de 80 ms.

Objetivo: padronizar governança.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q27.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 256, Q27)
- **B.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 245, Q27)
- **C.** analisar dead-letter queue e reprocessamento (SLO 99.9%, VAR 575, Q27)
- **D.** expor o banco diretamente à internet (SLO 97.0%, VAR 855, Q27)

**Respostas corretas:** C

**Racional:** A opção correta prioriza padronizar governança sem violar requisitos de latência abaixo de 80 ms. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 28

**Categoria:** Arquitetura & Estratégia

**Provedor:** Azure

Você está trabalhando em service mesh entre clouds para um sistema crítico no provedor Azure. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: times distribuídos com autonomia.

Objetivo: minimizar risco de rollback.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q28.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** centralizar logs com tracing distribuído (SLO 99.9%, VAR 949, Q28)
- **B.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 333, Q28)
- **C.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 294, Q28)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 598, Q28)

**Respostas corretas:** A

**Racional:** A opção correta prioriza minimizar risco de rollback sem violar times distribuídos com autonomia. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 29

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Agnóstico

Durante operação de federacao de identidades, o time observou erros 5xx intermitentes no provedor Agnóstico. Os alerts indicam impacto direto nos usuários finais.

Restrições: requisitos de latência abaixo de 200 ms.

Objetivo: garantir segurança de dados sensíveis.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q29.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** eliminar logs para economizar storage (SLO 97.0%, VAR 449, Q29)
- **B.** mitigar com feature flag e rollback controlado (SLO 99.5%, VAR 232, Q29)
- **C.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 842, Q29)
- **D.** eliminar logs para economizar storage (SLO 97.0%, VAR 482, Q29)

**Respostas corretas:** B

**Racional:** A opção correta prioriza garantir segurança de dados sensíveis sem violar requisitos de latência abaixo de 200 ms. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 30

**Categoria:** Troubleshooting & Incident Response

**Provedor:** GCP

Durante operação de segurança zero trust, o time observou falha na replicação de banco no provedor GCP. Os alerts indicam impacto direto nos usuários finais.

Restrições: requisitos de latência abaixo de 120 ms.

Objetivo: minimizar risco de rollback.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 197, Q30)
- **B.** mitigar com feature flag e rollback controlado (SLO 99.9%, VAR 119, Q30)
- **C.** expor o banco diretamente à internet (SLO 97.0%, VAR 493, Q30)
- **D.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 868, Q30)

**Respostas corretas:** B

**Racional:** A opção correta prioriza minimizar risco de rollback sem violar requisitos de latência abaixo de 120 ms. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 31

**Categoria:** Troubleshooting & Incident Response

**Provedor:** AWS

Durante operação de service mesh entre clouds, o time observou aumento súbito de CPU no provedor AWS. Os alerts indicam impacto direto nos usuários finais.

Restrições: tráfego com picos imprevisíveis.

Objetivo: padronizar governança.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 292, Q31)
- **B.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 711, Q31)
- **C.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 719, Q31)
- **D.** auditar configurações de cache e headers (SLO 99.5%, VAR 761, Q31)

**Respostas corretas:** D

**Racional:** A opção correta prioriza padronizar governança sem violar tráfego com picos imprevisíveis. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 32

**Categoria:** Arquitetura & Estratégia

**Provedor:** GCP

Você está trabalhando em federacao de identidades para um sistema crítico no provedor GCP. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: orçamento com teto mensal.

Objetivo: garantir rastreabilidade de mudanças.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q32.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 302, Q32)
- **B.** expor o banco diretamente à internet (SLO 97.0%, VAR 823, Q32)
- **C.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 721, Q32)
- **D.** implementar Cloud Armor com regras de cache e WAF (SLO 99.9%, VAR 382, Q32)

**Respostas corretas:** D

**Racional:** A opção correta prioriza garantir rastreabilidade de mudanças sem violar orçamento com teto mensal. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 33

**Categoria:** Arquitetura & Estratégia

**Provedor:** OCI

Você está trabalhando em governança e tagging para um sistema crítico no provedor OCI. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: tráfego com picos imprevisíveis.

Objetivo: padronizar governança.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q33.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** introduzir Queue com read replicas (SLO 99.5%, VAR 165, Q33)
- **B.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 204, Q33)
- **C.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 635, Q33)
- **D.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 267, Q33)

**Respostas corretas:** A

**Racional:** A opção correta prioriza padronizar governança sem violar tráfego com picos imprevisíveis. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 34

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Agnóstico

Durante operação de governança e tagging, o time observou expiração inesperada de tokens no provedor Agnóstico. Os alerts indicam impacto direto nos usuários finais.

Restrições: requisitos de latência abaixo de 50 ms.

Objetivo: reduzir custo de infraestrutura.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** analisar dead-letter queue e reprocessamento (SLO 99.9%, VAR 590, Q34)
- **B.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 338, Q34)
- **C.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 256, Q34)
- **D.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 991, Q34)

**Respostas corretas:** A

**Racional:** A opção correta prioriza reduzir custo de infraestrutura sem violar requisitos de latência abaixo de 50 ms. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 35

**Categoria:** Arquitetura & Estratégia

**Provedor:** Azure

Você está trabalhando em service mesh entre clouds para um sistema crítico no provedor Azure. O cenário atual envolve equipes distribuídas, e há necessidade de padronização técnica.

Restrições: sem janela de manutenção.

Objetivo: evitar regressões de performance.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q35.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 737, Q35)
- **B.** habilitar Blob para criptografia e rotação (SLO 99.5%, VAR 107, Q35)
- **C.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 388, Q35)
- **D.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 372, Q35)

**Respostas corretas:** B

**Racional:** A opção correta prioriza evitar regressões de performance sem violar sem janela de manutenção. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 36

**Categoria:** Troubleshooting & Incident Response

**Provedor:** AWS

Durante operação de roteamento global e DNS, o time observou expiração inesperada de tokens no provedor AWS. Os alerts indicam impacto direto nos usuários finais.

Restrições: requisitos de latência abaixo de 200 ms.

Objetivo: minimizar risco de rollback.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 574, Q36)
- **B.** auditar configurações de cache e headers (SLO 99.5%, VAR 937, Q36)
- **C.** eliminar logs para economizar storage (SLO 97.0%, VAR 155, Q36)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 763, Q36)

**Respostas corretas:** B

**Racional:** A opção correta prioriza minimizar risco de rollback sem violar requisitos de latência abaixo de 200 ms. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 37

**Categoria:** Troubleshooting & Incident Response

**Provedor:** OCI

Durante operação de roteamento global e DNS, o time observou falha na replicação de banco no provedor OCI. Os alerts indicam impacto direto nos usuários finais.

Restrições: times distribuídos com autonomia.

Objetivo: reduzir custo de infraestrutura.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q37.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 100, Q37)
- **B.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 410, Q37)
- **C.** verificar latência entre zonas e ajustar routing (SLO 99.95%, VAR 111, Q37)
- **D.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 555, Q37)

**Respostas corretas:** C

**Racional:** A opção correta prioriza reduzir custo de infraestrutura sem violar times distribuídos com autonomia. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 38

**Categoria:** Troubleshooting & Incident Response

**Provedor:** AWS

Durante operação de topologia hub-spoke multi-cloud, o time observou erros 5xx intermitentes no provedor AWS. Os alerts indicam impacto direto nos usuários finais.

Restrições: conformidade com ISO 27001 e LGPD.

Objetivo: reduzir custo de infraestrutura.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q38.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 693, Q38)
- **B.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 811, Q38)
- **C.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 670, Q38)
- **D.** validar políticas de autoscaling e backoff (SLO 99.9%, VAR 990, Q38)

**Respostas corretas:** D

**Racional:** A opção correta prioriza reduzir custo de infraestrutura sem violar conformidade com ISO 27001 e LGPD. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 39

**Categoria:** Troubleshooting & Incident Response

**Provedor:** OCI

Durante operação de governança e tagging, o time observou expiração inesperada de tokens no provedor OCI. Os alerts indicam impacto direto nos usuários finais.

Restrições: RPO máximo de 10 minutos.

Objetivo: diminuir tempo de build.

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 765, Q39)
- **B.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 145, Q39)
- **C.** revisar métricas de saturação e ajustar limites (SLO 99.9%, VAR 929, Q39)
- **D.** expor o banco diretamente à internet (SLO 97.0%, VAR 994, Q39)

**Respostas corretas:** C

**Racional:** A opção correta prioriza diminuir tempo de build sem violar RPO máximo de 10 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 40

**Categoria:** Troubleshooting & Incident Response

**Provedor:** GCP

Durante operação de observabilidade cross-cloud, o time observou loop de deploy com rollback no provedor GCP. Os alerts indicam impacto direto nos usuários finais.

Restrições: tráfego com picos imprevisíveis.

Objetivo: garantir segurança de dados sensíveis.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q40.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** expor o banco diretamente à internet (SLO 97.0%, VAR 542, Q40)
- **B.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 188, Q40)
- **C.** mitigar com feature flag e rollback controlado (SLO 99.9%, VAR 517, Q40)
- **D.** expor o banco diretamente à internet (SLO 97.0%, VAR 716, Q40)

**Respostas corretas:** C

**Racional:** A opção correta prioriza garantir segurança de dados sensíveis sem violar tráfego com picos imprevisíveis. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 41

**Categoria:** Arquitetura & Estratégia

**Provedor:** Agnóstico

Você está trabalhando em service mesh entre clouds para um sistema crítico no provedor Agnóstico. O cenário atual envolve dependências legadas, e há necessidade de padronização técnica.

Restrições: RPO máximo de 30 minutos.

Objetivo: manter SLAs de resposta.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q41.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 442, Q41)
- **B.** eliminar logs para economizar storage (SLO 97.0%, VAR 600, Q41)
- **C.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 219, Q41)
- **D.** associar CDN para desacoplamento (SLO 99.95%, VAR 906, Q41)

**Respostas corretas:** D

**Racional:** A opção correta prioriza manter SLAs de resposta sem violar RPO máximo de 30 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 42

**Categoria:** Arquitetura & Estratégia

**Provedor:** Azure

Você está trabalhando em topologia hub-spoke multi-cloud para um sistema crítico no provedor Azure. O cenário atual envolve equipes distribuídas, e há necessidade de padronização técnica.

Restrições: RTO máximo de 10 minutos.

Objetivo: garantir rastreabilidade de mudanças.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q42.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 312, Q42)
- **B.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 290, Q42)
- **C.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 947, Q42)
- **D.** associar AKS para desacoplamento (SLO 99.95%, VAR 223, Q42)

**Respostas corretas:** D

**Racional:** A opção correta prioriza garantir rastreabilidade de mudanças sem violar RTO máximo de 10 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 43

**Categoria:** Troubleshooting & Incident Response

**Provedor:** OCI

Durante operação de service mesh entre clouds, o time observou alta taxa de cache miss no provedor OCI. Os alerts indicam impacto direto nos usuários finais.

Restrições: ambiente com compliance PCI.

Objetivo: padronizar governança.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q43.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 492, Q43)
- **B.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 870, Q43)
- **C.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 651, Q43)
- **D.** corrigir health checks e probes (SLO 99.5%, VAR 916, Q43)

**Respostas corretas:** D

**Racional:** A opção correta prioriza padronizar governança sem violar ambiente com compliance PCI. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 44

**Categoria:** Arquitetura & Estratégia

**Provedor:** Agnóstico

Você está trabalhando em estratégia active-active global para um sistema crítico no provedor Agnóstico. O cenário atual envolve equipes distribuídas, e há necessidade de padronização técnica.

Restrições: orçamento com teto mensal.

Objetivo: evitar regressões de performance.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 800, Q44)
- **B.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 231, Q44)
- **C.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 707, Q44)
- **D.** incluir WAF com TTL e invalidation (SLO 99.95%, VAR 110, Q44)

**Respostas corretas:** D

**Racional:** A opção correta prioriza evitar regressões de performance sem violar orçamento com teto mensal. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 45

**Categoria:** Troubleshooting & Incident Response

**Provedor:** Agnóstico

Durante operação de federacao de identidades, o time observou expiração inesperada de tokens no provedor Agnóstico. Os alerts indicam impacto direto nos usuários finais.

Restrições: sem janela de manutenção.

Objetivo: diminuir tempo de build.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q45.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 926, Q45)
- **B.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 769, Q45)
- **C.** expor o banco diretamente à internet (SLO 97.0%, VAR 280, Q45)
- **D.** mitigar com feature flag e rollback controlado (SLO 99.5%, VAR 862, Q45)

**Respostas corretas:** D

**Racional:** A opção correta prioriza diminuir tempo de build sem violar sem janela de manutenção. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 46

**Categoria:** Arquitetura & Estratégia

**Provedor:** Azure

Você está trabalhando em gestão de chaves e HSM para um sistema crítico no provedor Azure. O cenário atual envolve crescimento acelerado, e há necessidade de padronização técnica.

Restrições: times distribuídos com autonomia.

Objetivo: evitar regressões de performance.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q46.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** usar Application Gateway com health checks avançados (SLO 99.9%, VAR 134, Q46)
- **B.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 818, Q46)
- **C.** expor o banco diretamente à internet (SLO 97.0%, VAR 532, Q46)
- **D.** consolidar todos os serviços em uma única VM (SLO 97.0%, VAR 168, Q46)

**Respostas corretas:** A

**Racional:** A opção correta prioriza evitar regressões de performance sem violar times distribuídos com autonomia. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 47

**Categoria:** Arquitetura & Estratégia

**Provedor:** Agnóstico

Você está trabalhando em service mesh entre clouds para um sistema crítico no provedor Agnóstico. O cenário atual envolve equipes distribuídas, e há necessidade de padronização técnica.

Restrições: ciclos de release semanais.

Objetivo: diminuir tempo de build.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q47.png)

Qual alternativa atende melhor aos requisitos descritos?

- **A.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 864, Q47)
- **B.** implementar KMS com regras de cache e WAF (SLO 99.5%, VAR 250, Q47)
- **C.** eliminar logs para economizar storage (SLO 97.0%, VAR 818, Q47)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 500, Q47)

**Respostas corretas:** B

**Racional:** A opção correta prioriza diminuir tempo de build sem violar ciclos de release semanais. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 48

**Categoria:** Arquitetura & Estratégia

**Provedor:** Azure

Você está trabalhando em roteamento global e DNS para um sistema crítico no provedor Azure. O cenário atual envolve dependências legadas, e há necessidade de padronização técnica.

Restrições: RPO máximo de 30 minutos.

Objetivo: minimizar risco de rollback.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** adotar WAF com auto scaling baseado em métricas (SLO 99.5%, VAR 248, Q48)
- **B.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 589, Q48)
- **C.** desativar controles de segurança para reduzir latência (SLO 97.0%, VAR 625, Q48)
- **D.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 174, Q48)

**Respostas corretas:** A

**Racional:** A opção correta prioriza minimizar risco de rollback sem violar RPO máximo de 30 minutos. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 49

**Categoria:** Arquitetura & Estratégia

**Provedor:** OCI

Você está trabalhando em service mesh entre clouds para um sistema crítico no provedor OCI. O cenário atual envolve dependências legadas, e há necessidade de padronização técnica.

Restrições: ambiente com compliance PCI.

Objetivo: aumentar disponibilidade global.

Qual alternativa atende melhor aos requisitos descritos?

- **A.** aumentar timeout sem investigar causa (SLO 97.0%, VAR 176, Q49)
- **B.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 543, Q49)
- **C.** adotar CDN com auto scaling baseado em métricas (SLO 99.95%, VAR 609, Q49)
- **D.** remover WAF para simplificar tráfego (SLO 97.0%, VAR 714, Q49)

**Respostas corretas:** C

**Racional:** A opção correta prioriza aumentar disponibilidade global sem violar ambiente com compliance PCI. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

### Questão 50

**Categoria:** Troubleshooting & Incident Response

**Provedor:** GCP

Durante operação de observabilidade cross-cloud, o time observou loop de deploy com rollback no provedor GCP. Os alerts indicam impacto direto nos usuários finais.

Restrições: times distribuídos com autonomia.

Objetivo: manter SLAs de resposta.

![diagram](assets/diagrams/arquitetoMulticloud_pleno/q50.png)

Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?

- **A.** desabilitar criptografia para ganho imediato (SLO 97.0%, VAR 746, Q50)
- **B.** auditar configurações de cache e headers (SLO 99.95%, VAR 645, Q50)
- **C.** usar credenciais estáticas compartilhadas (SLO 97.0%, VAR 164, Q50)
- **D.** eliminar logs para economizar storage (SLO 97.0%, VAR 357, Q50)

**Respostas corretas:** B

**Racional:** A opção correta prioriza manter SLAs de resposta sem violar times distribuídos com autonomia. Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência.

## Gabarito Final

- Questão 01: A
- Questão 02: C
- Questão 03: A
- Questão 04: B
- Questão 05: B
- Questão 06: B
- Questão 07: A
- Questão 08: C
- Questão 09: A
- Questão 10: A
- Questão 11: B
- Questão 12: C
- Questão 13: B
- Questão 14: B
- Questão 15: D
- Questão 16: D
- Questão 17: B
- Questão 18: D
- Questão 19: B
- Questão 20: A
- Questão 21: C
- Questão 22: A
- Questão 23: B
- Questão 24: D
- Questão 25: D
- Questão 26: C
- Questão 27: C
- Questão 28: A
- Questão 29: B
- Questão 30: B
- Questão 31: D
- Questão 32: D
- Questão 33: A
- Questão 34: A
- Questão 35: B
- Questão 36: B
- Questão 37: C
- Questão 38: D
- Questão 39: C
- Questão 40: C
- Questão 41: D
- Questão 42: D
- Questão 43: D
- Questão 44: D
- Questão 45: D
- Questão 46: A
- Questão 47: B
- Questão 48: A
- Questão 49: C
- Questão 50: B
