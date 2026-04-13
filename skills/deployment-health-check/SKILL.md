---
name: deployment-health-check
argument-hint: "[service, version, environment]"
description: >
  Automated post-deployment health verification using Datadog metrics, logs, and APM data.
  Compares service health before/after deployment, detects regressions, and provides
  rollback recommendations. Use after deployments to validate release success and
  catch issues early.
compatibility:
  tools: [datadog]
  dependencies: [get_datadog_metric, search_datadog_logs, search_datadog_spans, search_datadog_events]
---

# Deployment Health Check

Validates deployment success through comprehensive health monitoring and regression detection.
When invoked directly with `/datadops:deployment-health-check`, use `$ARGUMENTS` as the deployment context.
If needed, ask for the service name, version, environment, and deployment window before continuing.

## Capabilities

### 📊 Before/After Comparison
- Baseline metrics capture pre-deployment
- Post-deployment performance analysis
- Statistical significance testing
- Regression severity assessment

### 🔍 Multi-Dimensional Health Check
- **Golden Signals**: Error rate, latency, throughput, saturation
- **Custom Metrics**: Business KPIs and service-specific indicators
- **Log Patterns**: New error types, warning frequencies
- **APM Performance**: Trace latency distribution, dependency health

### ⚡ Early Warning System
- Real-time monitoring during deployment window
- Automated anomaly detection
- Progressive rollout validation
- Canary deployment analysis

## Health Check Dimensions

### 1. Service Performance
```
- Request success rate (target: > 99.5%)
- Response time percentiles (P50, P95, P99)
- Throughput consistency
- Memory/CPU utilization patterns
```

### 2. Error Patterns
```
- New error types or frequencies
- HTTP status code distributions  
- Exception rate changes
- Dependency failure impacts
```

### 3. Infrastructure Health
```
- Host resource utilization
- Container restart rates
- Network connectivity
- Database connection pools
```

### 4. Business Metrics
```
- Conversion rates
- User engagement metrics
- Revenue-impacting indicators
- Customer experience scores
```

## Workflow Process

### Phase 1: Baseline Capture (Pre-deployment)
1. **Metrics Snapshot**
   - Capture 1-hour baseline before deployment
   - Record key performance indicators
   - Document expected traffic patterns

2. **Health Thresholds**
   - Calculate statistical baselines
   - Set regression detection thresholds
   - Define success/failure criteria

### Phase 2: Deployment Monitoring (During)
3. **Real-time Tracking**
   - Monitor deployment events and progress
   - Track immediate health indicators
   - Alert on deployment-blocking issues

### Phase 3: Post-deployment Validation (After)
4. **Comparison Analysis**
   - Compare 30-60 minutes post vs baseline
   - Statistical significance testing
   - Trend analysis and projections

5. **Health Assessment**
   - Overall deployment health score
   - Specific regression identification
   - Risk assessment and recommendations

## Usage Examples

### Standard Deployment Check
```
"I just deployed version 2.1.4 of the payment service. Validate the deployment health."
```

**Expected Response:**
- Deployment event correlation
- Before/after metric comparisons
- Error rate and latency analysis
- Health score and recommendations

### Canary Deployment Validation
```
"Check if the canary deployment of checkout service is performing well compared to production."
```

**Expected Response:**
- Canary vs production performance comparison
- Statistical significance of differences
- Recommendations for traffic ramp-up
- Rollback triggers if needed

### Rollback Decision Support
```
"Should we rollback the API service deployment? Performance seems degraded."
```

**Expected Response:**
- Quantified performance regression analysis
- Impact assessment (user experience, business metrics)
- Rollback recommendation with confidence level
- Monitoring plan if continuing with deployment

## Health Check Templates

### Microservice Health Check
- API response times and success rates
- Database query performance
- Cache hit rates and performance
- Downstream service dependencies

### Frontend Application Check
- Page load times and user interactions
- JavaScript error rates
- CDN performance metrics
- User engagement indicators  

### Infrastructure Service Check
- Resource utilization patterns
- Service discovery health
- Load balancer performance
- Auto-scaling behavior

## Integration Patterns

### CI/CD Pipeline Integration
```bash
# Claude Code interactive invocation
/datadops:deployment-health-check payment service version 2.1.4 in production

# Prompt-based automation example
claude -p "Validate deployment health for $SERVICE_NAME version $GITHUB_SHA in $ENVIRONMENT. Compare pre-deployment and post-deployment metrics, logs, spans, and events, then give a go/no-go recommendation."
```

### Automated Rollback Triggers
- Health score below threshold (< 80%)
- Error rate increase > 2x baseline  
- Latency regression > 50% increase
- Critical business metric degradation

## Risk Assessment Framework

### Low Risk (Score: 90-100%)
- All metrics within expected ranges
- No significant error pattern changes
- Performance improvements or neutral
- **Action**: Continue monitoring

### Medium Risk (Score: 70-89%)
- Minor performance regressions
- Slight error rate increases
- Some concerning log patterns
- **Action**: Enhanced monitoring, prepare rollback

### High Risk (Score: < 70%)
- Significant performance degradation
- Major error rate increases
- Customer-impacting issues
- **Action**: Consider immediate rollback

## Success Criteria

- **Detection Speed**: Identify regressions within 15 minutes
- **Accuracy**: < 5% false positive rate on health assessments
- **Coverage**: Monitor 100% of critical service indicators
- **Actionability**: Clear go/no-go recommendations with confidence scores

## Customization Options

### Service-Specific Thresholds
- Custom success rate targets per service
- Business-critical metric weightings  
- Environment-specific baselines

### Deployment Window Awareness
- Time-based baseline adjustments
- Traffic pattern expectations
- Seasonal/cyclical considerations
