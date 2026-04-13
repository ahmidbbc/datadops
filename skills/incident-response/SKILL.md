---
name: incident-response
argument-hint: "[service, symptoms, environment]"
description: >
  Comprehensive incident response workflow using Datadog observability data.
  Automatically investigates service issues by correlating logs, metrics, APM traces,
  and infrastructure data. Creates incident timeline and actionable recommendations.
  Use when investigating production issues, service outages, or performance degradations.
compatibility:
  tools: [datadog]
  dependencies: [search_datadog_logs, get_datadog_metric, search_datadog_spans, search_datadog_monitors, search_datadog_events]
---

# Incident Response Workflow

Orchestrates a complete incident investigation using Datadog's observability stack.
When invoked directly with `/datadops:incident-response`, use `$ARGUMENTS` as the investigation context.
If key context is missing, ask for the affected service, environment, and timeframe before proceeding.

## Capabilities

### 🚨 Automatic Issue Detection
- Cross-reference alerting monitors with service health
- Identify correlated failures across multiple services
- Timeline reconstruction from events and deployments

### 🔍 Multi-Signal Investigation
- **Logs Analysis**: Error patterns, stack traces, correlation IDs
- **Metrics Correlation**: Performance indicators, resource utilization
- **APM Traces**: Request flow analysis, bottleneck identification
- **Infrastructure**: Host health, container status, network issues

### 📋 Structured Response
- Incident severity assessment
- Impact analysis (affected users, services)
- Root cause hypothesis generation
- Actionable remediation steps

## Workflow Triggers

Use this skill when:
- "Production is down" or "service is having issues"
- Multiple alerts firing simultaneously
- Performance degradation reports
- Customer-impacting incidents

## Investigation Process

### Phase 1: Rapid Assessment (2-3 minutes)
1. **Monitor Status Check**
   - Query active alerts for target service and dependencies
   - Assess alert severity and duration
   - Identify primary vs secondary failures

2. **Service Health Snapshot**
   - Current error rates, latency percentiles
   - Traffic patterns vs baseline
   - Key infrastructure metrics

### Phase 2: Deep Investigation (5-10 minutes)
3. **Timeline Correlation**
   - Recent deployments or configuration changes
   - Infrastructure events (scaling, failures)
   - External service dependencies

4. **Pattern Analysis**
   - Log error patterns and frequency trends
   - APM trace sampling of failures
   - Database/cache performance correlation

### Phase 3: Root Cause & Response (5-15 minutes)
5. **Root Cause Identification**
   - Synthesize multi-signal evidence
   - Compare with historical incidents
   - Generate testable hypotheses

6. **Response Recommendations**
   - Immediate mitigation steps
   - Rollback procedures if applicable
   - Monitoring points for verification

## Usage Examples

### Service Outage Investigation
```
"Our payment service is returning 500 errors. Investigate the incident and provide next steps."
```

**Expected Response:**
- Current alert status and severity
- Error rate trends and affected endpoints
- Recent deployments or changes
- Infrastructure health (DB, cache, dependencies)
- Specific remediation actions

### Performance Degradation
```
"Users are reporting slow checkout. Analyze the performance issue across the stack."
```

**Expected Response:**
- Latency percentile analysis
- APM trace bottleneck identification
- Resource utilization patterns
- Downstream service impact
- Optimization recommendations

### Cross-Service Impact
```
"Multiple services are alerting. Correlate the failures and identify the root cause."
```

**Expected Response:**
- Service dependency mapping
- Failure propagation analysis
- Common infrastructure or upstream cause
- Prioritized recovery sequence

## Implementation Notes

### Multi-Environment Support
- Automatically detects environment from service tags
- Adjusts investigation scope and urgency
- Environment-specific baseline comparisons

### Context Preservation
- Maintains investigation state across queries
- Links related traces and log entries
- Preserves timeline for post-incident review

### Escalation Triggers
- Recommends escalation when complexity exceeds automation
- Identifies need for subject matter experts
- Suggests communication to stakeholders

## Integration Points

### With Datadog MCP Tools
- `search_datadog_monitors` - Active alert status
- `get_datadog_metric` - Performance indicators
- `search_datadog_logs` - Error patterns and context
- `search_datadog_spans` - Request flow analysis
- `search_datadog_events` - Timeline correlation

### With Case Management
- Creates structured incident records
- Links evidence and investigation steps
- Enables post-mortem generation

### With Communication Tools  
- Formats status updates for stakeholders
- Generates technical summaries for teams
- Provides customer impact assessments

## Success Metrics

- **Time to Detection**: < 5 minutes from symptom to root cause hypothesis
- **Context Quality**: Complete multi-signal correlation
- **Actionability**: Specific next steps with confidence levels
- **Accuracy**: Root cause identification rate in post-incident review
