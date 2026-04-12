import textwrap

import snakemd

# Todo
#  - [ ] [Pangolin tunnel + Newt with OpenTelemetry + Grafana](https://medium.com/@Andreasrahimic/pangolin-tunnel-newt-opentelemetry-grafana-b2d2759aea0e)
#  - [ ] Farm Load Overall:
#        Prometheus-Query: `100 * (1 - avg(rate(node_cpu_seconds_total{mode="idle"}[$__rate_interval])))`

"""
Farm Load Overall:

{
  "id": 340,
  "type": "timeseries",
  "title": "Farm Load Overall",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 6,
    "w": 24
  },
  "fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "barWidthFactor": 0.6,
        "lineWidth": 1,
        "fillOpacity": 0,
        "gradientMode": "none",
        "spanNulls": false,
        "insertNulls": false,
        "showPoints": "auto",
        "showValues": false,
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "axisBorderShow": false,
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": false,
        "hideFrom": {
          "tooltip": false,
          "viz": false,
          "legend": false
        },
        "thresholdsStyle": {
          "mode": "off"
        },
        "lineStyle": {
          "fill": "solid"
        }
      },
      "color": {
        "mode": "palette-classic"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "value": null,
            "color": "green"
          },
          {
            "value": 80,
            "color": "red"
          }
        ]
      },
      "unit": "percent"
    },
    "overrides": [
      {
        "matcher": {
          "id": "byName",
          "options": "Value"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Farm Load Overall (user space)"
          }
        ]
      }
    ]
  },
  "pluginVersion": "12.4.2",
  "targets": [
    {
      "refId": "A",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[$__rate_interval])))",
      "range": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code"
    }
  ],
  "datasource": {
    "uid": "PBFA97CFB590B2093",
    "type": "prometheus"
  },
  "options": {
    "tooltip": {
      "mode": "single",
      "sort": "none",
      "hideZeros": false
    },
    "legend": {
      "showLegend": false,
      "displayMode": "list",
      "placement": "bottom",
      "calcs": []
    }
  }
}






{
  "id": 340,
  "type": "timeseries",
  "title": "Farm Load Overall",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 6,
    "w": 24
  },
  "fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "barWidthFactor": 0.6,
        "lineWidth": 1,
        "fillOpacity": 0,
        "gradientMode": "none",
        "spanNulls": false,
        "insertNulls": false,
        "showPoints": "auto",
        "showValues": false,
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "axisBorderShow": false,
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": false,
        "hideFrom": {
          "tooltip": false,
          "viz": false,
          "legend": false
        },
        "thresholdsStyle": {
          "mode": "off"
        },
        "lineStyle": {
          "fill": "solid"
        }
      },
      "color": {
        "mode": "palette-classic"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "green",
            "value": null
          },
          {
            "color": "red",
            "value": 80
          }
        ]
      },
      "unit": "percent"
    },
    "overrides": [
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Farm Load Overall (CPU user space)"
          },
          {
            "id": "custom.fillOpacity",
            "value": 30
          }
        ]
      },
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Load minions (CPU user space)"
          }
        ]
      },
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Load miniboss (CPU user space)"
          }
        ]
      }
    ]
  },
  "pluginVersion": "12.4.2",
  "targets": [
    {
      "refId": "A",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[$__rate_interval])))",
      "range": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code"
    },
    {
      "refId": "B",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[$__rate_interval])))",
      "range": true,
      "instant": false,
      "datasource": {
        "uid": "PBFA97CFB590B2093",
        "type": "prometheus"
      },
      "editorMode": "code",
      "legendFormat": "__auto"
    },
    {
      "refId": "C",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[$__rate_interval])))",
      "range": true,
      "instant": false,
      "datasource": {
        "uid": "PBFA97CFB590B2093",
        "type": "prometheus"
      },
      "editorMode": "code",
      "legendFormat": "__auto"
    }
  ],
  "datasource": {
    "uid": "PBFA97CFB590B2093",
    "type": "prometheus"
  },
  "options": {
    "tooltip": {
      "mode": "single",
      "sort": "none",
      "hideZeros": false
    },
    "legend": {
      "showLegend": false,
      "displayMode": "list",
      "placement": "bottom",
      "calcs": []
    }
  }
}
"""


"""
Panel JSON
{
  "id": 340,
  "type": "timeseries",
  "title": "Farm Load Overall",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 6,
    "w": 24
  },
  "fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "barWidthFactor": 0.6,
        "lineWidth": 1,
        "fillOpacity": 0,
        "gradientMode": "none",
        "spanNulls": false,
        "insertNulls": false,
        "showPoints": "auto",
        "showValues": false,
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "axisBorderShow": false,
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": false,
        "hideFrom": {
          "tooltip": false,
          "viz": false,
          "legend": false
        },
        "thresholdsStyle": {
          "mode": "off"
        },
        "lineStyle": {
          "fill": "solid"
        }
      },
      "color": {
        "mode": "palette-classic"
      },
      "mappings": [],
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "green",
            "value": null
          },
          {
            "color": "red",
            "value": 80
          }
        ]
      },
      "unit": "percent"
    },
    "overrides": [
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Farm Load Overall (CPU user space)"
          },
          {
            "id": "custom.fillOpacity",
            "value": 30
          }
        ]
      },
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Load minions (CPU user space)"
          }
        ]
      },
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Load miniboss (CPU user space)"
          }
        ]
      }
    ]
  },
  "pluginVersion": "12.4.2",
  "targets": [
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[$__rate_interval])))",
      "range": true,
      "refId": "A"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[$__rate_interval])))",
      "instant": false,
      "legendFormat": "__auto",
      "range": true,
      "refId": "B"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[$__rate_interval])))",
      "instant": false,
      "legendFormat": "__auto",
      "range": true,
      "refId": "C"
    }
  ],
  "datasource": {
    "type": "prometheus",
    "uid": "PBFA97CFB590B2093"
  },
  "options": {
    "tooltip": {
      "mode": "single",
      "sort": "none",
      "hideZeros": false
    },
    "legend": {
      "showLegend": false,
      "displayMode": "list",
      "placement": "bottom",
      "calcs": []
    }
  }
}
"""

"""
Panel Data
{
  "state": "Done",
  "series": [
    {
      "refId": "A",
      "meta": {
        "type": "timeseries-multi",
        "typeVersion": [
          0,
          1
        ],
        "custom": {
          "calculatedMinStep": 15000,
          "resultType": "matrix"
        },
        "executedQueryString": "Expr: 100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[1m0s])))\nStep: 15s",
        "preferredVisualisationType": "graph"
      },
      "fields": [
        {
          "name": "Time",
          "type": "time",
          "typeInfo": {
            "frame": "time.Time"
          },
          "config": {
            "interval": 15000,
            "custom": {
              "drawStyle": "line",
              "lineInterpolation": "smooth",
              "barAlignment": 0,
              "barWidthFactor": 0.6,
              "lineWidth": 1,
              "fillOpacity": 0,
              "gradientMode": "none",
              "showPoints": "auto",
              "showValues": false,
              "pointSize": 5,
              "axisPlacement": "auto",
              "axisColorMode": "text",
              "axisBorderShow": false,
              "axisCenteredZero": false,
              "hideFrom": {
                "tooltip": false,
                "viz": false,
                "legend": false
              },
              "thresholdsStyle": {
                "mode": "off"
              }
            },
            "unit": "percent",
            "color": {
              "mode": "palette-classic"
            },
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {
                  "color": "green",
                  "value": null
                },
                {
                  "color": "red",
                  "value": 80
                }
              ]
            }
          },
          "values": [
            1775293050000,
            1775293065000,
            1775293080000,
            1775293095000,
            1775293110000,
            1775293125000,
            1775293140000
          ],
          "entities": {},
          "state": {
            "scopedVars": {
              "__dataContext": "Filtered out in JSON serialization"
            },
            "displayName": "Time",
            "multipleFrames": true,
            "seriesIndex": 0,
            "nullThresholdApplied": true,
            "origin": {
              "frameIndex": 0,
              "fieldIndex": 0
            }
          }
        },
        {
          "name": "Value",
          "type": "number",
          "typeInfo": {
            "frame": "float64"
          },
          "labels": {},
          "config": {
            "displayNameFromDS": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[1m0s])))",
            "custom": {
              "drawStyle": "line",
              "lineInterpolation": "smooth",
              "barAlignment": 0,
              "barWidthFactor": 0.6,
              "lineWidth": 1,
              "fillOpacity": 30,
              "gradientMode": "none",
              "lineStyle": {
                "fill": "solid"
              },
              "spanNulls": false,
              "insertNulls": false,
              "showPoints": "auto",
              "showValues": false,
              "pointSize": 5,
              "stacking": {
                "mode": "none",
                "group": "A"
              },
              "axisPlacement": "auto",
              "axisLabel": "",
              "axisColorMode": "text",
              "axisBorderShow": false,
              "scaleDistribution": {
                "type": "linear"
              },
              "axisCenteredZero": false
            },
            "unit": "percent",
            "mappings": [],
            "displayName": "Farm Load Overall (CPU user space)"
          },
          "values": [
            56.01463427775637,
            32.55275866666162,
            21.62314814815074,
            22.328703703716645,
            22.266666666659564,
            24.096296296290053,
            24.60277777777433
          ],
          "entities": {},
          "state": {
            "scopedVars": {
              "__dataContext": "Filtered out in JSON serialization"
            },
            "multipleFrames": true,
            "displayName": "Farm Load Overall (CPU user space)",
            "seriesIndex": 0,
            "range": {
              "min": 5.947777777780894,
              "max": 100,
              "delta": 94.0522222222191
            }
          }
        }
      ],
      "length": 7
    },
    {
      "refId": "B",
      "meta": {
        "type": "timeseries-multi",
        "typeVersion": [
          0,
          1
        ],
        "custom": {
          "calculatedMinStep": 15000,
          "resultType": "matrix"
        },
        "executedQueryString": "Expr: 100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[1m0s])))\nStep: 15s",
        "preferredVisualisationType": "graph"
      },
      "fields": [
        {
          "name": "Time",
          "type": "time",
          "typeInfo": {
            "frame": "time.Time"
          },
          "config": {
            "interval": 15000,
            "custom": {
              "drawStyle": "line",
              "lineInterpolation": "smooth",
              "barAlignment": 0,
              "barWidthFactor": 0.6,
              "lineWidth": 1,
              "fillOpacity": 0,
              "gradientMode": "none",
              "showPoints": "auto",
              "showValues": false,
              "pointSize": 5,
              "axisPlacement": "auto",
              "axisColorMode": "text",
              "axisBorderShow": false,
              "axisCenteredZero": false
            },
            "unit": "percent"
          },
          "values": [
            1775293050000,
            1775293065000,
            1775293080000,
            1775293095000,
            1775293110000,
            1775293125000,
            1775293140000
          ],
          "entities": {},
          "state": {
            "scopedVars": {
              "__dataContext": "Filtered out in JSON serialization"
            },
            "displayName": "Time",
            "multipleFrames": true,
            "seriesIndex": 1,
            "nullThresholdApplied": true,
            "origin": {
              "frameIndex": 1,
              "fieldIndex": 0
            }
          }
        },
        {
          "name": "Value",
          "type": "number",
          "typeInfo": {
            "frame": "float64"
          },
          "labels": {},
          "config": {
            "displayNameFromDS": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[1m0s])))",
            "custom": {
              "drawStyle": "line",
              "lineInterpolation": "smooth",
              "barAlignment": 0,
              "barWidthFactor": 0.6,
              "lineWidth": 1,
              "fillOpacity": 0,
              "gradientMode": "none",
              "spanNulls": false,
              "insertNulls": false,
              "showPoints": "auto",
              "showValues": false,
              "pointSize": 5,
              "axisPlacement": "auto",
              "axisLabel": "",
              "axisColorMode": "text",
              "axisBorderShow": false,
              "axisCenteredZero": false
            },
            "unit": "percent",
            "displayName": "Load minions (CPU user space)"
          },
          "values": [
            56.01463427775637,
            32.55275866666162,
            5.947777777780894,
            6.794444444459979,
            6.719999999991466,
            8.91555555554806,
            9.523333333329209
          ],
          "entities": {},
          "state": {
            "calcs": {
              "sum": 126.46850405552762,
              "max": 56.01463427775637,
              "min": 5.947777777780894,
              "logmin": 5.947777777780894,
              "mean": 18.066929150789658,
              "last": 9.523333333329209,
              "first": 56.01463427775637,
              "lastNotNull": 9.523333333329209,
              "firstNotNull": 56.01463427775637,
              "count": 7,
              "nonNullCount": 7,
              "allIsNull": false,
              "allIsZero": false,
              "range": 50.06685649997548,
              "diff": -46.49130094442717,
              "delta": 0.6077777777811484,
              "step": -26.604980888880725,
              "diffperc": -82.99849056211556,
              "previousDeltaUp": true
            },
            "scopedVars": {
              "__dataContext": "Filtered out in JSON serialization"
            },
            "multipleFrames": true,
            "displayName": "Load minions (CPU user space)",
            "seriesIndex": 1,
            "range": {
              "min": 5.947777777780894,
              "max": 100,
              "delta": 94.0522222222191
            }
          }
        }
      ],
      "length": 7
    },
    {
      "refId": "C",
      "meta": {
        "type": "timeseries-multi",
        "typeVersion": [
          0,
          1
        ],
        "custom": {
          "calculatedMinStep": 15000,
          "resultType": "matrix"
        },
        "executedQueryString": "Expr: 100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[1m0s])))\nStep: 15s",
        "preferredVisualisationType": "graph"
      },
      "fields": [
        {
          "name": "Time",
          "type": "time",
          "typeInfo": {
            "frame": "time.Time"
          },
          "config": {
            "interval": 15000,
            "custom": {
              "drawStyle": "line",
              "lineInterpolation": "smooth",
              "barAlignment": 0,
              "barWidthFactor": 0.6,
              "lineWidth": 1,
              "fillOpacity": 0,
              "gradientMode": "none",
              "showPoints": "auto",
              "showValues": false,
              "pointSize": 5,
              "axisPlacement": "auto",
              "axisColorMode": "text",
              "axisBorderShow": false,
              "axisCenteredZero": false
            },
            "unit": "percent"
          },
          "values": [
            1775293080000,
            1775293095000,
            1775293110000,
            1775293125000,
            1775293140000
          ],
          "entities": {},
          "state": {
            "scopedVars": {
              "__dataContext": "Filtered out in JSON serialization"
            },
            "displayName": "Time",
            "multipleFrames": true,
            "seriesIndex": 2,
            "nullThresholdApplied": true,
            "origin": {
              "frameIndex": 2,
              "fieldIndex": 0
            }
          }
        },
        {
          "name": "Value",
          "type": "number",
          "typeInfo": {
            "frame": "float64"
          },
          "labels": {},
          "config": {
            "displayNameFromDS": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[1m0s])))",
            "custom": {
              "drawStyle": "line",
              "lineInterpolation": "smooth",
              "barAlignment": 0,
              "barWidthFactor": 0.6,
              "lineWidth": 1,
              "fillOpacity": 0,
              "gradientMode": "none",
              "spanNulls": false,
              "insertNulls": false,
              "showPoints": "auto",
              "showValues": false,
              "pointSize": 5,
              "axisPlacement": "auto",
              "axisLabel": "",
              "axisColorMode": "text",
              "axisBorderShow": false,
              "axisCenteredZero": false
            },
            "unit": "percent",
            "displayName": "Load miniboss (CPU user space)"
          },
          "values": [
            100,
            100,
            100,
            100,
            100
          ],
          "entities": {},
          "state": {
            "calcs": {
              "sum": 500,
              "max": 100,
              "min": 100,
              "logmin": 100,
              "mean": 100,
              "last": 100,
              "first": 100,
              "lastNotNull": 100,
              "firstNotNull": 100,
              "count": 5,
              "nonNullCount": 5,
              "allIsNull": false,
              "allIsZero": false,
              "range": 0,
              "diff": 0,
              "delta": 0,
              "step": 0,
              "diffperc": 0,
              "previousDeltaUp": true
            },
            "scopedVars": {
              "__dataContext": "Filtered out in JSON serialization"
            },
            "multipleFrames": true,
            "displayName": "Load miniboss (CPU user space)",
            "seriesIndex": 2,
            "range": {
              "min": 5.947777777780894,
              "max": 100,
              "delta": 94.0522222222191
            }
          }
        }
      ],
      "length": 5
    }
  ],
  "annotations": [],
  "request": {
    "app": "dashboard",
    "requestId": "SQR2868",
    "timezone": "browser",
    "range": {
      "to": "2026-04-04T08:59:08.563Z",
      "from": "2026-04-04T05:59:08.563Z",
      "raw": {
        "from": "now-3h",
        "to": "now"
      }
    },
    "interval": "15s",
    "intervalMs": 15000,
    "targets": [
      {
        "datasource": {
          "type": "prometheus",
          "uid": "PBFA97CFB590B2093"
        },
        "editorMode": "code",
        "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[$__rate_interval])))",
        "range": true,
        "refId": "A"
      },
      {
        "datasource": {
          "type": "prometheus",
          "uid": "PBFA97CFB590B2093"
        },
        "editorMode": "code",
        "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[$__rate_interval])))",
        "instant": false,
        "legendFormat": "__auto",
        "range": true,
        "refId": "B"
      },
      {
        "datasource": {
          "type": "prometheus",
          "uid": "PBFA97CFB590B2093"
        },
        "editorMode": "code",
        "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[$__rate_interval])))",
        "instant": false,
        "legendFormat": "__auto",
        "range": true,
        "refId": "C"
      }
    ],
    "maxDataPoints": 1248,
    "scopedVars": {
      "__sceneObject": "Filtered out in JSON serialization",
      "__interval": {
        "text": "15s",
        "value": "15s"
      },
      "__interval_ms": {
        "text": "15000",
        "value": 15000
      }
    },
    "startTime": 1775293148563,
    "rangeRaw": {
      "from": "now-3h",
      "to": "now"
    },
    "dashboardUID": "rYdddlPWk",
    "panelId": 340,
    "panelName": "Farm Load Overall",
    "panelPluginId": "timeseries",
    "dashboardTitle": "Node Exporter Full",
    "endTime": 1775293148894
  },
  "timings": {
    "dataProcessingTime": 0
  },
  "structureRev": 4
}
"""


"""
Panel JSON:
{
  "id": 340,
  "type": "timeseries",
  "title": "Farm Load Overall",
  "gridPos": {
    "x": 0,
    "y": 0,
    "h": 6,
    "w": 24
  },
  "fieldConfig": {
    "defaults": {
      "custom": {
        "drawStyle": "line",
        "lineInterpolation": "smooth",
        "barAlignment": 0,
        "barWidthFactor": 0.6,
        "lineWidth": 1,
        "fillOpacity": 0,
        "gradientMode": "none",
        "spanNulls": false,
        "insertNulls": false,
        "showPoints": "auto",
        "showValues": false,
        "pointSize": 5,
        "stacking": {
          "mode": "none",
          "group": "A"
        },
        "axisPlacement": "auto",
        "axisLabel": "",
        "axisColorMode": "text",
        "axisBorderShow": false,
        "scaleDistribution": {
          "type": "linear"
        },
        "axisCenteredZero": false,
        "hideFrom": {
          "tooltip": false,
          "viz": false,
          "legend": false
        },
        "thresholdsStyle": {
          "mode": "off"
        },
        "lineStyle": {
          "fill": "solid"
        }
      },
      "color": {
        "mode": "thresholds",
        "seriesBy": "last"
      },
      "mappings": [],
      "thresholds": {
        "mode": "percentage",
        "steps": [
          {
            "color": "green",
            "value": null
          },
          {
            "value": 80,
            "color": "red"
          }
        ]
      },
      "max": 100,
      "min": 0,
      "unit": "percent"
    },
    "overrides": [
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - min(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "custom.fillOpacity",
            "value": 0
          },
          {
            "id": "custom.fillBelowTo",
            "value": "100 * (1 - max(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[1m0s])))"
          },
          {
            "id": "custom.drawStyle",
            "value": "line"
          },
          {
            "id": "displayName",
            "value": "Minions Max"
          },
          {
            "id": "custom.showPoints",
            "value": "never"
          }
        ]
      },
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Minions Avg"
          },
          {
            "id": "color",
            "value": {
              "mode": "fixed",
              "fixedColor": "dark-orange"
            }
          }
        ]
      },
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - max(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Minions Min"
          },
          {
            "id": "custom.showPoints",
            "value": "never"
          }
        ]
      },
      {
        "matcher": {
          "id": "byName",
          "options": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[1m0s])))"
        },
        "properties": [
          {
            "id": "displayName",
            "value": "Miniboss"
          },
          {
            "id": "custom.showPoints",
            "value": "never"
          }
        ]
      }
    ]
  },
  "pluginVersion": "12.4.2",
  "targets": [
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{mode=\"idle\"}[$__rate_interval])))",
      "range": true,
      "refId": "Farm Load Overall Avg CPU"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^miniboss-alloy-default$\", mode=\"idle\"}[$__rate_interval])))",
      "instant": false,
      "legendFormat": "__auto",
      "range": true,
      "refId": "Miniboss Avg CPU"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code",
      "expr": "100 * (1 - max(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[$__rate_interval])))",
      "instant": false,
      "legendFormat": "__auto",
      "range": true,
      "refId": "Minions Min CPU"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code",
      "expr": "100 * (1 - avg(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[$__rate_interval])))",
      "instant": false,
      "legendFormat": "__auto",
      "range": true,
      "refId": "Minions Avg CPU"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "editorMode": "code",
      "expr": "100 * (1 - min(rate(node_cpu_seconds_total{instance=~\"^minion[0-9]{2}-alloy-worker$\",  mode=\"idle\"}[$__rate_interval])))",
      "instant": false,
      "legendFormat": "__auto",
      "range": true,
      "refId": "Minions Max CPU"
    }
  ],
  "datasource": {
    "type": "prometheus",
    "uid": "PBFA97CFB590B2093"
  },
  "options": {
    "tooltip": {
      "mode": "single",
      "sort": "none",
      "hideZeros": false
    },
    "legend": {
      "showLegend": false,
      "displayMode": "list",
      "placement": "bottom",
      "calcs": []
    }
  }
}
"""


# Todo
#  - [ ] https://grafana.com/grafana/plugins/grafana-image-renderer/


def readme_feature(
    doc: snakemd.Document,
    main_header: str,
) -> snakemd.Document:

    # Some Specific information

    doc.add_heading(
        text=main_header,
        level=1,
    )

    doc.add_quote(text=textwrap.dedent("""\
            [!CAUTION]

            Starting with Grafana release `12.4.0`,
            the `grafana/grafana-oss` Docker Hub
            repository will no longer be updated.
            Instead, we encourage you to use
            the `grafana/grafana` Docker Hub
            repository. These two repositories
            have the same Grafana OSS docker images.

            ([Source](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/))\
            """))

    # Logo

    doc.add_paragraph(
        snakemd.Inline(
            text=textwrap.dedent("""\
                Logo Grafana\
                """),
            image="https://grafana.com/media/products/cloud/grafana/grafana-product-logo.svg",
            link="https://grafana.com/grafana/",
        ).__str__()
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            Grafana is written and maintained by Grafana Labs.\
            """))

    # Logo

    # doc.add_paragraph(
    #     snakemd.Inline(
    #         text=textwrap.dedent(
    #             """
    #             Logo Ynput
    #             """
    #         ),
    #         image={
    #             "Ynput": "https://ynput.io/wp-content/uploads/2022/09/ynput-logo-small-bg.svg",
    #         }["Ynput"],
    #         link="https://ynput.io",
    #     ).__str__()
    # )

    doc.add_paragraph(text=textwrap.dedent("""\
            Grafana Labs offers different versions of Grafana:\
            """))

    doc.add_unordered_list(
        [
            "OSS",
            "Enterprise",
        ]
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            `OpenStudioLandscapes-Grafana` is based on the [OSS](https://ynput.io/ayon/pricing/)
            version provided by their own Docker image:\
            """))

    doc.add_unordered_list(
        [
            "[`docker.io/grafana/grafana`](https://hub.docker.com/r/grafana/grafana)",
        ]
    )

    doc.add_heading(
        text="Official Documentation",
        level=2,
    )

    doc.add_unordered_list(
        [
            "[Setup](https://grafana.com/docs/grafana/latest/setup-grafana/)",
            "[Install](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)",
            "[Configure a Docker Image](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/)",
            "[Administration](https://grafana.com/docs/grafana/latest/administration/)",
        ]
    )

    doc.add_heading(
        text="Grafana Alloy",
        level=3,
    )

    # Default Ports:
    # # Grafana
    #   [x] running
    #   3000
    #
    # # Loki
    #   [x] running
    #   3100
    #   Endpoints:
    #   - https://grafana.com/docs/loki/latest/reference/loki-http-api/
    #     - /metrics
    #
    # # Prometheus
    #   [x] running
    #   9090
    #   Endpoints:
    #   - https://prometheus.io/docs/prometheus/latest/querying/api/
    #     - /api/v1/status/config
    #
    # # Alloy
    #   [x] running
    #   12345

    # Todo:
    #  - [ ] Can this be helpful?
    #        - Alloy Configurator: https://github.com/grafana/alloy-configurator

    doc.add_paragraph(text=textwrap.dedent("""\
            Alloy can collect, process, 
            and export telemetry signals to 
            scale and future-proof your observability approach.
            More info:\
            """))

    doc.add_unordered_list(
        [
            "[https://grafana.com/docs/alloy/latest/](https://grafana.com/docs/alloy/latest/)",
        ]
    )

    doc.add_heading(
        text="Alloy Scenarios",
        level=4,
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            This repository contains scenarios that 
            demonstrate how to use Grafana Alloy to 
            monitor various data sources. 
            Each scenario is a self-contained example 
            which will include an LGMT stack 
            (Loki, Grafana, Metrics, Tempo) and an 
            Alloy configuration file.\
            """))

    doc.add_unordered_list(
        [
            "[https://github.com/grafana/alloy-scenarios/](https://github.com/grafana/alloy-scenarios/)",
        ]
    )

    doc.add_heading(
        text="Configure Grafana",
        level=2,
    )

    doc.add_heading(
        text="Default Paths",
        level=3,
    )

    doc.add_unordered_list(
        [
            "[Default paths](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/#default-paths)",
        ]
    )

    doc.add_heading(
        text="`defaults.ini`",
        level=3,
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            As it turned out, the contents of the `defaults.ini` file are
            tied to the Grafana version. A mismatch can lead to a non-functional
            container (see [issue](https://github.com/michimussato/OpenStudioLandscapes-Grafana/issues/7)).
            Hence, the `defaults.ini` file can't be managed by an OpenStudioLandscapes Dagster asset
            without compromising cross-version compatibility.
            The main entry point for Grafana configuration is therefore the [`grafana.ini`](#grafanaini) file
            (exclusively).
            """))

    doc.add_heading(
        text="`grafana.ini`",
        level=3,
    )

    doc.add_unordered_list(
        [
            "[Configure Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/)",
        ]
    )

    # doc.add_heading(
    #     text="A",
    #     level=3,
    # )
    #
    # doc.add_unordered_list(
    #     [
    #         "[REST API Docs](https://docs.ayon.dev/api)",
    #         "[GraphQL API Explorer](https://playground.ayon.app/explorer)",
    #         "[Python API Docs](https://docs.ayon.dev/ayon-python-api)",
    #         "[C++ API Docs](https://docs.ayon.dev/ayon-cpp-api)",
    #         "[USD Resolver Docs](https://docs.ayon.dev/ayon-usd-resolver)",
    #         "[Frontend React Components](https://components.ayon.dev)",
    #     ]
    # )

    doc.add_horizontal_rule()

    return doc


if __name__ == "__main__":
    pass
