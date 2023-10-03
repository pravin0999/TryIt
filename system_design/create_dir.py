import os

# List of system design categories and related algorithms
system_designs = {
    # "rate_limiters":
    # ["fixed_window", "token_bucket", "sliding_window", "leaky_bucket"],
    # "load_balancing": ["round_robin", "least_connections", "ip_hashing"],
    # "caching": ["LRU_cache", "LFU_cache", "MRU_cache"],
    # "data_sharding": ["consistent_hashing", "range_based", "hash_based"],
    # "database_replication": ["master_slave", "master_master", "sharding"],
    # "fault_tolerance": ["failover", "failback", "clustering"],
    # "concurrency": ["thread_safe", "distributed_lock", "distributed_semaphore"],
    # "distributed_transaction": ["distributed_lock", "distributed_semaphore"],
    # "content_based_filtering": ["bloom_filter", "inverted_index", "tf_idf"],
    # "search_engine": ["inverted_index", "hash_table", "R_tree"],
    # "content_delegating_storage": ["object_storage", "block_storage", "file_system"],
    # "content_based_recommendation": ["cosine_similarity", "cosine_distance"],
    # "content_delivery_network": ["CDN", "edge_server", "edge_cache"],
    # "unique_id_generation": ["UUID", "hash_id", "random_id"],
    # "retry_policy": ["exponential_backoff", "jitter_backoff", "linear_backoff"],
    # "task_scheduling": ["round_robin", "priority_queue", "priority_queue_with_fifo"],
    # "log_aggregation": ["log_aggregation", "log_aggregation_with_rollup"],
    # "blob_storage": ["object_storage", "block_storage", "file_system"],
    # "counters": ["distributed_counter", "distributed_counter_with_ttl"],
    # "dns_lookup": ["DNS", "DNS_over_HTTPS"],
    # "batch_processing": ["batch_processing", "batch_processing_with_ttl"],
    
  
    # Add more categories and their algorithms here
}

for category, algorithms in system_designs.items():
  os.makedirs(category, exist_ok=True)  # creating directory for each category
  for algorithm in algorithms:
    with open(f"{category}/{algorithm}.py", 'w') as f:
      f.write("# Add algorithm description here\n\n")
