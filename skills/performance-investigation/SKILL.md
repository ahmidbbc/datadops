---
name: performance-investigation
description: >
  Deep performance analysis using APM traces, metrics, and logs to identify bottlenecks
  and optimization opportunities. Correlates database queries, external API calls,
  and resource usage to pinpoint root causes of slow performance. Use when investigating
  latency issues, throughput problems, or resource optimization needs.
compatibility:
  tools: [datadog-mcp-server]
  dependencies: [search_datadog_spans, get_datadog_metric, analyze_datadog_logs, apm_search_spans]
---

# Performance Investigation

Comprehensive performance analysis across the full application stack to identify and resolve bottlenecks.

## Capabilities

### 🔍 Multi-Layer Analysis
- **Application Layer**: Code-level bottlenecks, algorithm efficiency
- **Database Layer**: Query performance, connection pooling, indexing
- **Infrastructure Layer**: CPU, memory, I/O, network utilization
- **External Dependencies**: Third-party API performance, service meshes

### 📈 Performance Profiling
- Request flow visualization
- Latency breakdown by component
- Resource utilization correlation
- Throughput and concurrency analysis

### 🎯 Optimization Recommendations
- Specific performance improvements
- Infrastructure scaling suggestions
- Code optimization opportunities
- Caching strategy recommendations

## Investigation Methodology

### Phase 1: Performance Characterization
1. **Baseline Establishment**
   - Current performance percentiles (P50, P95, P99)
   - Throughput and error rate baselines
   - Resource utilization patterns

2. **Bottleneck Identification**
   - Slowest endpoints and operations
   - Most resource-intensive requests
   - Error-prone performance patterns

### Phase 2: Deep Trace Analysis
3. **Request Flow Mapping**
   - End-to-end request tracing
   - Service dependency visualization
   - Latency contribution breakdown

4. **Database Performance**
   - Query execution time analysis
   - Connection pool utilization
   - Index effectiveness assessment

### Phase 3: Resource Correlation
5. **Infrastructure Metrics**
   - CPU, memory, disk I/O patterns
   - Network bandwidth and latency
   - Container/host resource contention

6. **Scaling Patterns**
   - Performance under load
   - Resource scaling effectiveness
   - Bottleneck migration analysis

## Performance Patterns

### Database Bottlenecks
```
Symptoms:
- High database query latency
- Connection pool exhaustion
- Lock contention

Investigation:
- Slow query identification
- Query execution plan analysis
- Database resource utilization
- Connection pool metrics

Recommendations:
- Index optimization
- Query restructuring
- Connection pool tuning
- Read replica utilization
```

### Memory/CPU Constraints
```
Symptoms:
- High memory utilization
- CPU throttling
- Garbage collection overhead

Investigation:
- Memory allocation patterns
- CPU utilization spikes
- GC frequency and duration
- Thread pool utilization

Recommendations:
- Memory optimization
- Vertical/horizontal scaling
- GC tuning
- Resource allocation adjustments
```

### External API Dependencies
```
Symptoms:
- External service timeouts
- Cascading latency issues
- Dependency error propagation

Investigation:
- External API response times
- Circuit breaker effectiveness
- Retry pattern analysis
- Fallback mechanism performance

Recommendations:
- Timeout optimization
- Circuit breaker tuning
- Caching strategies
- Async processing patterns
```

## Usage Examples

### API Endpoint Performance
```
"The /checkout endpoint is very slow. Investigate what's causing the latency."
```

**Expected Analysis:**
- Trace analysis of checkout requests
- Database query performance in checkout flow
- External service dependencies (payment, inventory)
- Resource utilization during checkout operations
- Specific optimization recommendations

### Service-Wide Performance Review
```
"Our user service performance has degraded over the past week. What's the root cause?"
```

**Expected Analysis:**
- Week-over-week performance comparison
- Trend analysis of key metrics
- Code deployment correlation
- Infrastructure changes impact
- Systematic performance improvement plan

### Database Performance Issues
```
"Database queries are timing out frequently. Analyze the database performance."
```

**Expected Analysis:**
- Slow query identification and analysis
- Database resource utilization patterns
- Connection pool health and sizing
- Query optimization opportunities
- Infrastructure scaling recommendations

## Optimization Frameworks

### Application-Level Optimizations
```
1. Algorithm Efficiency
   - Time complexity analysis
   - Data structure optimization
   - Caching implementation

2. Concurrency Patterns
   - Thread pool optimization
   - Async processing adoption
   - Parallelization opportunities

3. Resource Management
   - Memory allocation optimization
   - Connection reuse strategies
   - Resource cleanup patterns
```

### Infrastructure Optimizations
```
1. Scaling Strategies
   - Horizontal vs vertical scaling
   - Auto-scaling configuration
   - Load distribution optimization

2. Resource Allocation
   - CPU/memory right-sizing
   - Storage optimization
   - Network bandwidth planning

3. Caching Layers
   - Application-level caching
   - Database query caching
   - CDN optimization
```

## Performance Metrics Framework

### Golden Signals
- **Latency**: Response time distribution
- **Traffic**: Request rate and patterns
- **Errors**: Error rate and types
- **Saturation**: Resource utilization levels

### Business Impact Metrics
- **User Experience**: Page load times, interaction responsiveness
- **Conversion Impact**: Performance effect on business outcomes
- **Cost Efficiency**: Resource cost per transaction
- **Scalability**: Performance under increasing load

## Investigation Tools Integration

### APM Trace Analysis
- Request flow visualization
- Span duration analysis
- Error correlation
- Dependency mapping

### Metrics Correlation
- Performance metric trends
- Resource utilization patterns
- Business metric impact
- Baseline comparisons

### Log Analysis
- Performance-related log patterns
- Error frequency analysis
- Resource exhaustion indicators
- Timing correlation

## Optimization Recommendations

### Immediate Actions (0-24 hours)
- Configuration parameter tuning
- Resource allocation adjustments
- Cache policy optimization
- Connection pool sizing

### Short-term Improvements (1-4 weeks)
- Code optimization implementation
- Database index creation
- Infrastructure scaling
- Monitoring enhancement

### Long-term Strategies (1-3 months)
- Architecture pattern changes
- Technology stack upgrades
- Capacity planning
- Performance testing integration

## Success Metrics

- **Investigation Speed**: Root cause identification within 30 minutes
- **Recommendation Quality**: Measurable performance improvements
- **Coverage**: Analysis across all stack layers
- **Actionability**: Prioritized recommendations with impact estimates

## Performance Baselines

### Response Time Targets
- API endpoints: < 200ms P95
- Database queries: < 100ms P95
- External API calls: < 500ms P95
- Page loads: < 2 seconds P95

### Resource Utilization
- CPU usage: < 70% sustained
- Memory usage: < 80% sustained
- Database connections: < 80% pool utilization
- Queue depths: < 100 messages sustained