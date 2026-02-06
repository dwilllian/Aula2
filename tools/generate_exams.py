import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import random

ROLES = [
    ("devops", "pleno"),
    ("devops", "senior"),
    ("devsecops", "pleno"),
    ("devsecops", "senior"),
    ("frontend", "pleno"),
    ("frontend", "senior"),
    ("backend", "pleno"),
    ("backend", "senior"),
    ("arquitetoMulticloud", "pleno"),
    ("arquitetoMulticloud", "senior"),
]

PROVIDERS = ["AWS", "Azure", "GCP", "OCI", "Agnóstico"]
CATEGORIES = ["Arquitetura & Estratégia", "Troubleshooting & Incident Response"]

TOPICS = {
    "devops": [
        "pipeline de entrega contínua com gates de segurança",
        "auto scaling baseado em filas e métricas customizadas",
        "observabilidade unificada com tracing distribuído",
        "estratégia de DR multi-região",
        "padronização de artefatos e assinatura",
        "provisionamento com infraestrutura como código",
        "blue/green com controle de tráfego",
        "otimização de custos com autoscaling preditivo",
        "segregação de redes e endpoints privados",
        "gestão de releases com feature flags",
    ],
    "devsecops": [
        "esteira de CI/CD com SAST, SCA e assinatura",
        "gestão de segredos com rotação automática",
        "validação de imagem e policy-as-code",
        "deteção de drift e conformidade contínua",
        "segurança de APIs com OAuth/OIDC",
        "isolamento de workloads por identidade",
        "proteção contra supply chain attacks",
        "hardening de runtime e observabilidade",
        "criptografia end-to-end e KMS",
        "gestão de vulnerabilidades em containers",
    ],
    "frontend": [
        "performance Web Core Vitals em aplicação React",
        "renderização híbrida com Next.js",
        "gestão de estado com consistência eventual",
        "cache de assets e invalidation",
        "observabilidade de erros no cliente",
        "microfrontends com isolamento",
        "segurança de conteúdo com CSP",
        "acessibilidade e internacionalização",
        "autenticação com sessões e tokens",
        "entrega via CDN e edge compute",
    ],
    "backend": [
        "serviços gRPC com versionamento",
        "cache distribuído com Redis",
        "mensageria Kafka com idempotência",
        "multi-tenant em banco relacional",
        "rate limiting em APIs",
        "autenticação e autorização centralizadas",
        "migrações online sem downtime",
        "observabilidade com tracing",
        "resiliência com circuit breaker",
        "processamento assíncrono e filas",
    ],
    "arquitetoMulticloud": [
        "topologia hub-spoke multi-cloud",
        "estratégia active-active global",
        "federacao de identidades",
        "service mesh entre clouds",
        "segurança zero trust",
        "padronização de landing zones",
        "governança e tagging",
        "roteamento global e DNS",
        "observabilidade cross-cloud",
        "gestão de chaves e HSM",
    ],
}

SERVICE_SNIPPETS = {
    "AWS": ["ALB", "EKS", "RDS", "S3", "CloudFront", "WAF", "SQS", "KMS"],
    "Azure": ["Application Gateway", "AKS", "Azure SQL", "Blob", "Front Door", "WAF", "Service Bus", "Key Vault"],
    "GCP": ["HTTPS LB", "GKE", "Cloud SQL", "GCS", "Cloud CDN", "Cloud Armor", "Pub/Sub", "KMS"],
    "OCI": ["Load Balancer", "OKE", "Autonomous DB", "Object Storage", "CDN", "WAF", "Queue", "Vault"],
    "Agnóstico": ["Ingress", "Kubernetes", "Postgres", "Object Storage", "CDN", "WAF", "Queue", "KMS"],
}

CONSTRAINTS = [
    "sem janela de manutenção",
    "RPO máximo de {rpo} minutos",
    "RTO máximo de {rto} minutos",
    "requisitos de latência abaixo de {lat} ms",
    "conformidade com ISO 27001 e LGPD",
    "tráfego com picos imprevisíveis",
    "orçamento com teto mensal",
    "times distribuídos com autonomia",
    "ciclos de release semanais",
    "ambiente com compliance PCI",
]

OBJECTIVES = [
    "reduzir tempo de recuperação",
    "garantir rastreabilidade de mudanças",
    "minimizar risco de rollback",
    "aumentar disponibilidade global",
    "diminuir tempo de build",
    "evitar regressões de performance",
    "garantir segurança de dados sensíveis",
    "reduzir custo de infraestrutura",
    "manter SLAs de resposta",
    "padronizar governança",
]

INCIDENTS = [
    "picos de latência no tráfego de API",
    "erros 5xx intermitentes",
    "fila crescendo sem consumo",
    "expiração inesperada de tokens",
    "alta taxa de cache miss",
    "falhas na autenticação",
    "degeneração de throughput",
    "loop de deploy com rollback",
    "aumento súbito de CPU",
    "falha na replicação de banco",
]

ARCH_ACTIONS = [
    "implementar {edge} com regras de cache e WAF",
    "usar {lb} com health checks avançados",
    "adotar {app} com auto scaling baseado em métricas",
    "introduzir {db} com read replicas",
    "incluir {cache} com TTL e invalidation",
    "associar {queue} para desacoplamento",
    "habilitar {kms} para criptografia e rotação",
    "centralizar logs com tracing distribuído",
]

TROUBLE_ACTIONS = [
    "revisar métricas de saturação e ajustar limites",
    "validar políticas de autoscaling e backoff",
    "inspecionar erros de autenticação no IdP",
    "verificar latência entre zonas e ajustar routing",
    "auditar configurações de cache e headers",
    "analisar dead-letter queue e reprocessamento",
    "corrigir health checks e probes",
    "mitigar com feature flag e rollback controlado",
]

DISTRACTORS = [
    "desativar controles de segurança para reduzir latência",
    "consolidar todos os serviços em uma única VM",
    "expor o banco diretamente à internet",
    "eliminar logs para economizar storage",
    "usar credenciais estáticas compartilhadas",
    "desabilitar criptografia para ganho imediato",
    "aumentar timeout sem investigar causa",
    "remover WAF para simplificar tráfego",
]


def build_question(rng, role, level, idx, diagram=False):
    provider = rng.choice(PROVIDERS)
    category = rng.choice(CATEGORIES)
    topic = rng.choice(TOPICS[role])

    rpo = rng.choice([5, 10, 15, 30, 60])
    rto = rng.choice([10, 20, 30, 45, 60])
    lat = rng.choice([50, 80, 120, 200])

    constraint = rng.choice(CONSTRAINTS).format(rpo=rpo, rto=rto, lat=lat)
    objective = rng.choice(OBJECTIVES)

    services = rng.sample(SERVICE_SNIPPETS[provider], k=4)
    edge, lb, app, db = services[:4]
    cache = rng.choice(SERVICE_SNIPPETS[provider])
    queue = rng.choice(SERVICE_SNIPPETS[provider])
    kms = rng.choice(SERVICE_SNIPPETS[provider])

    context = (
        f"Você está trabalhando em {topic} para um sistema crítico no provedor {provider}. "
        f"O cenário atual envolve {rng.choice(['equipes distribuídas', 'crescimento acelerado', 'dependências legadas'])}, "
        f"e há necessidade de padronização técnica."
    )
    restriction = f"Restrições: {constraint}."
    objective_line = f"Objetivo: {objective}."

    if category == "Arquitetura & Estratégia":
        question = "Qual alternativa atende melhor aos requisitos descritos?"
        action_pool = ARCH_ACTIONS
    else:
        incident = rng.choice(INCIDENTS)
        context = (
            f"Durante operação de {topic}, o time observou {incident} no provedor {provider}. "
            f"Os alerts indicam impacto direto nos usuários finais."
        )
        question = "Qual é a ação mais eficaz para mitigar o incidente sem violar as restrições?"
        action_pool = TROUBLE_ACTIONS

    options = []
    correct_indices = []
    option_variants = rng.sample(range(100, 999), k=8)
    for i in range(4):
        if category == "Arquitetura & Estratégia":
            action = rng.choice(action_pool).format(
                edge=edge, lb=lb, app=app, db=db, cache=cache, queue=queue, kms=kms
            )
        else:
            action = rng.choice(action_pool)
        suffix = f"(SLO {rng.choice(['99.5', '99.9', '99.95'])}%, VAR {option_variants[i]}, Q{idx:02d})"
        options.append(f"{action} {suffix}")

    if level == "pleno":
        correct_count = 1
    else:
        correct_count = rng.choice([2, 3])

    correct_indices = rng.sample(range(4), k=correct_count)

    for i in range(4 - correct_count):
        distractor = rng.choice(DISTRACTORS)
        suffix = f"(SLO 97.0%, VAR {option_variants[4 + i]}, Q{idx:02d})"
        insert_at = [i for i in range(4) if i not in correct_indices][i]
        options[insert_at] = f"{distractor} {suffix}"

    answer_labels = ["A", "B", "C", "D"]
    correct_labels = [answer_labels[i] for i in sorted(correct_indices)]
    correct_texts = [options[i] for i in correct_indices]

    rationale = (
        f"A opção correta prioriza {objective} sem violar {constraint}. "
        f"Ela mantém governança e reduz risco operacional, ao contrário das alternativas que comprometem segurança ou resiliência."
    )

    return {
        "index": idx,
        "provider": provider,
        "category": category,
        "topic": topic,
        "context": context,
        "restriction": restriction,
        "objective": objective_line,
        "question": question,
        "options": options,
        "correct_labels": correct_labels,
        "correct_texts": correct_texts,
        "rationale": rationale,
        "diagram": diagram,
        "diagram_spec": {
            "provider": provider,
            "nodes": [
                {"id": "edge_node", "label": f"Edge/CDN\n{edge}"},
                {"id": "waf", "label": "WAF"},
                {"id": "lb", "label": f"LB\n{lb}"},
                {"id": "app", "label": f"App\n{app}"},
                {"id": "cache", "label": f"Cache\n{cache}"},
                {"id": "queue", "label": f"Queue\n{queue}"},
                {"id": "db", "label": f"DB\n{db}"},
                {"id": "obs", "label": "Observability"},
                {"id": "kms", "label": f"KMS\n{kms}"},
            ],
            "edges": [
                ["edge_node", "waf"],
                ["waf", "lb"],
                ["lb", "app"],
                ["app", "cache"],
                ["app", "queue"],
                ["app", "db"],
                ["app", "obs"],
                ["db", "kms"],
            ],
        },
    }


def ensure_unique_options(questions):
    seen = set()
    for q in questions:
        for option in q["options"]:
            if option in seen:
                raise ValueError(f"Duplicate option text detected: {option}")
            seen.add(option)


def write_exam(output_root, role, level, questions):
    exam_name = f"{role}_{level}"
    candidate_path = output_root / f"{exam_name}_candidato.md"
    answer_path = output_root / f"{exam_name}_gabarito.md"

    def write_header(fh, include_answers):
        fh.write(f"# Prova Técnica {role.title()} ({level.title()})\n\n")
        fh.write("**Quantidade de questões:** 50\n\n")
        fh.write("**Tempo estimado:** 60–90 minutos\n\n")
        fh.write("**Peso das questões:** iguais\n\n")
        if include_answers:
            fh.write("**Instruções:** Marque todas as alternativas corretas.\n\n")
        else:
            fh.write("**Instruções:** Selecione a melhor alternativa (Pleno) ou todas as corretas (Senior).\n\n")

    with candidate_path.open("w", encoding="utf-8") as fh:
        write_header(fh, include_answers=False)
        for q in questions:
            fh.write(f"### Questão {q['index']:02d}\n\n")
            fh.write(f"**Categoria:** {q['category']}\n\n")
            fh.write(f"**Provedor:** {q['provider']}\n\n")
            fh.write(f"{q['context']}\n\n")
            fh.write(f"{q['restriction']}\n\n")
            fh.write(f"{q['objective']}\n\n")
            if q["diagram"]:
                fh.write(f"![diagram](assets/diagrams/{exam_name}/q{q['index']:02d}.png)\n\n")
            fh.write(f"{q['question']}\n\n")
            for label, option in zip(["A", "B", "C", "D"], q["options"]):
                fh.write(f"- **{label}.** {option}\n")
            fh.write("\n")

    with answer_path.open("w", encoding="utf-8") as fh:
        write_header(fh, include_answers=True)
        answer_map = []
        for q in questions:
            fh.write(f"### Questão {q['index']:02d}\n\n")
            fh.write(f"**Categoria:** {q['category']}\n\n")
            fh.write(f"**Provedor:** {q['provider']}\n\n")
            fh.write(f"{q['context']}\n\n")
            fh.write(f"{q['restriction']}\n\n")
            fh.write(f"{q['objective']}\n\n")
            if q["diagram"]:
                fh.write(f"![diagram](assets/diagrams/{exam_name}/q{q['index']:02d}.png)\n\n")
            fh.write(f"{q['question']}\n\n")
            for label, option in zip(["A", "B", "C", "D"], q["options"]):
                fh.write(f"- **{label}.** {option}\n")
            answers = ", ".join(q["correct_labels"])
            fh.write(f"\n**Respostas corretas:** {answers}\n\n")
            fh.write(f"**Racional:** {q['rationale']}\n\n")
            answer_map.append({"questao": q["index"], "respostas": q["correct_labels"]})

        fh.write("## Gabarito Final\n\n")
        for item in answer_map:
            fh.write(f"- Questão {item['questao']:02d}: {', '.join(item['respostas'])}\n")

    return candidate_path, answer_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", default="provas_v3_profissional")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    output_root = Path(args.output)
    output_root.mkdir(parents=True, exist_ok=True)

    diagrams_root = output_root / "assets" / "diagrams"
    specs_root = output_root / "specs"
    diagrams_root.mkdir(parents=True, exist_ok=True)
    specs_root.mkdir(parents=True, exist_ok=True)

    manifest = {
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "seed": args.seed,
        "provas": [],
        "files": {},
        "file_question_map": {},
    }

    for role, level in ROLES:
        exam_name = f"{role}_{level}"
        diagram_ratio = {
            "devops": 0.5,
            "devsecops": 0.55,
            "frontend": 0.3,
            "backend": 0.35,
            "arquitetoMulticloud": 0.6,
        }[role]
        diagram_count = int(round(50 * diagram_ratio))
        diagram_indices = set(rng.sample(range(1, 51), k=diagram_count))

        questions = []
        provider_counts = {p: 0 for p in PROVIDERS}
        category_counts = {c: 0 for c in CATEGORIES}
        diagram_specs = []

        for i in range(1, 51):
            q = build_question(
                rng,
                role,
                level,
                i,
                diagram=i in diagram_indices,
            )
            questions.append(q)
            provider_counts[q["provider"]] += 1
            category_counts[q["category"]] += 1
            if q["diagram"]:
                diagram_specs.append({
                    "question": i,
                    "exam": exam_name,
                    "spec": q["diagram_spec"],
                })

        ensure_unique_options(questions)

        candidate_path, answer_path = write_exam(output_root, role, level, questions)

        spec_path = specs_root / f"{exam_name}.json"
        with spec_path.open("w", encoding="utf-8") as fh:
            json.dump({"exam": exam_name, "diagrams": diagram_specs}, fh, indent=2, ensure_ascii=False)

        for file_path in [candidate_path, answer_path, spec_path]:
            content = file_path.read_bytes()
            manifest["files"][str(file_path)] = hashlib.sha256(content).hexdigest()
            if file_path.suffix == ".md":
                manifest["file_question_map"][str(file_path)] = [q["index"] for q in questions]

        manifest["provas"].append({
            "name": exam_name,
            "role": role,
            "level": level,
            "questions": 50,
            "diagram_count": len(diagram_specs),
            "providers": provider_counts,
            "categories": category_counts,
            "files": [str(candidate_path), str(answer_path), str(spec_path)],
        })

    manifest_path = output_root / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    manifest["files"][str(manifest_path)] = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
