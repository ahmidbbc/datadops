# 📊 DatadOps - Installation Guide

## Overview

The DatadOps plugin provides intelligent workflows on top of the official Datadog MCP server, enabling advanced incident response, performance investigation, and deployment validation capabilities.
The plugin bundles the Datadog MCP server configuration, so users do not need to run `claude mcp add ...` manually.

## Prerequisites

✅ **Claude Code** with MCP support  
✅ **Datadog account** with API access  
✅ **Internet connection** for OAuth authentication  

## Installation Steps

### 1. Install the DatadOps Plugin

```bash
# Install the plugin from your configured marketplace
claude plugin install datadops
```

If you install or update the plugin during an active Claude Code session, run:

```text
/reload-plugins
```

**What this does:**
- Installs the DatadOps plugin
- Registers the official Datadog MCP server configuration bundled with the plugin
- Exposes the Datadog monitoring tools needed by the DatadOps skills
- Makes the workflows available in Claude Code

### 2. Authenticate with Datadog

1. **Start Claude Code** and open a new session
2. **Type `/mcp`** to manage your MCP servers
3. **Select "datadog"** from the list
4. **Click "Authenticate"**
5. **Browser opens** - login to your Datadog account
6. **Click "Allow Access"** to authorize Claude Code
7. **Return to Claude Code** - should see "Authentication successful"

If you are installing the plugin manually instead of through a marketplace:
```bash
# Clone/copy the plugin to your Claude plugins directory
cp -r datadops ~/.claude/plugins/
```

### 3. Verify Installation

Test that everything works:

```
Ask Claude: "Give me a health overview of our production services"
```

**Expected result:**
- Claude uses the bundled `datadog` MCP server to fetch data
- The service-health-overview skill provides structured analysis
- You get a comprehensive health dashboard

## Configuration

### Environment Detection

The plugin automatically detects your Datadog environment based on:
- Service tags (`env:prod`, `env:staging`, etc.)
- Dashboard organization
- Monitor naming conventions

### Service Discovery

Services are discovered through:
- APM service catalog
- Monitor configurations  
- Dashboard widgets
- Log service tags

### Custom Thresholds

You can customize health thresholds per service:

```json
// ~/.claude/datadops-config.json
{
  "services": {
    "payment-api": {
      "success_rate_target": 99.9,
      "latency_p95_target": 100,
      "error_rate_threshold": 0.1
    },
    "search-service": {
      "success_rate_target": 99.5,
      "latency_p95_target": 500,
      "error_rate_threshold": 0.5
    }
  },
  "environments": {
    "prod": {
      "strict_thresholds": true,
      "alert_escalation": true
    },
    "staging": {
      "relaxed_thresholds": true,
      "alert_escalation": false
    }
  }
}
```

## Available Skills

### 🚨 Incident Response
**Trigger**: "Investigate incident", "service is down", "production issues"
- Comprehensive incident analysis
- Multi-signal correlation (logs, metrics, traces)
- Timeline reconstruction  
- Actionable remediation steps

### 🔍 Performance Investigation  
**Trigger**: "Performance issue", "slow response", "investigate bottleneck"
- APM trace analysis
- Database performance correlation
- Resource utilization patterns
- Optimization recommendations

### 🩺 Service Health Overview
**Trigger**: "Health check", "service status", "system overview"
- Overall service health scoring
- Key metrics dashboard
- Active alert summary
- Trend analysis

### 📋 Deployment Health Check
**Trigger**: "Validate deployment", "check release", "deployment health"
- Before/after deployment comparison
- Regression detection
- Performance impact analysis
- Rollback recommendations

## Usage Examples

### Daily Operations

```
# Morning health check
"Give me a health overview of all critical services"

# Incident investigation
"Payment service is returning 500 errors. Investigate the issue."

# Performance troubleshooting
"Checkout is slow. What's causing the performance problem?"

# Post-deployment validation
"I deployed v1.2.3 of the API service. Is it healthy?"
```

### Workflow Integration

```yaml
# CI/CD pipeline integration
- name: Post-deployment Health Check
  run: |
    claude -p "Validate deployment health for $SERVICE_NAME version $VERSION in $ENVIRONMENT. Compare pre-deployment and post-deployment metrics, logs, spans, and events, then return a go/no-go recommendation."

# Incident response runbook
- name: Automated Investigation
  run: |
    claude -p "Investigate the incident affecting $SERVICE_NAME in $ENVIRONMENT. Correlate monitors, logs, spans, and recent events, then provide severity, likely root cause, and immediate next steps."
```

## Troubleshooting

### Authentication Issues

**Problem**: "Authentication failed" when connecting to Datadog
**Solution**:
1. Verify you have admin access to your Datadog account
2. Check that OAuth is enabled in your organization
3. Try authentication in incognito/private browser window

### Missing Data

**Problem**: "No data found for service"
**Solution**:
1. Verify service name matches Datadog service catalog
2. Check that APM is properly configured for the service
3. Ensure proper tagging (especially `env` tags)

### Performance Issues

**Problem**: Skills are slow to respond
**Solution**:
1. Check your Datadog account's rate limits
2. Reduce the time range for analysis
3. Focus on specific services rather than organization-wide queries

### Skills Not Triggering

**Problem**: Claude doesn't use the Datadog skills
**Solution**:
1. Verify the plugin is properly installed
2. Verify the bundled `datadog` MCP server appears in `/mcp`
3. Use more specific trigger phrases from the skill descriptions
4. Explicitly mention the service or environment name

## Rate Limits

The official Datadog MCP server has fair-use limits:
- **50 requests per 10 seconds** (burst)
- **5,000 daily tool calls**
- **50,000 monthly tool calls**

The DatadOps plugin optimizes these by:
- Batching related queries
- Caching frequently accessed data
- Using efficient query patterns

## Support

### Getting Help

1. **Plugin Issues**: Check the plugin documentation and examples
2. **MCP Server Issues**: Refer to [Datadog MCP documentation](https://docs.datadoghq.com/bits_ai/mcp_server/)
3. **Authentication Issues**: Contact your Datadog admin

### Feedback

The plugin is designed to improve based on real usage patterns:
- Share successful workflows and use cases
- Report issues with specific service types or configurations
- Suggest additional skills or optimizations

## Security Notes

### Data Access
- The plugin only reads Datadog data (no writes except for case management)
- Respects all Datadog RBAC and permissions
- No data is stored locally or transmitted to third parties

### Authentication
- Uses official Datadog OAuth flow
- Credentials managed by Datadog and Claude Code
- No API keys stored in plugin configuration

### Audit Trail
- All tool calls are logged in Datadog's Audit Trail
- Searchable by event name "MCP Server"
- Includes user identity and tool arguments
