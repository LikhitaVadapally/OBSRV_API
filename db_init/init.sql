-- Connect to the default database (obsrv_db)
\connect obsrv_db;

-- Create datasets table if not exists
CREATE TABLE IF NOT EXISTS datasets (
    id TEXT PRIMARY KEY,
    dataset_id TEXT,
    type TEXT NOT NULL,
    name TEXT,
    validation_config JSON,
    extraction_config JSON,
    dedup_config JSON,
    data_schema JSON,
    denorm_config JSON,
    router_config JSON,
    dataset_config JSON,
    status TEXT,
    tags TEXT[],
    data_version INT,
    created_by TEXT,
    updated_by TEXT,
    created_date TIMESTAMP NOT NULL DEFAULT now(),
    updated_date TIMESTAMP NOT NULL,
    published_date TIMESTAMP NOT NULL DEFAULT now()
);


INSERT INTO datasets (
    id, dataset_id, type, name, validation_config, extraction_config, dedup_config, data_schema,
    denorm_config, router_config, dataset_config, status, tags, data_version, created_by, updated_by,
    created_date, updated_date, published_date
) VALUES (
    'observations-transformed', 'observations-transformed', 'dataset', 'observations-transformed',
    '{"validate": true, "mode": "Strict", "validation_mode": "Strict"}'::json,
    '{"is_batch_event": true, "extraction_key": "events", "dedup_config": {"drop_duplicates": true, "dedup_key": "id", "dedup_period": 720}, "batch_id": "id"}'::json,
    '{"drop_duplicates": true, "dedup_key": "id", "dedup_period": 720}'::json,
    '{"$schema": "https://json-schema.org/draft/2020-12/schema", "title": "Canonical Observations", "description": "A canonical observation ", "type": "object", "properties": {"obsCode": {"type": "string"}}}'::json,
    '{"redis_db_host": "192.168.106.2", "redis_db_port": 6379, "denorm_fields": [{"denorm_key": "assetRef", "redis_db": 3, "denorm_out_field": "assetMeta"}]}'::json,
    '{"topic": "observations-transformed"}'::json,
    '{}'::json,
    'Live',
    ARRAY['tag1', 'tag2'],
    1,
    'SYSTEM',
    'SYSTEM',
    now(),
    now(),
    now()
);