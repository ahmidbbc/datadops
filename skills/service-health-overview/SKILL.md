---
name: service-health-overview
argument-hint: "[service, team, or environment]"
description: >
  Quick service health assessment providing a comprehensive overview of current
  service status using key metrics, active alerts, and recent events. Perfect
  for daily health checks, incident triage, or getting rapid service insights.
  Use when you need fast service status or as a starting point for deeper investigation.
compatibility:
  tools: [datadog]
  dependencies: [search_datadog_monitors, get_datadog_metric, search_datadog_events, search_datadog_services]
---

# Service Health Overview

Rapid service health assessment providing actionable insights in under 60 seconds.
When invoked directly with `/datadops:service-health-overview`, use `$ARGUMENTS` as the scope for the report.
If the scope is unclear, ask whether to focus on a service, a team, or an environment.

## Capabilities

### 🩺 Health Dashboard
- Overall service health score (0-100)
- Key performance indicators status
- Active alert summary
- Recent event timeline

### ⚡ Quick Assessment
- Traffic patterns and trends
- Error rate and latency status  
- Infrastructure health indicators
- Dependency service status

### 🎯 Actionable Insights
- Issues requiring immediate attention
- Performance optimization opportunities
- Proactive monitoring recommendations
- Escalation triggers

## Health Check Components

### 1. Service Availability (30% weight)
```
✅ Green (90-100%): All systems operational
🟡 Yellow (75-89%): Minor issues, monitoring required
🔴 Red (0-74%): Critical issues, immediate action needed

Indicators:
- HTTP success rate
- Service uptime
- Critical endpoint availability
```

### 2. Performance Health (25% weight)
```
Metrics:
- Response time percentiles
- Throughput consistency  
- Resource utilization
- Database performance

Thresholds:
- Excellent: All metrics within targets
- Good: Minor performance variations
- Poor: Significant performance degradation
```

### 3. Error Patterns (25% weight)
```
Analysis:
- Error rate trends
- New error types
- Error severity distribution
- Customer impact assessment

Classifications:
- Low: Error rate < 1%, no critical errors
- Medium: Error rate 1-5%, some customer impact
- High: Error rate > 5%, significant customer impact
```

### 4. Infrastructure Status (20% weight)
```
Components:
- Host/container health
- Resource availability
- Network connectivity
- Storage performance

Assessment:
- Healthy: All infrastructure optimal
- Warning: Resource constraints detected
- Critical: Infrastructure failures present
```

## Quick Health Patterns

### 🟢 Healthy Service
```
Overall Score: 95-100

Characteristics:
- Success rate > 99.5%
- Latency within targets
- No active alerts
- Stable resource usage
- Recent deployments successful

Recommended Actions:
- Continue monitoring
- Review performance trends
- Plan capacity for growth
```

### 🟡 Warning State
```
Overall Score: 75-94

Characteristics:
- Success rate 95-99.5%
- Latency slightly elevated
- Minor alerts present
- Increasing resource usage
- Some deployment issues

Recommended Actions:
- Investigate warning indicators
- Review recent changes
- Prepare mitigation plans
- Increase monitoring frequency
```

### 🔴 Critical State
```
Overall Score: 0-74

Characteristics:
- Success rate < 95%
- High latency or timeouts
- Critical alerts firing
- Resource exhaustion
- Failed deployments

Recommended Actions:
- Immediate investigation required
- Escalate to on-call team
- Prepare rollback procedures
- Customer communication
```

## Usage Examples

### Daily Health Check
```
"Give me a health overview of the payment service."
```

**Expected Response:**
- Overall health score and status
- Key metrics summary (success rate, latency, throughput)
- Any active alerts or recent events
- Notable trends or changes
- Recommended actions

### Multi-Service Overview
```
"Check the health of all checkout-related services."
```

**Expected Response:**
- Health scores for all related services
- Service dependency health map
- Cross-service issues or patterns
- Priority services needing attention
- System-level recommendations

### Pre-Meeting Brief
```
"Prepare a service health summary for our team standup."
```

**Expected Response:**
- Concise health status for key services
- Notable incidents or improvements
- Performance trends
- Upcoming concerns or maintenance
- Team focus areas

## Health Metrics

### Golden Signals
- **Latency**: P95 response time < target
- **Traffic**: Request volume within expected range
- **Errors**: Error rate < threshold
- **Saturation**: Resource utilization < limits

### Business Metrics
- **Availability**: Service uptime percentage
- **Performance**: User experience indicators
- **Reliability**: Consistent service delivery
- **Efficiency**: Resource cost optimization

### Leading Indicators
- **Deployment Success**: Recent release health
- **Dependency Health**: Upstream service status
- **Resource Trends**: Capacity planning signals
- **Alert Patterns**: Early warning indicators

## Integration Points

### With Incident Response
- Automatic escalation triggers
- Context for investigation
- Historical health patterns
- Impact assessment

### With Performance Investigation
- Entry point for deep analysis
- Problem area identification
- Resource optimization leads
- Trend analysis starting point

### With Deployment Health
- Pre/post deployment comparison
- Release impact assessment
- Rollback decision support
- Continuous deployment validation

## Customization Options

### Service-Specific Thresholds
```json
{
  "payment_service": {
    "success_rate_target": 99.9,
    "latency_p95_target": 100,
    "error_rate_threshold": 0.1
  },
  "search_service": {
    "success_rate_target": 99.5,
    "latency_p95_target": 500,
    "error_rate_threshold": 0.5
  }
}
```

### Environment-Specific Scoring
- Production: Stricter thresholds
- Staging: Moderate thresholds  
- Development: Relaxed thresholds

### Business Hours Awareness
- Peak traffic expectations
- Maintenance window considerations
- Weekend/holiday adjustments

## Reporting Formats

### Executive Summary
- High-level health status
- Business impact assessment
- Critical issues only
- Strategic recommendations

### Technical Overview
- Detailed metrics and trends
- Infrastructure status
- Performance analysis
- Operational recommendations

### Incident Context
- Current service state
- Recent changes or events
- Dependency impact
- Investigation starting points

## Automation Integration

### Scheduled Health Checks
```bash
# Claude Code interactive invocation
/datadops:service-health-overview critical production services

# Prompt-based automation examples
0 9 * * * claude -p "Give me a health overview of all critical production services. Summarize health scores, active alerts, recent events, and the top recommended actions."
0 * * * * claude -p "Give me a health overview of critical services and mention only active alerts, regressions, and immediate actions."
```

### Alert Integration
- Health degradation notifications
- Automatic escalation triggers
- Status page updates
- Team communication

## Success Metrics

- **Response Time**: Complete overview in < 60 seconds
- **Accuracy**: Health assessment matches detailed investigation
- **Completeness**: Coverage of all critical service aspects
- **Actionability**: Clear next steps for any identified issues
